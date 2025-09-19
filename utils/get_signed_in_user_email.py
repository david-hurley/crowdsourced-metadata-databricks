from databricks.sdk import WorkspaceClient

def get_signed_in_user_email():
    """
    Get the current user's information from Databricks.
    
    Args:
        profile (str): The Databricks profile to use for authentication
        
    Returns:
        str: The current user's email/username
    """
    # Initialize the WorkspaceClient
    w = WorkspaceClient()
    
    # Get details about the current user's identity
    current_user_details = w.current_user.me()
    
    # Access the email address
    user_email = current_user_details.user_name
    
    return user_email
