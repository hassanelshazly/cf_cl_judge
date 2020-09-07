from bs4 import BeautifulSoup as bs
import requests
import getpass
import params
import util
import json
import time
import re

def submit(client):
    url_submit = "{base}/{type}/{id}/submit".format(
        base=params.base, type=params.type_contest, id=params.contest_id)
    # print (url_submit)

    submit_page = client.get(url_submit)
    if submit_page.status_code != 200:
        print ('fail to connect: ', url_submit)
        return False

    csrf_token = util.get_csrf_token(submit_page.content)
    source_file = open(params.source_file_name).read()

    parts = {
        "csrf_token"           : csrf_token,
        "source"               : source_file,
        "contestId"            : params.contest_id,
        "submittedProblemIndex": params.problem_id,
        "ftaa"                 : params.ftaa,
        "bfaa"                 : params.bfaa,
        "_tta"                 : params.tta,
        "programTypeId"        : params.lang,
        "tabSize"              : params.tab_size,
        "sourceFile"           : "",
        "action"               : "submitSolutionFormSubmitted",
    }

    submit_result = client.post(url_submit, data=parts)
    print(submit_result)
    return True