import requests

response = requests.get(
    "http://localhost:8088/api/v1/database/_info",
    headers={"Authorization": "Bearer " + access_token})
print(response.json())