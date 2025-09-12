# Database Column Metadata Management Dashboard

A simple one-screen Plotly Dash application for managing database column metadata using AG Grid.

## Features

- **AG Grid Integration**: Professional data grid with sorting, filtering, and pagination
- **Column Metadata Management**: Review and manage database column metadata
- **Column Structure**:
  - Catalog
  - Schema
  - Table
  - Column
  - Comment
  - Glossary Tag
  - Other Tags

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Dash app:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:8050
```

## Features

- **Interactive Grid**: Sort, filter, and search through column metadata records
- **Color-coded Sections**: Different background colors for comments, glossary tags, and other tags
- **Export Functionality**: Export selected data as CSV
- **Responsive Design**: Modern, clean interface
- **Sample Data**: Pre-populated with example column metadata from multiple tables

## Usage

- Use the grid controls to sort and filter data by catalog, schema, table, or column
- View detailed comments and tags for each database column
- Use the "Refresh Data" button to reload the dataset
- Use the "Export Selected" button to export filtered data