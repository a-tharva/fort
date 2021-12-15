import hashlib
import json
import getpass
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
def search_verify_user(user_name, user_pwd):
    file_name = f'{PATH}/{user_name}.json'
    userpwd = hashlib.sha256(user_pwd.encode())
    try:
        with open (file_name, 'r') as file:
            json_obj = json.load(file)
            if json_obj["user_pwd"] == userpwd.hexdigest():
                print(f'\nUser {user_name} found and logged in')
                print("""[insert / display / show / logout]
insert into database / display whole database / show selected password and decrypt it / logout of current acount""")
                while True:
                    inp = input('>>')
                    if inp.lower() == 'insert':
                        key = json_obj["key"]
                        key = key + user_pwd
                        WEBSITE_NAME = input('  Enter website name:')
                        WEBSITE_USER_NAME = input(f'  Enter username or mail for {WEBSITE_NAME}:')
                        PASSWORD = getpass.getpass(f'  Enter password for {WEBSITE_USER_NAME}:')
                        PASSWORD = PASSWORD.encode()
                        # Encrypt
                        obj = Fernet(key)
                        PASSWORD = obj.encrypt(PASSWORD).decode('utf-8')
                        insert_into(user_name, WEBSITE_NAME, WEBSITE_USER_NAME, PASSWORD)
                    # For show option    
                    elif inp.lower() == 'show':
                        website_name = input('  Enter Website name :')
                        # Decrypt
                        key = json_obj["key"]
                        key = key + user_pwd
                        obj = Fernet(key)
                        result = show(user_name, website_name)
                        for _ in result:
                            print('\n','     User name:', _[0])
                            pwd = obj.decrypt(_[1].encode()).decode('utf-8')
                            print('      Password:', pwd)
                    # For display option    
                    elif inp.lower() == 'display' or inp.lower() == 'display all':
                        search_display_database(user_name)
                    # For logout option    
                    elif inp.lower() == 'logout':
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
