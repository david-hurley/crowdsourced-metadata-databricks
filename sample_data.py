# Sample data for the metadata management app

sample_data = [
    {
        "catalog": "main",
        "schema": "public",
        "table": "users",
        "column": "user_id",
        "comment": "Unique identifier for each user",
        "glossary tag": "#user,#identifier,#primary_key",
        "other tags": "pii,unique,auto_increment"
    },
    {
        "catalog": "main",
        "schema": "public",
        "table": "users",
        "column": "email",
        "comment": "User email address for authentication",
        "glossary tag": "#user,#authentication,#contact",
        "other tags": "pii,email,required"
    },
    {
        "catalog": "main",
        "schema": "public",
        "table": "users",
        "column": "created_at",
        "comment": "Timestamp when user account was created",
        "glossary tag": "#audit,#timestamp,#creation",
        "other tags": "system,readonly,datetime"
    },
    {
        "catalog": "main",
        "schema": "analytics",
        "table": "user_activity",
        "column": "activity_id",
        "comment": "Unique identifier for each activity record",
        "glossary tag": "#activity,#identifier,#primary_key",
        "other tags": "analytics,unique,auto_increment"
    },
    {
        "catalog": "main",
        "schema": "analytics",
        "table": "user_activity",
        "column": "user_id",
        "comment": "Foreign key reference to users table",
        "glossary tag": "#activity,#user,#foreign_key",
        "other tags": "reference,analytics,required"
    },
    {
        "catalog": "main",
        "schema": "analytics",
        "table": "user_activity",
        "column": "action_type",
        "comment": "Type of user action performed",
        "glossary tag": "#activity,#action,#classification",
        "other tags": "enum,analytics,behavior"
    },
    {
        "catalog": "main",
        "schema": "commerce",
        "table": "orders",
        "column": "order_id",
        "comment": "Unique identifier for each order",
        "glossary tag": "#order,#identifier,#primary_key",
        "other tags": "commerce,unique,auto_increment"
    },
    {
        "catalog": "main",
        "schema": "commerce",
        "table": "orders",
        "column": "total_amount",
        "comment": "Total monetary value of the order",
        "glossary tag": "#order,#amount,#financial",
        "other tags": "commerce,money,calculated"
    },
    {
        "catalog": "main",
        "schema": "commerce",
        "table": "orders",
        "column": "status",
        "comment": "Current status of the order",
        "glossary tag": "#order,#status,#workflow",
        "other tags": "enum,commerce,state"
    },
    {
        "catalog": "main",
        "schema": "commerce",
        "table": "products",
        "column": "product_id",
        "comment": "Unique identifier for each product",
        "glossary tag": "#product,#identifier,#primary_key",
        "other tags": "commerce,unique,auto_increment"
    },
    {
        "catalog": "main",
        "schema": "commerce",
        "table": "products",
        "column": "name",
        "comment": "Display name of the product",
        "glossary tag": "#product,#name,#display",
        "other tags": "commerce,text,required"
    },
    {
        "catalog": "main",
        "schema": "commerce",
        "table": "products",
        "column": "price",
        "comment": "Current selling price of the product",
        "glossary tag": "#product,#price,#financial",
        "other tags": "commerce,money,decimal"
    }
]
