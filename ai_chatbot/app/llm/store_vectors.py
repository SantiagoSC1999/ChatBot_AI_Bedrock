import vecs
import os
import uuid
from dotenv import load_dotenv
from app.utils.logger.logger_util import get_logger

logger = get_logger()

load_dotenv()

def setup_supabase():
    print('entrando a configuración de supabase')
    DB_CONNECTION = os.getenv('DB_SUPABASE_CONNECTION')
    COLLECTION_NAME = os.getenv('SUPABASE_COLLECTION')
    
        # Crear cliente
    try:
        vx = vecs.create_client(DB_CONNECTION)
        collection = vx.get_or_create_collection(name=COLLECTION_NAME, dimension=1024)
        logger.info(f" Colección '{COLLECTION_NAME}' obtenida")
        return collection
    except Exception as e:
        logger.error(f" Error con Supabase: {str(e)}")
           # return None

def store_embedding(collection, text: str, embedding: list):
    try:   
        new_id = str(uuid.uuid4())     
        collection.upsert(
            records=[(new_id, embedding, {"text": text})]
        )
        print(f"✓ Vector almacenado para: '{text}...'")
    except Exception as e:
        print(f"Error almacenando vector: {str(e)}")

