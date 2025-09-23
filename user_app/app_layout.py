# layout.py
from dash import html, dcc
import dash_ag_grid as dag

def get_grid_options():
    """Grid options"""
    return {
        "rowHeight": 60,
        "headerHeight": 50,
        "pagination": True,
        "paginationPageSize": 25,
        "paginationPageSizeSelector": [10, 25, 50, 100],
        "suppressRowHoverHighlight": False,
        "rowSelection": "multiple",
        "stopEditingWhenCellsLoseFocus": True,
        "undoRedoCellEditing": True,
        "animateRows": True,
        "suppressColumnVirtualisation": True,
        "suppressRowVirtualisation": False,
        "enableCellTextSelection": True,
        "ensureDomOrder": True,
        "suppressHorizontalScroll": False,
        "alwaysShowHorizontalScroll": False,
        "suppressColumnMoveAnimation": True,
        "suppressRowTransform": False
    }

def get_default_column_def():
    """Default column properties"""
    return {
        "resizable": True,
        "sortable": True
    }

def make_column_defs(df_tags_comments, df_glossary_tags):
    # Define the specific columns to show in the grid with responsive widths
    column_defs = [
        {
            "headerName": "Entity Type",
            "field": "entity_type",
            "editable": False,
            "width": 80,
            "minWidth": 80,
            "maxWidth": 100,
            "cellStyle": {"textAlign": "center"},
            "wrapHeaderText": True
        },
        {
            "headerName": "Entity Path",
            "field": "entity_path",
            "editable": False,
            "width": 200,
            "minWidth": 150,
            "flex": 1,
            "cellStyle": {"textAlign": "left", "whiteSpace": "normal", "wordWrap": "break-word"},
            "wrapHeaderText": True,
            "wrapText": True,
            "autoHeight": True
        },
        {
            "headerName": "Current Comment",
            "field": "current_comment",
            "editable": False,
            "width": 200,
            "minWidth": 150,
            "flex": 1,
            "cellStyle": {"textAlign": "left", "whiteSpace": "normal", "wordWrap": "break-word"},
            "wrapText": True,
            "autoHeight": True,
            "wrapHeaderText": True
        },
        {
            "headerName": "Proposed Comment",
            "field": "proposed_comment",
            "editable": False,
            "width": 200,
            "minWidth": 150,
            "flex": 1,
            "cellStyle": {"textAlign": "left", "whiteSpace": "normal", "wordWrap": "break-word"},
            "wrapText": True,
            "autoHeight": True,
            "wrapHeaderText": True
        },
        {
            "headerName": "Glossary Tag",
            "field": "glossary_tag",
            "editable": {
                "function": "params.data.approval_status !== 'pending'"
            },
            "cellEditor": "agSelectCellEditor",
            "cellEditorParams": {
                "values": df_glossary_tags['tag'].dropna().unique().tolist()
            },
            "width": 120,
            "minWidth": 100,
            "maxWidth": 150,
            "cellStyle": {"textAlign": "center"},
            "wrapHeaderText": True
        },
        {
            "headerName": "Review Status",
            "field": "approval_status",
            "editable": False,
            "width": 120,
            "minWidth": 100,
            "maxWidth": 140,
            "cellStyle": {"textAlign": "center", "fontWeight": "bold"},
            "wrapHeaderText": True,
            "cellRenderer": "function(params) { return params.value ? `<span class='status-${params.value}'>${params.value}</span>` : ''; }"
        },
        {
            "headerName": "Review Comment",
            "field": "reason_for_not_approved",
            "editable": False,
            "width": 200,
            "minWidth": 150,
            "flex": 1,
            "cellStyle": {"textAlign": "left", "whiteSpace": "normal", "wordWrap": "break-word"},
            "wrapText": True,
            "autoHeight": True,
            "wrapHeaderText": True
        },
        {
            "headerName": "Sent for Review",
            "field": "saved",
            "editable": False,
            "width": 100,
            "minWidth": 80,
            "maxWidth": 120,
            "cellStyle": {"textAlign": "center", "fontWeight": "bold"},
            "cellRenderer": "function(params) { return `<span class='${params.value === '❌' ? 'unsaved-status' : 'saved-status'}'>${params.value}</span>`; }",
            "wrapHeaderText": True
        }
    ]
    
    return column_defs

def create_layout():
    layout = html.Div([
        dcc.Store(id="data-store", storage_type="memory"),
        html.Div(id="dummy", style={"display": "none"}),

        # Main container with modern styling
        html.Div([
            # Header section
            html.Div([
                html.H1("User Portal: Crowdsourced Metadata - Databricks"),
                html.P("Set Entity Comments with Governed Glossary Tags. Current and proposed comments sync once per day")
            ], className="header-section"),

            # Content section
            html.Div([
                # Grid section wrapped in Loading spinner
                html.Div([
                    dcc.Loading(
                        id="loading-grid",
                        type="circle",
                        children=[
                            dag.AgGrid(
                                id="metadata-grid",
                                rowData=[],
                                columnDefs=[{"headerName": "Loading...", "field": "dummy"}],
                                defaultColDef=get_default_column_def(),
                                dashGridOptions={
                                    **get_grid_options(),
                                    "rowClassRules": {
                                        "unsaved-row": "params.data.saved === '❌'"
                                    }
                                },
                                style={"height": "600px", "width": "100%"},
                                className="ag-theme-alpine"
                            )
                        ],
                        style={"height": "600px"}
                    )
                ], className="grid-container"),

                # Save button section
                html.Div([
                    html.Button(
                        "💾 Save Changes",
                        id="save-btn",
                        n_clicks=0,
                        className="save-btn"
                    )
                ], className="save-section")
            ], className="content-section")
        ], className="main-container")
    ])

    return layout
