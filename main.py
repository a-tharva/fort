
from menu import *


if __name__ == '__main__':
    try:
        print(colored("""
                                /3888@@@@8803/
                              /8@@@@@@@@@@@@@@8/
                             7@@@8          78@@@
                             @@@8            8@@8
                             @@@%            %@@@
                             @@@%            %@@@
                             @@@%            %@@@
                             @@@%            %@@@
                         ///7@@@6////////////6888///*
                         6888888888888800000000000003
                         6888888888888800000000000003
                         6888888888888800000000000003
                         688888888889/=+/600000000003
                         688888888881_==_200000000003
                         6888888888881_=1900000000003
                         6888888888880_=9000000000003
                         6888888888880++9000000000003
                         6888888888888800000000000003
                         6500000000000066666666666633""", 'blue'))
        print(colored( """
                            Password Manager Python
                            
Program Created By a-tharva
Link to Original: github.com/a-tharva/
Info:
    - This is written in Python
    - Still in development""", 'red'))
        show_menu()
        
    except KeyboardInterrupt:
        pass