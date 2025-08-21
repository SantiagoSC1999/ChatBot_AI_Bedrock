import os
import vecs
from dotenv import load_dotenv
from ai_chatbot.app.utils.logger.logger_util import get_logger

load_dotenv()
logger = get_logger()

class SupabaseConfig:
    def __init__(self):
        self.db_connection = os.getenv("DB_SUPABASE_CONNECTION")
        self.collection_name = os.getenv("SUPABASE_COLLECTION")
        self.embedding_dim = 1024  # Dimensión para Amazon Titan Embed v2
        
    def validate(self):
        """Valida que las configuraciones estén presentes"""
        if not self.db_connection:
            raise ValueError("DB_SUPABASE_CONNECTION no está configurado")
        if not self.collection_name:
            raise ValueError("SUPABASE_COLLECTION no está configurado")
            
    def get_client(self):
        """Retorna un cliente vecs configurado"""
        self.validate()
        try:
            return vecs.create_client(self.db_connection)
        except Exception as e:
            logger.error(f"Error creating Supabase client: {str(e)}")
            raise