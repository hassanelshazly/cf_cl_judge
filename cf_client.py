from bs4 import BeautifulSoup as bs
from parameters import parameters
from api import api
import requests
import getpass
import json
import time

class cf_client:
    def __init__(self):
        self.client = requests.session()
        self.params = parmeters()
        self.login_status = False
        self.api = api(self.params)

    def claer(self):
        self.params.set_user("")
        self.params.set_password("")
        self.login_status = False

    ## Helper function to extract csrf tokon from an HTML page
    def get_csrf_token(self, html):
        soup = bs(html, features="lxml")
        head = soup.head
        meta = head.findChildren("meta")
        csrf_token = [
            m for m in meta if "name" in m.attrs and m["name"] == "X-Csrf-Token"]
        return csrf_token[0]["content"]

    ######### Login ##########
    def check_error(self, html, error_type):
        soup = bs(html, features="lxml")
        error = soup.findAll("span", {"class": "error " + error_type})
        if len(error) > 0:
            return error[0].text

    def login(self):
        cf_enter = "{base}/enter".format(base=self.params.base)
        login_page = self.client.get(cf_enter)
        csrf_token = self.get_csrf_token(login_page.content)
        # print (csrf_token)

        login_data = {
            "csrf_token"   : csrf_token,
            "handleOrEmail": self.params.get_user(),
            "password"     : self.params.get_password(),
            "ftaa"         : self.params.ftaa,
            "bfaa"         : self.params.bfaa,
            "_tta"         : self.params.tta,
            "action"       : "enter",
            "remember"     : "on"
        }

        login_result = self.client.post(cf_enter, data=login_data)
        # print (login_result.status_code)
        if login_result.status_code != 200:
            print ("failed to connect", cf_enter)
            return False
        else:
            error = self.check_error(login_result.content, "for__password")
            if error == None:
                print("Successful login")
            else:
                print(error)
                return False
        self.login_status = True
        return True

    ####### Submit #########
    def check_depes(self):
        if ~self.login_status:
            self.login()

    def submit(self):
        url_submit = "{base}/{type}/{id}/submit".format(
            base=self.params.base, type=self.params.type_contest, id=self.params.contest_id)
        # print (url_submit)
        
        self.check_depes()

        submit_page = self.client.get(url_submit)
        if submit_page.status_code != 200:
            print ('fail to connect: ', url_submit)
            return False

        csrf_token = self.get_csrf_token(submit_page.content)
        source_file = open(self.params.get_file()).read()

        submit_data = {
            "csrf_token"           : csrf_token,
            "source"               : source_file,
            "contestId"            : self.params.get_contest(),
            "submittedProblemIndex": self.params.get_problem(),
            "ftaa"                 : self.params.ftaa,
            "bfaa"                 : self.params.bfaa,
            "_tta"                 : self.params.tta,
            "programTypeId"        : self.params.get_lang(),
            "tabSize"              : self.params.tab_size,
            "sourceFile"           : "",
            "action"               : "submitSolutionFormSubmitted",
        }

        submit_result = self.client.post(url_submit, data=submit_data)
        if submit_page.status_code != 200:
            print ('fail to submit')
            return False
        else:
            error = self.check_error(submit_result.content, "for__source")
            if error == None:
                print("Successful Submission")
                self.api.check_last_verdict()
            else:
                print(error)
        return True