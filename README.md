# Crowdsourced Metadata Management Dashboard

A Plotly Dash application for managing entity metadata and glossary tags in Databricks using AG Grid. This application allows users to review, edit, and manage database column metadata with an integrated glossary tagging system.

## Features

- **AG Grid Integration**: Professional data grid with sorting, filtering, and pagination
- **Entity Metadata Management**: Review and manage database entity metadata
- **Glossary Tagging**: Interactive dropdown system for applying glossary tags
- **Review Workflow**: Track approval status and review comments
- **Real-time Updates**: Live data synchronization with PostgreSQL database
- **Column Structure**:
  - Entity Type
  - Entity Path
  - Current Comment
  - Proposed Comment
  - Glossary Tag
  - Review Status
  - Review Comment
  - Sent for Review

## Prerequisites

- Python 3.8+
- Databricks workspace access
- PostgreSQL database (Lakebase) access
- Databricks CLI (for asset bundle deployment)

## Local Development Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd crowdsourced-metadata-databricks
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Create a `.env` file in the project root with your Databricks credentials:
```bash
# Databricks Configuration
DATABRICKS_HOST=https://your-workspace.cloud.databricks.com
DATABRICKS_TOKEN=your-personal-access-token

# Database Configuration (if needed for local testing)
DB_HOST=your-db-host
DB_PORT=5432
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
```

### 5. Run Locally
```bash
python app.py
```

The application will be available at: `http://localhost:8050`

## Databricks Asset Bundle Deployment

### 1. Install Databricks CLI
```bash
pip install databricks-cli
```

### 2. Configure Databricks CLI
```bash
databricks configure --token
```

### 3. Deploy the Asset Bundle
```bash
# Deploy to development workspace
databricks bundle deploy

# Deploy to production workspace
databricks bundle deploy --target production
```

### 4. Access the Application
After deployment, the application will be available as a Databricks Asset Bundle job. You can:
- View it in the Databricks workspace under "Workflows"
- Access the web interface through the job's URL
- Monitor logs and performance in the Databricks UI

## Configuration

### Database Queries
The application uses several SQL queries defined in `app.py`:

- **ENTITIES_QUERY**: Fetches entity metadata with approval status
- **GLOSSARY_QUERY**: Retrieves available glossary tags
- **SAVE_QUERY**: Saves user changes to the database

### Customization
- **Styling**: Modify `app_css.py` for custom themes
- **Layout**: Update `app_layout.py` for UI changes
- **Database**: Adjust queries in `app.py` for different data sources

## File Structure

```
crowdsourced-metadata-databricks/
├── app.py                 # Main Dash application
├── app_layout.py          # UI layout and column definitions
├── app_css.py            # Custom CSS styling
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── databricks.yml        # Asset bundle configuration
├── utils/
│   ├── lakebase_client.py           # Database connection
│   └── get_signed_in_user_email.py  # User authentication
└── README.md             # This file
```

## Troubleshooting

### Local Development Issues
- **Database Connection**: Ensure PostgreSQL credentials are correct
- **Databricks SDK**: Verify your workspace URL and token
- **Dependencies**: Make sure all packages are installed correctly

### Asset Bundle Issues
- **Authentication**: Check Databricks CLI configuration
- **Permissions**: Ensure you have workspace admin rights
- **Resources**: Verify job resources are sufficient

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review Databricks Asset Bundle documentation
3. Contact the development team


GRANT CONNECT ON DATABASE public TO "a442985c-3625-4022-a8a9-0f75fc1c650d";
GRANT USAGE, CREATE ON SCHEMA david_hurley TO "a442985c-3625-4022-a8a9-0f75fc1c650d";
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE "public"."david_hurley"."governed_entity_paths_and_comments_pg" TO "a442985c-3625-4022-a8a9-0f75fc1c650d";