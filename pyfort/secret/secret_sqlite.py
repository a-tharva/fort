import sqlite3
from ..utils.utils import PATH


# Connect to database data.db
connect = sqlite3.connect(f'{PATH}/data.db')
cursor = connect.cursor()

class handle:
    """Class to handle sqlite database functions"""

    def create_db(user_name):
        # Create new database
        create = f'CREATE TABLE IF NOT EXISTS {user_name}(ID INTEGER PRIMARY KEY AUTOINCREMENT, WEBSITE_NAME TEXT , WEBSITE_USER_NAME BLOB, PASSWORD BLOB)'
        cursor.execute(create)


    def insert_into(user_name, WEBSITE_NAME, WEBSITE_USER_NAME, PASSWORD):
        # Insert new row in database
        insert = f"INSERT INTO {user_name}(WEBSITE_NAME, WEBSITE_USER_NAME, PASSWORD) VALUES('{WEBSITE_NAME}','{WEBSITE_USER_NAME}','{PASSWORD}')"
        cursor.execute(insert)
        cursor.execute('COMMIT')


    def replace_element(user_name, to_update, value, id_no):
        # Replace element in table
        replace = f"UPDATE {user_name} SET {to_update} = {value} WHERE ID = {id_no}"
        try:
            cursor.execute(replace)
            print(f'  {to_update} updated')
            cursor.execute('COMMIT')
        except Exception as error:
            print(error)


    def show(user_name, website_name):
        # Print selected row
        user_name = user_name
        website_name = website_name
        select = f"SELECT WEBSITE_USER_NAME, PASSWORD FROM {user_name} WHERE WEBSITE_NAME = '{website_name}'"
        print(f'  {website_name}')
        result = cursor.execute(select)
        return result


    def display_db(user_name):
        # Print whole database
        create_user_table = f'CREATE TABLE IF NOT EXISTS {user_name}(ID INTEGER PRIMARY KEY AUTOINCREMENT, WEBSITE_NAME TEXT , WEBSITE_USER_NAME BLOB, PASSWORD BLOB)'
        cursor.execute(create_user_table)
        display = f'SELECT * FROM {user_name}'
        cursor.execute(display)
        show = cursor.fetchall()

        # For printing in table format 
        print('+---+'+'-'*15+'+'+'-'*30+'+'+'-'*100+'+')
        print('|No.|Website name   |Website user name{0[0]:13s}|Password{0[0]:92s}|'.format(['']))
        print('+---+'+'-'*15+'+'+'-'*30+'+'+'-'*100+'+')
        for row in show:
            print('|{0[0]:3d}|{0[1]:15s}|{0[2]:30s}|{0[3]:50s}'.format(row))
        print('+---+'+'-'*15+'+'+'-'*30+'+'+'-'*100+'+')

        
    @staticmethod
    def delete_table(user_name):
        # Delete table
        delete_table = f'DROP TABLE {user_name}'
        try:
            cursor.execute(delete_table)
            cursor.execute('COMMIT')
        except sqlite3.OperationalError:
            pass

    
    def delete_entry(user_name, id_no):
        # Delete row
        delete_entry = f'DELETE FROM {user_name} WHERE ID = {id_no}'
        cursor.execute(delete_entry)
        cursor.execute('COMMIT')