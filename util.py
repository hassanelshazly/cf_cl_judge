from bs4 import BeautifulSoup as bs

def get_csrf_token(html):
    soup = bs(html, features="lxml")
    head = soup.head
    meta = head.findChildren("meta")
    csrf_token = [
        m for m in meta if "name" in m.attrs and m["name"] == "X-Csrf-Token"]
    return csrf_token[0]["content"]