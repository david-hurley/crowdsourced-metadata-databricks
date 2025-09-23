# Crowdsourced Metadata Management Dashboard

Two Plotly Dash apps for managing entity metadata and glossary tags in Databricks using AG Grid.

- `user_app`: User-facing app for reviewing and editing metadata  
- `admin_app`: Admin-facing app for managing reviews  

Both apps require **Python 3.11**, **Databricks CLI authentication**, and **PostgreSQL (Lakebase) access**.

---

## Prerequisites

- Python 3.11  
- [UV](https://docs.astral.sh/uv/) package manager (recommended)  
- Databricks CLI configured with your workspace token (confirm with `databricks auth profiles`) - must point to `e2-demo-field-eng` workspace, where Lakebase lives

## Run User App Locally
1. Change directory to `user_app` 
2. Create and activate a `venv` in `user_app` and install requirements.txt with `pip install -r requirements.txt`
3. Run the app with `python app.py`
4. You can see changes written in `e2-demo-field-eng` to the Lakebase instance

## Run Admin App Locally
1. Change directory to `admin_app` 
2. Create and activate a `venv` in `admin_app` and install requirements.txt with `pip install -r requirements.txt`
3. Run the app with `python app.py`
4. You can see changes written in `e2-demo-field-eng` to the Lakebase instance