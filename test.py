import requests

url = "http://127.0.0.1:5000/books"

payload = {}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNDk0ODA0NSwianRpIjoiMzM4MDRkZGEtZTc4Yy00ZDZlLWI1ZWYtN2JkMzExOTViNDE5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXIiLCJuYmYiOjE3MDQ5NDgwNDUsImNzcmYiOiJiMTU4YTQ3Yy00MDNjLTQ5ZGEtOTY3Yy0zMmVlOWRkMTgwMzQiLCJleHAiOjE3MDQ5NDg5NDV9.wvIUuq2_WsnRiKVK27gsPDv7-_OgYPYmVv6fzInjfvs'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
