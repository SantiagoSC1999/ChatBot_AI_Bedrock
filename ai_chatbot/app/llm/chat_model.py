import boto3
import os
import json
from app.utils.prompt.prompt_prms_support import DEFAULT_CHATBOT_PRMS_SUPPORT
from dotenv import load_dotenv

load_dotenv()

bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

def chat_with_model(prompt = DEFAULT_CHATBOT_PRMS_SUPPORT, temperature=0.7):
    body = json.dumps({
        "prompt": prompt,
        "maxTokens": 512,
        "temperature": temperature,
    })
    response = bedrock_client.invoke_model(
        body=body,
        modelId="anthropic.claude-3-7-sonnet-20250219-v1:0",
        # modelId="deepseek.r1-v1:0",
        accept="application/json",
        contentType="application/json"
    )
    response_body = json.loads(response["body"].read())
    return response_body["completion"]