import re
import smtplib
from email.mime.text import MIMEText
from telethon import TelegramClient
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Парсинг ссылки
def parse_link(link):
    username = re.search(r't\.me/([^/]+)', link).group(1)
    return username

# Отправка email-жалобы
def send_email_report(username):
    msg = MIMEText(f"Аккаунт @{username} рассылает детскую порнографию (экстренная жалоба)")
    msg['Subject'] = f"URGENT: Violation report @{username}"
    msg['From'] = config['EMAIL']['address']
    msg['To'] = 'abuse@telegram.org'

    with smtplib.SMTP(config['EMAIL']['smtp_server'], config['EMAIL']['smtp_port']) as server:
        server.starttls()
        server.login(config['EMAIL']['address'], config['EMAIL']['password'])
        server.send_message(msg)

# Главная функция
async def main(link):
    username = parse_link(link)
    
    # 1. Email-жалобы
    for _ in range(5):
        send_email_report(username)

if name == "__main__":
    import asyncio
    link = input("Введите ссылку на нарушение: ")
    asyncio.run(main(link))
