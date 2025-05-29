import os
import boto3
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

def upload_para_s3(arquivo_local, bucket, nome_arquivo_s3):
    """
    Faz upload de um arquivo local para um bucket S3.

    :param arquivo_local: caminho do arquivo JSON local
    :param bucket: nome do bucket no S3
    :param nome_arquivo_s3: nome desejado no bucket
    """
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )

    try:
        s3.upload_file(arquivo_local, bucket, nome_arquivo_s3)
        print(f"✅ Upload concluído: {nome_arquivo_s3}")
    except Exception as e:
        print(f"❌ Falha no upload: {e}")
