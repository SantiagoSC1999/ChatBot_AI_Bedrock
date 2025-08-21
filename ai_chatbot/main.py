from app.llm.test_connection import test_bedrock_connection
from app.llm.generate_embeddings import get_text_embedding
from app.llm.store_vectors import setup_supabase, store_embedding
from app.utils.logger.logger_util import get_logger

logger = get_logger()

def main():
    # 1. Testear conexión
    if not test_bedrock_connection():
        return
    
    # 2. Configurar Supabase
    collection = setup_supabase()
    
    # 3. ejemplos para vectoriza    
    logger.info(" Enter your question:")
    question = input("Question: ").strip()
    
    if not question:
        logger.warning("No ingresaste una pregunta. Abortando.")
        return

    logger.info(" Enter your answer:")
    answer = input("Answer: ").strip()

    if not answer:
        logger.warning(" No ingresaste una respuesta. Abortando.")
        return
    
    full_text = f"Q:{question}\nA: {answer}"
    logger.info(f"text to vectorize:\n{full_text}")
        
    # for i, question in enumerate(full_text, start = 1):
        # logger.info(f"\nProcesando: '{full_text[:50]}...'")
        
    embedding = get_text_embedding(full_text)
            
        # store_embedding(i, collection, full_text, embedding)
        # logger.info(f"✗ Error almacenando: '{question}'")
        
    if embedding:
        store_embedding(1, collection, full_text, embedding)
        logger.info("Vector almacenado exitosamente.")
    else:
        logger.error("No se pudo generar el embedding.")

if __name__ == "__main__":
    main()