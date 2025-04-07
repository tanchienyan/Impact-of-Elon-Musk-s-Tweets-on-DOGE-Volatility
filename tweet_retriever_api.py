import requests

url = "https://api.twitter.com/2/users/{id}/tweets"

headers = {"Authorization": "Bearer <token>"}

response = requests.request("GET", url, headers=headers)

print(response.text)