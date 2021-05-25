
from test import *

def main():
    user_input = input(" Use a for loop or a while loop? for or while ")
    if user_input == 'for':
        use_for_loop()
    elif user_input == 'while':
        use_while_loop()
   

if __name__ == '__main__':
    main()