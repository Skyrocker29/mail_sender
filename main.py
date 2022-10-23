import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import csv

email_sendler = "it1@lizing-p.ru"
password = "r8CeMA@n5DOu"


def send_mail():
    smtp_server = smtplib.SMTP("mail.nic.ru", 587)
    smtp_server.starttls()
    server: SMTP = smtplib.SMTP("mail.nic.ru", 587)  # Создаем объект SMTP
    #server.set_debuglevel(True)  # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
    server.starttls()  # Начинаем шифрованный обмен по TLS
    server.login(email_sendler, password)  # Получаем доступ
    email_getter = str(email)
    msg = MIMEMultipart()
    msg['From'] = email_sendler
    msg['To'] = email_getter
    msg['Subject'] = 'Предложение для компании ' + str(name)
    html = f"""\
        <html>
            <head></head>
            <body>
                <table border="1">
                    <tr>
                        <th>Организация</th>
                        <th>Остатки по банку</th>
                        <th>Остатки по кассе</th>
                    </tr>
                    <tr>
                        {name}
                    </tr>
                </table>
            </body>
        </html>
    """
    msg.attach(MIMEText(html, 'html'))
    server.send_message(msg)  # Отправляем сообщение
    server.quit()


with open("contacts_file.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем первую строчку
    for name, email in reader:
        print("Отправка письма для " + name)
        # Код отправки на почту...
        send_mail()
