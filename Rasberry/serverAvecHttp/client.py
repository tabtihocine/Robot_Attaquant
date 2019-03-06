import requests

r = requests.get("http://127.0.0.1:12341")
print(r.status_code)