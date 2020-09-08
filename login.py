from bs4 import BeautifulSoup as bs
import requests
import getpass
import params
import util
import json
import time
import re

def check_login_error(html):
    soup = bs(html, features="lxml")
    error = soup.findAll("span", {"class": "error for__password"})
    if len(error) > 0:
        return error[0].text

def login(client):
    cf_enter = "{base}/enter".format(base=params.base)
    login_page = client.get(cf_enter)
    csrf_token = util.get_csrf_token(login_page.content)
    # print (csrf_token)

    login_data = {
        "csrf_token"   : csrf_token,
        "handleOrEmail": params.get_user(),
        "password"     : params.get_passward(),
        "ftaa"         : params.ftaa,
        "bfaa"         : params.bfaa,
        "_tta"         : params.tta,
        "action"       : "enter",
        "remember"     : "on"
    }

    login_result = client.post(cf_enter, data=login_data)
    # print (login_result.status_code)
    if login_result.status_code != 200:
        print ("failed to connect", cf_enter)
        return False
    else:
        error = check_login_error(login_result.content)
        if error == None:
            print("Successful login")
        else:
            print(error)
            return False
    return True

if __name__ == "__main__":
    client = requests.session()
    login(client)
    import submit
    submit.submit(client)
