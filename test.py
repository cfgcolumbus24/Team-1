import requests

url = 'http://127.0.0.1:3000/query'
headers = {'Content-Type': 'application/json'}
data = {'inputs': 'Show me all patients older than 50'}

response = requests.post(url, headers=headers, json=data)

print("Response content:", response.content)

