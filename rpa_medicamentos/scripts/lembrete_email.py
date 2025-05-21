import smtplib
from email.mime.text import MIMEText

def enviar_lembrete(destinatario, mensagem):
    msg = MIMEText(mensagem)
    msg['Subject'] = 'Lembrete de Medicamento'
    msg['From'] = 'seuemail@gmail.com'
    msg['To'] = destinatario

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('seuemail@gmail.com', 'sua_senha')
        smtp.send_message(msg)