# Configuration file for column definitions and tag settings

# Predefined glossary tags
glossary_tags = [
    "#user", "#authentication", "#contact", "#identifier", "#primary_key", "#foreign_key",
    "#audit", "#timestamp", "#creation", "#activity", "#action", "#classification",
    "#order", "#amount", "#financial", "#status", "#workflow", "#product", "#name", "#display",
    "#price", "#commerce", "#analytics", "#behavior", "#reference", "#enum", "#state",
    "#pii", "#unique", "#auto_increment", "#required", "#system", "#readonly", "#datetime",
    "#money", "#calculated", "#text", "#decimal"
]

# Column definitions for AG Grid
column_definitions = [
    {
        "field": "catalog",
        "headerName": "Catalog",
        "width": 120,
        "cellStyle": {"textAlign": "center", "fontWeight": "bold"},
        "cellRenderer": "agTextCellRenderer"
    },
    {
        "field": "schema",
        "headerName": "Schema",
        "width": 120,
        "cellStyle": {"textAlign": "center", "fontWeight": "bold"},
        "cellRenderer": "agTextCellRenderer"
    },
    {
        "field": "table",
        "headerName": "Table",
        "width": 150,
        "cellStyle": {"fontWeight": "bold", "color": "#2c3e50"}
    },
    {
        "field": "column",
        "headerName": "Column",
        "width": 150,
        "cellStyle": {"fontWeight": "bold", "color": "#34495e"}
    },
    {
        "field": "comment",
        "headerName": "Comment",
        "width": 300,
        "wrapText": True,
        "autoHeight": True,
        "cellStyle": {"backgroundColor": "#f8f9fa", "padding": "8px"},
        "editable": True,
        "cellEditor": "agTextCellEditor",
        "cellEditorParams": {
            "maxLength": 1000,
            "useFormatter": True
        }
    },
    {
        "field": "glossary tag",
        "headerName": "Glossary Tag",
        "width": 200,
        "wrapText": True,
        "autoHeight": True,
        "cellStyle": {"backgroundColor": "#e8f5e8", "padding": "8px"},
        "editable": True,
        "cellEditor": "agSelectCellEditor",
        "cellEditorParams": {
            "values": glossary_tags,
            "multiple": True,
            "separator": ","
        },
        "cellRenderer": "agTextCellRenderer"
    },
    {
        "field": "other tags",
        "headerName": "Other Tags",
        "width": 200,
        "wrapText": True,
        "autoHeight": True,
        "cellStyle": {"backgroundColor": "#fff3cd", "padding": "8px"},
        "editable": True,
        "cellEditor": "agTextCellEditor",
        "cellEditorParams": {
            "maxLength": 500,
            "useFormatter": True
        }
    }
]

# Grid options
grid_options = {
    "rowHeight": 60,
    "headerHeight": 40,
    "pagination": True,
    "paginationPageSize": 20,
    "suppressRowHoverHighlight": False,
    "rowSelection": "multiple",
    "stopEditingWhenCellsLoseFocus": True,
    "undoRedoCellEditing": True
}

# Default column properties
default_column_def = {
    "resizable": True,
    "sortable": True
}
