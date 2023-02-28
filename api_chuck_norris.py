import os
import requests

os.system("cls")

api = 'https://api.chucknorris.io/jokes/random'

response = requests.get(api)
response = response.json()

print(response['value'])