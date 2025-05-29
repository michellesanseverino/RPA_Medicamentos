import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

def enviar_email(destinatario, assunto, corpo):
    """
    Envia um e-mail de lembrete com as informações do medicamento.
    """

    remetente = os.getenv("EMAIL_REMETENTE")
    senha = os.getenv("EMAIL_SENHA")

    msg = MIMEText(corpo)
    msg["Subject"] = assunto
    msg["From"] = remetente
    msg["To"] = destinatario

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(remetente, senha)
            servidor.send_message(msg)
            print(f"✅ E-mail enviado para {destinatario}")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")
