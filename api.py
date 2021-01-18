from parameters import parameters
import requests
import json
import time

class api:
    def __init__(self, params = parameters()):
        self.params = params

    def api_method(self, method, data):
        url = "{base}/api/{method}".format(
                    base=self.params.base, method=method)

        data = requests.get(url, params=data)
        js = json.loads(data.content)
        
        if js.get("status") != "OK":
            print ("failed to retrieve", method)
            print (js.get("comment"))
        
        return js.get("result")

    def get_submissions(self, start, count):
        submission_method = "user.status"
        submission_data = {
            "handle" : self.params.get_user(),
            "from"   : start,
            "count"  : count
        }
        
        return self.api_method(submission_method, submission_data)

    def get_user_info(self):
        user_info_method = "user.info"
        user_info_data = {
            "handles" : self.params.get_user(),
        }
        return self.api_method(user_info_method, user_info_data)[0]


    def check_verdict(submission):
        if submission.get("verdict") == None:
            print("COMPILING")
        else:
            print("VERDIT" , "\t\t", submission["verdict"])
            print("PASSED TESTS", "\t", submission.get("passedTestCount"))
            print("TIME", "\t\t", submission.get("timeConsumedMillis"))

    def check_last_verdict(self):
        while True:
            try:
                result = self.get_submissions(1, 1)[0]
            except:
                print("NO SUBMISSIONS FOUND")
                break

            if result.get("verdict") == None:
                print("COMPILING")
            elif result.get("verdict") == "TESTING":
                print("RUNNING ON TEST:", int(result.get("passedTestCount")) + 1 )
            else:
                check_verdict(result)
                break

            time.sleep(1.5)