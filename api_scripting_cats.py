import requests

base_url = "https://catfact.ninja/fact"

try:
    r = requests.get(base_url, timeout = 10)
except requests.exceptions.ConnectionError:
      print("invalid URL")
      exit(1)

print(r.status_code)

if(r.status_code != 200):
    print("invalid query")
    exit(1)

response = r.json()

print("fact: ", response.get("fact"))
print("length: ",response.get("length"))
