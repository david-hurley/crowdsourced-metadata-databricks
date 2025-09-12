import dash
from dash import html, Input, Output, State, callback, callback_context
import dash_ag_grid as dag
import pandas as pd
from sample_data import sample_data
from config import column_definitions, grid_options, default_column_def

app = dash.Dash(__name__)
df = pd.DataFrame(sample_data)

app.layout = html.Div([
    html.Div([
        html.H1("User Portal: Crowdsourced Metadata - Databricks", 
                style={"textAlign": "center", "marginBottom": "30px", "color": "#2c3e50"}),
        html.P("Submit comments and tags", 
               style={"textAlign": "center", "marginBottom": "30px", "color": "#7f8c8d"})
    ]),
    
    html.Div([
        dag.AgGrid(
            id="metadata-grid",
            rowData=df.to_dict('records'),
            columnDefs=column_definitions,
            defaultColDef=default_column_def,
            dashGridOptions=grid_options,
            style={"height": "600px", "width": "100%"}
        )
    ], style={"margin": "20px"}),
    
    html.Div([
        html.Button("Save Data", id="refresh-btn", n_clicks=0,
                   style={"padding": "10px 20px", "backgroundColor": "#27ae60", "color": "white", "border": "none", "borderRadius": "5px"})
    ], style={"textAlign": "center", "marginTop": "20px"})
], style={"fontFamily": "Arial, sans-serif", "backgroundColor": "#f5f6fa", "minHeight": "100vh"})

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            .ag-theme-alpine .ag-header {
                background-color: #34495e !important;
                color: white !important;
            }
            .ag-theme-alpine .ag-header-cell-label {
                color: white !important;
            }
            .ag-theme-alpine .ag-header-cell-text {
                color: white !important;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

@callback(
    Output("metadata-grid", "rowData"),
    [Input("refresh-btn", "n_clicks"), Input("metadata-grid", "cellValueChanged")],
    State("metadata-grid", "rowData"),
    prevent_initial_call=True
)
def handle_updates(save_clicks, cell_changed, row_data):
    ctx = callback_context
    if not ctx.triggered:
        return row_data
    
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if trigger_id == "refresh-btn":
        print("Saving data...")
        print(f"Data to save: {row_data}")
    elif trigger_id == "metadata-grid":
        print(f"Cell edited: {cell_changed}")
    
    return row_data

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
