import base64
import hashlib


def _key(key, user_pwd):
    # This function creates unique key to 
    # encrypt and decrypt data
    
    key = key[:len(key)-len(user_pwd)] + user_pwd
    sha256_key = hashlib.sha256(key.encode())
    sha256_key = sha256_key.hexdigest()
    sha256_key = bytes(sha256_key[:32],'utf-8')
    key = base64.urlsafe_b64encode(sha256_key)
    
    return key