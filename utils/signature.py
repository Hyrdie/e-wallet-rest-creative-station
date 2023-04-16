import hashlib

def get_signature(secret_key, username, api_name):
        signature_string = f'{secret_key}||{username}||{api_name}'
        signature = hashlib.sha256(signature_string.encode('utf-8')).hexdigest()
        return signature