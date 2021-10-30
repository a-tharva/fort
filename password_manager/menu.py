import os
from colorama import init
from termcolor import colored, cprint

from create_or_check_user_json import * 

# use Colorama to make Termcolor work on Windows too
init()


# Main menu
def show_menu():
    print("""
--Login  #Already created account
--Signup #Create new account
--Erase  #Delete account!!!\n""")
    while True:    
        choice = input('>')
        # To login into account
        if choice.lower() == 'login':
            user_name = input('Enter user name:')
            user_pwd = input(f'Enter password for {user_name}:')
            search_verify_user(user_name, user_pwd)
            del(user_pwd)
            del(user_name)
                
        # To signup for new user    
        elif choice.lower() == 'signup':
            try:
                print('>Creating new user')
                user_name = input(' Enter user name:')
                loc = f'data/{user_name}.json'
                # Check if user name is available
                if os.path.exists(loc):
                    print(' User already exist')
                    print(' Try another name')
                else:
                    userpwd = input(f' Enter password for {user_name}:')
                    signup(user_name, userpwd)
                    print(colored('Account created', 'green'))

            except Exception as Error:
                print(colored('>Something went wrong','red'))
                print(Error)
                
        # To delete all user related files and data
        elif choice.lower() == 'erase':
            flag = False
            user_name = input('Enter user name:')
            userpwd = input(f'Enter password for {user_name}:')
            loc = f'data/{user_name}.json'
            # Check if user exist
            if os.path.exists(loc):
                print(f'>File {user_name}.json exist')
                print('>Verifying password')
                flag = verify_password(user_name, userpwd, loc)
                if flag:
                    print('!!password verified')
                    confirm = input('>>Confirm want to delete account [y/n]:')
                    confirm1 = input('>>Sure want to delete account [y/n]:')
                    confirm2 = input('>>For real want to delete account [y/n]:')
                    if confirm == 'y' and confirm1 == 'y' and confirm2 == 'y':
                        #os.remove("demofile.txt")
                        pass    
                else:
                    print('!!password incorrect')
            else:
                print('No such file found')
                            