import sqlite3


connect = sqlite3.connect('pwd_manager/data.db')
cursor = connect.cursor()



def create_db(user_name):
    
    create = f'CREATE TABLE IF NOT EXISTS {user_name}(ID INTEGER PRIMARY KEY AUTOINCREMENT, WEBSITE_NAME TEXT , WEBSITE_USER_NAME BLOB, PASSWORD BLOB)'
    
    cursor.execute(create)
    print(f'Database with username {user_name} created')

def insert_into(user_name, WEBSITE_NAME, WEBSITE_USER_NAME, PASSWORD):
    
    print(WEBSITE_NAME, WEBSITE_USER_NAME, PASSWORD)
    insert = f"INSERT INTO {user_name}(WEBSITE_NAME, WEBSITE_USER_NAME, PASSWORD) VALUES('{WEBSITE_NAME}','{WEBSITE_USER_NAME}','{PASSWORD}')"
    
    cursor.execute(insert)
    cursor.execute('COMMIT')

def search_display_database(user_name):
    
    create_user_table = f'CREATE TABLE IF NOT EXISTS {user_name}(ID INTEGER PRIMARY KEY AUTOINCREMENT, WEBSITE_NAME TEXT , WEBSITE_USER_NAME TEXT, PASSWORD BLOB)'

    cursor.execute(create_user_table)
    
    display = f'SELECT * FROM {user_name}'
    cursor.execute(display)
    show = cursor.fetchall()
    print('-'*50)
    print('(No., Website name, Website user name, Password)')
    for row in show:
        print(row)
    print('\n')
    
def show(user_name, website_name):
    
    user_name = user_name
    website_name = website_name
    
    select = f"SELECT WEBSITE_USER_NAME, PASSWORD FROM {user_name} WHERE WEBSITE_NAME = '{website_name}'"
    print(f'  {website_name}')
    result = cursor.execute(select)
    return result