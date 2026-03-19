import requests

SERVICE_URL = "http://127.0.0.1:8001/api/v1/users"

def forward_user_to_service(user_data: dict):
    response = requests.post(SERVICE_URL, json=user_data)
    return response.json()