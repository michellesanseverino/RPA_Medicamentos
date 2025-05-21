import schedule
import time
from scripts.lembrete_email import enviar_lembrete

def job():
    enviar_lembrete("michelle@email.com", "Hora de tomar seu medicamento!")

schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
