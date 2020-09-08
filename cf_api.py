import requests
import params
import util
import json
import time

def api_method(method, data):
    url = "{base}/api/{method}".format(
                base=params.base, method=method)

    data = requests.get(url, params=data)
    js = json.loads(data.content)
    
    if js.get("status") != "OK":
        print ("failed to retrieve", method)
        print (js.get("comment"))
    return js.get("result")

def get_submissions(start, count):
    submission_method = "user.status"
    submission_data = {
        "handle" : params.get_user(),
        "from"   : start,
        "count"  : count
    }
    return api_method(submission_method, submission_data)


def check_verdict(submission):
    if submission.get("verdict") == None:
        print("COMPILING")
    else:
        print("VERDIT       ", results["verdict"])
        print("PASSED TESTS ", results.get("passedTestCount"))
        print("TIME         ", results.get("timeConsumedMillis"))

def check_last_verdict():
    while True:
        try:
            results = get_submissions(1, 1)[0]
        except:
            print("NO SUBMISSIONS FOUND")
            break

        if results.get("verdict") == None:
            print("COMPILING")
        elif results.get("verdict") == "TESTING":
            print("RUNNING ON TEST:", int(results.get("passedTestCount")) + 1 )
        else:
            print("VERDIT" , "\t\t", results["verdict"])
            print("PASSED TESTS", "\t", results.get("passedTestCount"))
            print("TIME", "\t\t", results.get("timeConsumedMillis"))
            break
        time.sleep(1.5)

def get_user_info():
    user_info_method = "user.info"
    user_info_data = {
        "handles" : params.get_user(),
    }
    return api_method(user_info_method, user_info_data)[0]

if __name__ == "__main__":
    user_info = get_user_info()
    print(user_info.get("handle"), "\t",
          user_info.get("rank"), "\t", 
          user_info.get("rating"))
    check_last_verdict()
    # print(get_user_info())

