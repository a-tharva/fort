
from pwd_manager.save_retrive  import * 
import hashlib
import json
from cryptography.fernet import Fernet


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
    
    file_name = f'pwd_manager/{user_name}.json'
    with open(file_name, 'a+') as file:
        file.write(json_obj)
    
    create_db(user_name)
    

def search_verify_user(user_name, user_pwd):
    
    
    file_name = f'pwd_manager/{user_name}.json'
    userpwd = hashlib.sha256(user_pwd.encode())
    
    try:
        with open (file_name, 'r') as file:
            json_obj = json.load(file)
            if json_obj["user_pwd"] == userpwd.hexdigest():
                print(f'User {user_name} found and logged in')
                print(""">>
  --insert        #insert into database
  --display       #display whole database
  --show          #show selected password and decrypt it
  --logout        #logout of current acount
                      """)
                while True:
                    
                    inp = input('>>')
                    if inp.lower() == 'insert':
                        print('insert')
                        
                        key = json_obj["key"]
                        key = key + user_pwd
                        
                        WEBSITE_NAME = input('Enter website name:')
                        WEBSITE_USER_NAME = input(f'Enter user name for {WEBSITE_NAME}:')
                        PASSWORD = input(f'Enter password for {WEBSITE_USER_NAME}:')
                        
                        
                        PASSWORD = PASSWORD.encode()
                        
                        # Encrypt
                        obj = Fernet(key)
                        PASSWORD = obj.encrypt(PASSWORD).decode('utf-8')
                        
                        
                        insert_into(user_name, WEBSITE_NAME, WEBSITE_USER_NAME, PASSWORD)

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
                        
                        

                    elif inp.lower() == 'display' or inp.lower() == 'display all':
                        search_display_database(user_name)
                        
                   
                    elif inp.lower() == 'logout':
                        del(user_pwd)
                        print(f'Logged Out of {user_name} account')
                        del(user_name)
                        break
                    
                    
    except FileNotFoundError:
        print(f"No such user {user_name} found")
    
    
    
def verify_password(user_name, userpwd , file_name):
    
    userpwd = hashlib.sha256(userpwd.encode())
    
    with open (file_name, 'r') as file:
            json_obj = json.load(file)
            if json_obj["user_pwd"] == userpwd.hexdigest():
                return True
            else:
                return False


