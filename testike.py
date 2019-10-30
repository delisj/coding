import requests

url = "https://api.chucknorris.io/jokes/random"

r = requests.get(url)

data = r.json()

# print("id", data["id"])
# print("icon_url", data["icon_url"])

print(data['value'])
print(data['value'])