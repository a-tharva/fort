from pyfort.menu import *


def main():
    try:
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
        
        print(colored( """
Program Created By a-tharva
Link to Original: github.com/a-tharva/
Info: - This is written in Python
      - Still in development""", 'red'))
        show_menu()
        
    except KeyboardInterrupt:
        print('\nExiting...')