from .menu import show_menu
from .utils.utils import logo

def main():
    try:
        logo()
        show_menu()
        
    except KeyboardInterrupt:
        print('\nExiting...')