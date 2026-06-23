import subprocess
from flask import request


def ping_endpoint():
    host = request.args.get("host")
    return subprocess.check_output("ping -c 1 " + host, shell=True)

