# path defined in utils, not tested .env in linux 
# hence path is defined in utils
PATH = 'pyfort'
    
# Help print function
def _help():
    print('''

[display / get / help / insert / logout / replace]

display:    display whole database 
get:        get selected password and decrypt it 
help:       print help context
insert:     insert into database 
logout:     logout of current acount
replace:    replace element from table

''')

# logo print function
def logo():
    print('''
  __         _
 / _|___ _ _| |_
|  _/ _ \ '_|  _|
|_| \___/_|  \__|

''')