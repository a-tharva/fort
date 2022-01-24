# path defined in utils, not tested .env in linux 
# hence path is defined in utils
PATH = 'pyfort'
    

def _help():
    # Help print function
    print('''

  [display / get / help / insert / logout / replace]

  display:    display whole database 
  get:        get selected password and decrypt it 
  help:       print help context
  insert:     insert into database 
  logout:     logout of current acount
  replace:    replace element from table
''')


def logo():
    # logo print function
    print('''
  __         _
 / _|___ _ _| |_
|  _/ _ \ '_|  _|
|_| \___/_|  \__|

''')