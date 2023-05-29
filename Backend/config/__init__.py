import os
from dotenv import load_dotenv
from config.settings import Settings

class Config:
    def __init__(self):
        # Load the settings module and use its values as defaults
        settings = Settings()

        self.debug: bool = os.getenv("DEBUG") or settings.DEBUG
        self.supabase_project_url: str  = settings.SUPABASE_PROJECT_URL
        self.supabase_api_key: str = os.getenv("SUPABASE_API_KEY") or settings.SUPABASE_API_KEY

def load_config():
    load_dotenv()
    return Config()