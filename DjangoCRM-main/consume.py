import requests

response = requests.get('http://localhost:8000/profiles')
print(response.json())