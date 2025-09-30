#
# * 0
# pip install howdoi

# * 1
import requests

r = requests.get("https://requests.readthedocs.io")
r.status_code
print(r.headers)
