from menu import *


if __name__ == '__main__':
    try:
        print(colored("""
        `*kMdMkr`        
       l@@#MeMB@@c       
      l@@L     x@@V      
      E@@       #@0      
    `vB@@xxxxxxx@@Bv`    
    V@@@@@@3}K@@@@@@y    
    V@@@@@B` `Q@@@@@w    Password Manager Python
    V@@@@@@] x@@@@@@w    
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