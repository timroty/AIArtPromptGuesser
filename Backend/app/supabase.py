from supabase import create_client, Client
from config import load_config

class Supabase:
    def __init__(self):
        # Configs
        config = load_config()

        # Set up your Supabase credentials
        supabase_url: str = config.supabase_project_url
        supabase_key: str = config.supabase_api_key

        # Create the Supabase client instance
        self.client: Client = create_client(supabase_url, supabase_key)
        



