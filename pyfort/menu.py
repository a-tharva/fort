import os
import getpass

from colorama import init
from termcolor import colored, cprint

from .utils.utils import PATH
from .secret.secret_json import user 
from .secret.secret_sqlite import handle


# use Colorama to make Termcolor work on Windows too
init()


def show_menu():
    # Main menu
    while True: 
        print('\n[Login / Signup / Erase / Ctrl+C] \nLogin:Already created account / Signup:Create new account / Erase:Delete account!!!')
        choice = input('>')
        
        
        if choice.lower() == 'login':
            # To login into account
            user_name = input(' Enter user name:')
            user_pwd = getpass.getpass(f' Enter password for {user_name}:')
            user.login(user_name, user_pwd)
            del(user_pwd)
            del(user_name)
                
          
        elif choice.lower() == 'signup':
            # To signup for new user  
            try:
                print('>Creating new user')
                user_name = input(' Enter user name:')
                loc = f'{PATH}/{user_name}.json'
                
                if os.path.exists(loc):
                    # Check if user name is available
                    print(' User already exist')
                    print(' Try another name')
                else:
                    userpwd = getpass.getpass(f' Enter password for {user_name}:')
                    user.signup(user_name, userpwd)
                    print(colored('Account created', 'green'))
                    print(colored('Database created', 'green'))
            except Exception as Error:
                print(colored('>Something went wrong','red'))
                print(Error)
                
        
        elif choice.lower() == 'erase':
            # To delete all user related files and data
            flag = False
            user_name = input('Enter user name:')
            userpwd = input(f'Enter password for {user_name}:')
            loc = f'{PATH}/{user_name}.json'
            
            if os.path.exists(loc):
                # Check if user exist
                print(f'>File {user_name}.json exist')
                print('>Verifying password')
                flag = user.verify_password(user_name, userpwd, loc)
                if flag:
                    print('!!password verified')
                    confirm = input('>>Confirm want to delete account [Y/n]:')
                    confirm1 = input('  >>Sure want to delete data [Y/n]:')
                    if confirm == 'Y' and confirm1 == 'Y':
                        handle.delete_table(user_name)
                        os.remove(loc)
                        print('!!User file and data deleted!!')
                else:
                    print('!!password incorrect')
            else:
                print('No such file found')
                            