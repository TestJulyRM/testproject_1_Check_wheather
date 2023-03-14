import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class wheather:
    """Класс для определения погоды"""
    wheather_today = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&aqs=chrome..69i57j0i512l2j0i131i433i512j0i131i433l6.4818j1j7&sourceid=chrome&ie=UTF-8'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    'current_wheather = 0'

    def __init__(self):
        pass

    def check_wheather(self):
        """Функция определения погоды"""
        full_page = requests.get(self.wheather_today, headers=self.headers)
        'print(full_page.content)'
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "wob_t q8U8x"})
        return convert[0].text
    def print_wheather(self):
        """Функция вывода определения погоды"""
        wheather = self.check_wheather()
        null = str(0)

        if wheather > null:
            print('Сейчас на улице', wheather,  'C°, теплая погода')
            text = ('Сейчас на улице ' + wheather + ' C°, теплая погода')
            print(text)
            self.send_mail(text)

        elif wheather < null:
            print('Сейчас на улице', wheather, 'C°, холодная погода')
            text = ('Сейчас на улице ' + wheather + ' C°, холодная погода')
            print(text)
            self.send_mail(text)
        else:
            print('Сейчас на улице', wheather, 'C°, нулевая погода')
            text = ('Сейчас на улице ' + wheather + ' C°, нулевая погода. Лучше Вам сегодня сидеть дома и ни куда не идти. \n Если вы получили данное письмо, просим прислать подтверждение о получинии информации о погоде')
            print(text)
            self.send_mail(text)

    def send_mail(self, text):
        """Функция отправки информации о погоде на email"""
        msg = MIMEMultipart()
        msg['From'] = 'test.july2023@yandex.ru'
        msg['To'] = 'r.july@tpm13.ru'
        msg['Subject'] = 'Погода'
        msg.attach(MIMEText(text, 'plain'))

        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        server.ehlo('test.july2023@yandex.ru')
        server.login('test.july2023@yandex.ru', 'testruiner')
        server.auth_plain()
        server.send_message(msg)
        server.quit()


wheather1 = wheather()
wheather1.print_wheather()
