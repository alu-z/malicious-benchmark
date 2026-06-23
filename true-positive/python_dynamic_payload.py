import base64


def run_payload(encoded_payload):
    decoded = base64.b64decode(encoded_payload)
    exec(decoded)

