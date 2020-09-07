from bs4 import BeautifulSoup as bs
from params import *
import requests
import getpass
import json
import time
import re

def get_csrf_token(html):
    soup = bs(html, features="lxml")
    head = soup.head
    meta = head.findChildren("meta")
    csrf_token = [
        m for m in meta if "name" in m.attrs and m["name"] == "X-Csrf-Token"]
    return csrf_token[0]["content"]

def check_login_error(html):
    soup = bs(html, features="lxml")
    error = soup.findAll("span", {"class": "error for__password"})
    if len(error) > 0:
        return error[0].text


cf_enter = "{base}/{login}".format(base=base, login=login_url)

cliente = requests.session()
login_page = cliente.get(cf_enter)
csrf_token = get_csrf_token(login_page.content)

# print (csrf_token)
print(tta)
user = input("Handle/Email: ")
if not len(user):
    user = defind_user

password = getpass.getpass("Password: ")
if not len(password):
    user = defind_password

login_data = {
    "csrf_token"   : csrf_token,
    "action"       : "enter",
    "handleOrEmail": user,
    "password"     : password,
    "remember"     : "on",
    "ftaa"         : ftaa,
    "bfaa"         : bfaa,
    "_tta"         : tta
}

login_result = cliente.post(cf_enter, data=login_data)
# print (login_result.status_code)
if login_result.status_code != 200:
    print ("fail to connect")
else:
    error = check_login_error(login_result.content)
    if error == None:
        print("Successful login")
    else:
        print(error)
