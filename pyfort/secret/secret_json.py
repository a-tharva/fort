import json
import getpass
import hashlib
from cryptography.fernet import Fernet

from ..utils.utils import _help, PATH
from .secret_sqlite  import handle
from ..data.secret_key import _key


class user:
    """Class for user functions"""
    
    
    def signup(user_name, userpwd):
        # To signup for new user 
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
        handle.create_db(user_name)


    def login(user_name, user_pwd):
        # User menu 
        file_name = f'{PATH}/{user_name}.json'
        userpwd = hashlib.sha256(user_pwd.encode())
        try:
            with open (file_name, 'r') as file:
                json_obj = json.load(file)
                if json_obj["user_pwd"] == userpwd.hexdigest():
                    print(f'\nUser {user_name} found and logged in')
                    print(f'Key for {user_name}: {json_obj["key"]}')
                    
                    key = json_obj["key"]
                    key = _key(key, user_pwd)
                    
                    while True:
                        print('\n[display / get / help / insert / logout / remove / replace]')
                        inp = input('>>').lower()
                        if inp == 'display' or inp == 'display all':
                            # Print whole table, format the table in sql table print format
                            # sqlite api have issue so table format print is done with normal
                            # python print
                            handle.display_db(user_name)

                        elif inp == 'get':
                            # Print data with decrypted password  
                            website_name = input('  Enter Website name :')
                            obj = Fernet(key)
                            # Retrive and decrypt
                            result = handle.show(user_name, website_name)
                            for _ in result:
                                print('     User name:', _[0])
                                pwd = obj.decrypt(_[1].encode()).decode('utf-8')
                                print('      Password:', pwd,'\n')

                        elif inp == 'help':
                            # Help function from utils, print contents from _help() function
                            _help()


                        elif inp == 'insert':
                            # Insert into table with Password encryption
                            # Combining key with password
                            WEBSITE_NAME = input('  Enter website name:')
                            WEBSITE_USER_NAME = input(f'  Enter username or mail for {WEBSITE_NAME}:')
                            PASSWORD = getpass.getpass(f'  Enter password for {WEBSITE_USER_NAME}:')
                            PASSWORD = PASSWORD.encode()
                            # Encrypt
                            obj = Fernet(key)
                            PASSWORD = obj.encrypt(PASSWORD).decode('utf-8')
                            handle.insert_into(user_name, WEBSITE_NAME, WEBSITE_USER_NAME, PASSWORD)

                        elif inp == 'logout':
                            # Logout of current user and return to main menu 
                            # user name and password is deleted 
                            # user key and fernet key is deleted 
                            del(user_pwd)
                            print(f'Logged Out of  user {user_name}\n')
                            del(user_name)
                            del(key)
                            del(obj)
                            break

                        # Remove
                        elif inp == 'remove':
                            print('  Entire row including username and password for the site will be deleted')
                            id_no = input('  Enter row number to delete:')
                            try:
                                handle.delete_entry(user_name, id_no)
                                print(f'  Row {id_no} removed from database')
                            except Exception as error:
                                print(error)

                        # Replace selected column and id with provided one
                        elif inp == 'replace':
    #                        replace_opt = input('  Select ')
    #                        def replace_element(user_name, to_update, value, id_no)
                            print('Function yet to be implemented')

        except FileNotFoundError:
            print(f"No such user {user_name} found")


    def verify_password(user_name, userpwd , file_name):
        # Verify user password 
        userpwd = hashlib.sha256(userpwd.encode())
        with open (file_name, 'r') as file:
                json_obj = json.load(file)
                if json_obj["user_pwd"] == userpwd.hexdigest():
                    return True
                else:
                    return False
