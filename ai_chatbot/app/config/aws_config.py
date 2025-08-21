import os
import boto3
from botocore.exceptions import ClientError
from ai_chatbot.app.utils.logger.logger_util import get_logger  # Cambiado a logger_util

logger = get_logger()

class AWSConfig:
    def __init__(self):
        logger.debug("Inicializando AWSConfig")
        self.aws_access_key = os.getenv("AWS_ACCESS_KEY")
        self.aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.region = os.getenv("AWS_REGION", "us-east-1")
        
    def validate(self):
        if not all([self.aws_access_key, self.aws_secret_key]):
            logger.error("Credenciales AWS faltantes")
            raise ValueError("AWS credentials missing in environment variables")
            
    def get_bedrock_client(self):
        self.validate()
        try:
            logger.info("Creando cliente Bedrock")
            return boto3.client(
                service_name='bedrock-runtime',
                aws_access_key_id=self.aws_access_key,
                aws_secret_access_key=self.aws_secret_key,
                region_name=self.region
            )
        except Exception as e:
            logger.error(f"AWS Configuration Error: {str(e)}")
            raise