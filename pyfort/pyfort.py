from pyfort.menu import *


def main():
    try:
        print(colored("""
        `*kMdMkr`        
       l@@#MeMB@@c       
      l@@L     x@@V      
      E@@       #@0      
    `vB@@xxxxxxx@@Bv`      __         _
    V@@@@@@3}K@@@@@@y     / _|___ _ _| |_
    V@@@@@B` `Q@@@@@w    |  _/ _ \ '_|  _| 
    V@@@@@@] x@@@@@@w    |_| \___/_|  \__|  Password Manager
    V@@@@@#_--#@@@@@w    
    !dRRRRRRRRRRRRRd!""", 'blue'))
        
        print(colored( """
Program Created By a-tharva
Link to Original: github.com/a-tharva/
Info: - This is written in Python
      - Still in development""", 'red'))
        show_menu()
        
    except KeyboardInterrupt:
        print('\nExiting...')