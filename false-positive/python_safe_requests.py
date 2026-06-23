import requests


def send_healthcheck():
    return requests.post("https://api.example.invalid/health", json={"status": "ok"})

