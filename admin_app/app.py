import dash
from dash import html, dcc, Input, Output, State, callback_context
import dash_ag_grid as dag
import pandas as pd

from utils.get_signed_in_user_email import get_signed_in_user_email
from utils.lakebase_client import LakebaseClient
from app_css import get_app_css
from app_layout import create_layout, make_column_defs

# Constants
UNSAVED_STATUS = '❌'
SAVED_STATUS = '✅'
PENDING_STATUS = 'pending'
GLOSSARY_TAG_COLUMN = 'glossary_tag'
PROPOSED_COMMENT_COLUMN = 'proposed_comment'
ENTITY_PATH_COLUMN = 'entity_path'
SAVED_COLUMN = 'saved'

# Database queries
ENTITIES_QUERY = """
    -- Main query to fetch entity metadata with approval status
    -- Joins current system comments (t1) with proposed changes (t2)
    -- Calculates approval_status based on comment differences and approval state
    select 
    t1.entity_path,
    t1.comment as proposed_comment,
    t1.glossary_tag,
    t1.approved,
    t1.reason_for_not_approved
    from "public"."david_hurley"."governed_entity_change_record" as t1
    where t1.approved is not true
"""

SAVE_QUERY = """
    -- Update existing records where entity_path matches
    -- Only updates approved and reason_for_not_approved fields
    UPDATE public.david_hurley.governed_entity_change_record
    SET 
        approved = %s,
        reason_for_not_approved = %s
    WHERE entity_path = %s

"""

app = dash.Dash(__name__)
app.index_string = get_app_css()
app.layout = create_layout()

# Helper functions

def is_row_editable(approval_status):
    """Check if a row can be edited based on approval status."""
    return approval_status != PENDING_STATUS

def extract_user_changes(current_row_data):
    """Extract unsaved user changes from current row data."""
    user_changes = {}
    for row in current_row_data:
        if row.get(SAVED_COLUMN) == UNSAVED_STATUS:
            user_changes[row.get(ENTITY_PATH_COLUMN)] = {
                GLOSSARY_TAG_COLUMN: row.get(GLOSSARY_TAG_COLUMN, ''),
                PROPOSED_COMMENT_COLUMN: row.get(PROPOSED_COMMENT_COLUMN, ''),
                SAVED_COLUMN: row.get(SAVED_COLUMN, SAVED_STATUS)
            }
    return user_changes

def apply_user_changes(entities_data, user_changes):
    """Apply user changes to entities data."""
    for row in entities_data:
        entity_path = row.get(ENTITY_PATH_COLUMN)
        if entity_path in user_changes:
            changes = user_changes[entity_path]
            row[GLOSSARY_TAG_COLUMN] = changes.get(GLOSSARY_TAG_COLUMN, '')
            row[PROPOSED_COMMENT_COLUMN] = changes.get(PROPOSED_COMMENT_COLUMN, '')
            row[SAVED_COLUMN] = changes.get(SAVED_COLUMN, SAVED_STATUS)

def initialize_row_data(entities_data):
    """Initialize default values for row data."""
    for row in entities_data:
        # Set row lock status
        approval_status = row.get("approval_status")
        row["_locked"] = (approval_status == PENDING_STATUS)
        
        # Set default values
        if GLOSSARY_TAG_COLUMN not in row or row[GLOSSARY_TAG_COLUMN] is None:
            row[GLOSSARY_TAG_COLUMN] = ""
        if SAVED_COLUMN not in row:
            row[SAVED_COLUMN] = SAVED_STATUS
        # Ensure approved field is always a boolean (not null)
        if "approved" not in row or row["approved"] is None:
            row["approved"] = False

@app.callback(
    Output("data-store", "data"),
    Input("dummy", "id"),
    prevent_initial_call=False
)
def load_data(_):
    """Load entities and glossary data from database."""
    signed_in_user_email = get_signed_in_user_email()
    client = LakebaseClient()

    try:
        # Query entities data
        df_entities = client.query(ENTITIES_QUERY.format(user_email=signed_in_user_email))
        return {
            "entities": df_entities.to_dict("records"),
        }
    finally:
        client.close()

@app.callback(
    Output("metadata-grid", "rowData"),
    Output("metadata-grid", "columnDefs"),
    Input("data-store", "data"),
    State("metadata-grid", "rowData")
)
def update_grid(data, current_row_data):
    """Update grid with fresh data while preserving user changes."""
    if not data or "entities" not in data:
        return [], []

    # Prepare data for column definitions
    df_tags_comments = pd.DataFrame(data["entities"])
    column_defs = make_column_defs(df_tags_comments)

    # Get fresh entities data
    entities_data = data["entities"].copy()
    
    # Preserve user changes if they exist
    if current_row_data and len(current_row_data) > 0:
        user_changes = extract_user_changes(current_row_data)
        apply_user_changes(entities_data, user_changes)
    
    # Initialize row data with defaults
    initialize_row_data(entities_data)

    return entities_data, column_defs

def save_unsaved_rows(row_data):
    """Save all unsaved rows to database."""
    if not isinstance(row_data, list):
        return row_data
        
    client = LakebaseClient()
    try:
        for row in row_data:
            if not isinstance(row, dict):
                continue
                
            approval_status = row.get('approval_status')
            if row.get(SAVED_COLUMN) == UNSAVED_STATUS and is_row_editable(approval_status):
                # Use proposed comment if exists, otherwise current comment
                comment_to_save = (row.get(PROPOSED_COMMENT_COLUMN) or 
                                 row.get("current_comment") or "")
                
                client.execute(
                    SAVE_QUERY,
                    (
                        row.get("approved"),  # Use the checkbox value
                        row.get("reason_for_not_approved"),  # Use the comment value
                        row.get(ENTITY_PATH_COLUMN)  # WHERE clause parameter
                    )
                )
                row[SAVED_COLUMN] = SAVED_STATUS
    finally:
        client.close()
    
    return row_data


@app.callback(
    Output("metadata-grid", "rowData", allow_duplicate=True),
    Input("save-btn", "n_clicks"),
    Input("metadata-grid", "cellValueChanged"),
    State("metadata-grid", "rowData"),
    State("data-store", "data"),
    prevent_initial_call=True
)
def handle_updates(save_clicks, cell_changed, row_data, data_store):
    """Handle save button clicks and cell changes."""
    ctx = callback_context
    if not ctx.triggered:
        return row_data

    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == "save-btn":
        return save_unsaved_rows(row_data)
    elif trigger_id == "metadata-grid" and cell_changed:
        # Handle cell changes
        changed_cell = cell_changed[0]
        if changed_cell.get('colId') == 'approved':
            # Just update the value, don't mark as unsaved
            pass
        elif changed_cell.get('colId') == 'reason_for_not_approved':
            # Mark as unsaved when comment is changed
            row_idx = changed_cell.get('rowIndex', 0)
            if row_idx < len(row_data):
                row_data[row_idx][SAVED_COLUMN] = UNSAVED_STATUS

    return row_data

@app.callback(
    Output("data-store", "data", allow_duplicate=True),
    Input("save-btn", "n_clicks"),
    prevent_initial_call=True
)
def reload_data_after_save(save_clicks):
    """Reload fresh data after save button is clicked."""
    if save_clicks:
        return load_data("dummy")
    return dash.no_update

if __name__ == "__main__":
    app.run(debug=True)
