from win10toast import ToastNotifier
from requests import get
import random, time, webbrowser
toaster = ToastNotifier()
headers = {
    "User-Agent": "Windows:haxors.hanz.pornfree.pozt:v0.1.0 (by /u/HanzHaxors)"
}
posts = list()

def alert(title, description, url, duration=5, threaded=True):
    arg = [title, description]
    kwarg = {
        "duration": duration,
        "threaded": threaded,
        "callback_on_click": lambda: open(url)
        }
    toaster.show_toast(*arg, **kwarg)

def wait(s=1):
    time.sleep(s)
    return True

def open(url):
    webbrowser.open(url)

def fetch():
    try:
        posts_ = get("https://api.reddit.com/r/pornfree/new?limit=10", headers=headers)
        posts.extend(posts_.json()["data"]["children"])
    except Exception as e:
        print(e)
        exit()

fetch()
post = random.choice(posts)["data"]
alert(post["title"], post["selftext"], post["url"])

while wait(300):
    fetch()
    post = random.choice(posts)["data"]
    alert(post["title"], post["selftext"], post["url"])
