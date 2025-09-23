def get_app_css():
    """Get the CSS styling for the app."""
    return '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            * {
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
            }
            
            .main-container {
                background: white;
                margin: 20px;
                border-radius: 16px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                overflow: hidden;
                min-height: calc(100vh - 40px);
            }
            
            .header-section {
                background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
                color: white;
                padding: 40px 30px;
                text-align: center;
            }
            
            .header-section h1 {
                margin: 0 0 10px 0;
                font-size: 2.5rem;
                font-weight: 700;
                letter-spacing: -0.5px;
            }
            
            .header-section p {
                margin: 0;
                font-size: 1.1rem;
                opacity: 0.9;
                font-weight: 300;
            }
            
            .content-section {
                padding: 30px;
            }
            
            .grid-container {
                background: white;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08);
                overflow: hidden;
                margin-bottom: 30px;
            }
            
            .save-section {
                text-align: center;
                padding: 20px 0;
            }
            
            .save-btn {
                background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
                color: white;
                border: none;
                padding: 15px 40px;
                border-radius: 50px;
                font-size: 1.1rem;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(39, 174, 96, 0.3);
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            
            .save-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(39, 174, 96, 0.4);
            }
            
            .save-btn:active {
                transform: translateY(0);
            }
            
            /* AG Grid Styling */
            .ag-theme-alpine {
                --ag-header-background-color: #34495e;
                --ag-header-foreground-color: white;
                --ag-border-color: #e1e8ed;
                --ag-row-hover-color: #f8f9fa;
                --ag-selected-row-background-color: #e3f2fd;
                --ag-font-family: 'Inter', sans-serif;
                --ag-font-size: 14px;
                --ag-header-font-weight: 600;
                --ag-header-font-size: 13px;
                --ag-header-height: 50px;
                --ag-row-height: 60px;
            }
            
            .ag-theme-alpine .ag-header {
                background: linear-gradient(135deg, #34495e 0%, #2c3e50 100%) !important;
                border-bottom: 2px solid #2c3e50 !important;
            }
            
            .ag-theme-alpine .ag-header-cell-label {
                color: white !important;
                font-weight: 600 !important;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            
            .ag-theme-alpine .ag-header-cell-text {
                color: white !important;
            }
            
            .ag-theme-alpine .ag-cell {
                border-right: 1px solid #e1e8ed;
                padding: 12px 16px;
                display: flex;
                align-items: center;
            }
            
            .ag-theme-alpine .ag-row {
                border-bottom: 1px solid #f1f3f4;
                transition: all 0.2s ease;
            }
            
            .ag-theme-alpine .ag-row:hover {
                background-color: #f8f9fa !important;
                transform: translateY(-1px);
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            
            .ag-theme-alpine .ag-row.unsaved-row {
                background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%) !important;
                border-left: 4px solid #f44336;
            }
            
            .ag-theme-alpine .ag-row.unsaved-row:hover {
                background: linear-gradient(135deg, #ffcdd2 0%, #ef9a9a 100%) !important;
            }
            
            .ag-theme-alpine .ag-paging-panel {
                background: #f8f9fa;
                border-top: 1px solid #e1e8ed;
                padding: 15px;
            }
            
            .ag-theme-alpine .ag-paging-button {
                background: white;
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 8px 12px;
                margin: 0 2px;
                transition: all 0.2s ease;
            }
            
            .ag-theme-alpine .ag-paging-button:hover {
                background: #34495e;
                color: white;
                border-color: #34495e;
            }
            
            .ag-theme-alpine .ag-paging-button[disabled] {
                opacity: 0.5;
                cursor: not-allowed;
            }
            
            /* Loading spinner */
            .dash-loading {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 600px;
                background: white;
                border-radius: 12px;
            }
            
            /* Status indicators */
            .status-approved {
                color: #27ae60;
                font-weight: 600;
            }
            
            .status-pending {
                color: #f39c12;
                font-weight: 600;
            }
            
            .status-rejected {
                color: #e74c3c;
                font-weight: 600;
            }
            
            .saved-status {
                color: #27ae60;
                font-weight: 600;
            }
            
            .unsaved-status {
                color: #e74c3c;
                font-weight: 600;
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
