import requests
import json

base_url = "https://randomuser.me/api/"

try:
    r = requests.get(base_url, timeout = 10)
except requests.exceptions.ConnectionError:
      print("invalid URL")
      exit(1)

if(r.status_code != 200):
    print("invalid query")
    exit(1)

response = r.json()
# print(response)
# print(json.dumps(response, indent=4))

# print(response.get("results")[0], indent = 4)          # error (indent is argument of json.dumps)

data = response.get("results")[0]
# print(json.dumps(data, indent = 4))

name_data = data.get("name")

name = f'{name_data.get("title")}. {name_data.get("first")} {name_data.get("last")}'

print(name)

gender = data.get("gender")
email = data.get("email")
phone = data.get("phone")

print("""
name: {name}
gender: {gender}
email: {email}
phone: {phone}
""".format(
    name=name, gender=gender, email=email, phone=phone
 )
)

