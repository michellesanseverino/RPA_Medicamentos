import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY")
)

BUCKET = "meu-controle-medicamentos"

def upload_receita(arquivo_local, nome_s3):
    s3.upload_file(arquivo_local, BUCKET, nome_s3)
    return f"s3://{BUCKET}/{nome_s3}"