import base64
import json
import getpass
import hashlib
from cryptography.fernet import Fernet

from pyfort.secret.secret_sqlite  import * 


# To signup for new user 
def signup(user_name, userpwd):
    user_pwd = hashlib.sha256(userpwd.encode())
    key = Fernet.generate_key()
    userpwd = userpwd.encode()
    data = {
        "user_name" : user_name,
        "user_pwd" : user_pwd.hexdigest(),
        "key": key.decode('utf-8')
    }
    json_obj = json.dumps(data, indent = 3)
    file_name = f'{PATH}/{user_name}.json'
    with open(file_name, 'a+') as file:
        file.write(json_obj)
    create_db(user_name)
    
# Sub menu 
def login(user_name, user_pwd):
    file_name = f'{PATH}/{user_name}.json'
    userpwd = hashlib.sha256(user_pwd.encode())
    try:
        with open (file_name, 'r') as file:
            json_obj = json.load(file)
            if json_obj["user_pwd"] == userpwd.hexdigest():
                print(f'\nUser {user_name} found and logged in')
                print(f'Key for {user_name}: {json_obj["key"]}')
                print("""\n[insert / display / get / logout]
insert into database / display whole database / get selected password and decrypt it / logout of current acount""")
                while True:
                    inp = input('>>').lower()
                    if inp == 'insert':
                        # Combining key with password
                        key = json_obj["key"]
                        key = key[:len(key)-len(user_pwd)] + user_pwd
                        sha256_key = hashlib.sha256(key.encode())
                        sha256_key = sha256_key.hexdigest()
                        sha256_key = bytes(sha256_key[:32],'utf-8')
                        key = base64.urlsafe_b64encode(sha256_key)
                        
                        WEBSITE_NAME = input('  Enter website name:')
                        WEBSITE_USER_NAME = input(f'  Enter username or mail for {WEBSITE_NAME}:')
                        PASSWORD = getpass.getpass(f'  Enter password for {WEBSITE_USER_NAME}:')
                        PASSWORD = PASSWORD.encode()
                        # Encrypt
                        obj = Fernet(key)
                        PASSWORD = obj.encrypt(PASSWORD).decode('utf-8')
                        insert_into(user_name, WEBSITE_NAME, WEBSITE_USER_NAME, PASSWORD)
                    # For show option    
                    elif inp == 'get':
                        website_name = input('  Enter Website name :')
                        # Combining key with password
                        key = json_obj["key"]
                        key = key[:len(key)-len(user_pwd)] + user_pwd
                        sha256_key = hashlib.sha256(key.encode())
                        sha256_key = sha256_key.hexdigest()
                        sha256_key = bytes(sha256_key[:32],'utf-8')
                        key = base64.urlsafe_b64encode(sha256_key)
                        obj = Fernet(key)
                        # Retrive and decrypt
                        result = show(user_name, website_name)
                        for _ in result:
                            print('     User name:', _[0])
                            pwd = obj.decrypt(_[1].encode()).decode('utf-8')
                            print('      Password:', pwd,'\n')
                    # For display option    
                    elif inp == 'display' or inp == 'display all':
                        display_db(user_name)
                    # For logout option    
                    elif inp == 'logout':
                        del(user_pwd)
                        print(f'Logged Out of  user {user_name}\n')
                        del(user_name)
                        break
    except FileNotFoundError:
        print(f"No such user {user_name} found")
    
# Verify user password 
def verify_password(user_name, userpwd , file_name):
    userpwd = hashlib.sha256(userpwd.encode())
    with open (file_name, 'r') as file:
            json_obj = json.load(file)
            if json_obj["user_pwd"] == userpwd.hexdigest():
                return True
            else:
                return False
