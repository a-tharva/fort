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
    print("""
          kMdMk         
        @@#MeMB@@        
       @@       @@       
      @@         @0      
     vB@@xxxxxxx@@Bv       __         _
    V@@@@@@3}K@@@@@@y     / _|___ _ _| |_
    V@@@@@B` `Q@@@@@w    |  _/ _ \ '_|  _| 
    V@@@@@@] [@@@@@@w    |_| \___/_|  \__|  Password Manager
    V@@@@@#|_|#@@@@@w    
    !dRRRRRRRRRRRRRd!""")
        
    print("""
Program Created By a-tharva
Link to Original: github.com/a-tharva/
Info: - This is written in Python
      - Still in development""")