import getpass
import json


class parameters:
    def __init__(self):
        self.base  = "http://codeforces.com"
        self.ftaa = "88arrubrsiq4tutuk7"
        self.bfaa = "bc89c325296ff2581363bb50464f8dbd"
        self.tta  = "543"

        self.user     = ""
        self.password = ""

        self.contest_id   = "4"
        self.problem_id   = "A"
        self.lang         = 54
        self.tab_size     = 4
        self.type_contest = ""
        
        self.source_file_name = ""

    def load_params(self, fpath):
        data = open(fpath).read()
        params = json.loads(data)
        for key, value in params.items():
            try: 
                setattr(self, key, value)
            except:
                pass

    def get_user(self):
        if self.user == "" :
            self.user = input("Handle/Email: ") 
        return self.user

    def get_password(self):
        if self.password == "" :
            self.password = getpass.getpass("Password: ")  
        return self.password

    def get_file(self):
        if self.source_file_name == "":
            self.source_file_name = input("Please Enter file path: ") 
        return self.source_file_name

    def get_contest(self):
        if self.contest_id == "":
            self.contest_id = input("Please Enter contest id: ") 
        return self.contest_id
    
    def get_problem(self):
        if self.problem_id == "":
            self.problem_id = input("Please Enter problem id: ") 
        return self.problem_id
    
    def get_lang(self):
        if self.lang == "":
            self.lang = input("Please Enter language: ") 
        return self.lang

    def set_file(self):
        source_file_name = fname

    def set_contest(self, id):
        contest_id = id
    
    def set_problem(self, id):
        problem_id = id
    
    def set_lang(self, id):
        lang = id
