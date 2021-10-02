from save_retrive import *

#search_display_database('asd')

result = show('asd', 'EREW')
for _ in result:
    print('\n','User name:',_[0])
    print(' password :',_[1])