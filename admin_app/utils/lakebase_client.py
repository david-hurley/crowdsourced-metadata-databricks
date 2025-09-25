import psycopg2
import pandas as pd
from databricks.sdk import WorkspaceClient
import uuid

class LakebaseClient:
    def __init__(self):
        """
        Initialize and open a connection to the Lakebase Postgres instance.
        """
        # Hardcoded connection details
        self.instance_name = "fe-allstars-crowdsourced-metadata"
        self.dbname = "public"

        # Get credentials from Databricks workspace
        w = WorkspaceClient()
        self.user = w.current_user.me()
        instance = w.database.get_database_instance(name=self.instance_name)
        cred = w.database.generate_database_credential(
            request_id=str(uuid.uuid4()),
            instance_names=[self.instance_name]
        )

        # Open persistent connection
        self.conn = psycopg2.connect(
            host=instance.read_write_dns,
            dbname=self.dbname,
            user=self.user,
            password=cred.token,
            sslmode="require"
        )

    def query(self, sql: str) -> pd.DataFrame:
        """
        Execute a SQL query and return results as a DataFrame.
        """
        with self.conn.cursor() as cur:
            cur.execute(sql)
            cols = [d.name for d in cur.description]
            rows = cur.fetchall()
            return pd.DataFrame(rows, columns=cols)
    
    def execute(self, sql: str, params: tuple = None):
        """
        Execute a SQL statement that modifies the database (INSERT, UPDATE, DELETE, CREATE, etc.).
        """
        with self.conn.cursor() as cur:
            if params:
                cur.execute(sql, params)
            else:
                cur.execute(sql)
            self.conn.commit()

    def close(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()
            self.conn = None
