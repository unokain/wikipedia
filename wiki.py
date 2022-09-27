#!/usr/bin/python3
import requests
import json

S = requests.Session()
URL = "http://ja.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "則本真樹",
    "rvlimit": "10",
    "rvprop": "timestamp|user|comment|content",
    "rvdir": "older",
    "rvstart": "2022-09-01T00:00:00Z",
    "rvexcludeuser": "SSethi (WMF)",
    "rvslots": "main",
    "formatversion": "2",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]
print("PAGES",PAGES)
for page in PAGES:
    for page_update_history in page["revisions"]:
        print("ユーザー名", page_update_history['user'])
        print("更新時間", page_update_history['timestamp'])
        print("内容",page_update_history['slots']['main']['content'])
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

