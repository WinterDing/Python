#!/usr/bin/python

import random

def passwd_generator(passwd , passwd_len):
    for i in range(passwd_len):
        choice = random.randrange(1,5)
        if choice == 1:
            member = str(random.randrange(0,9))     #number 0-9
        elif choice == 2:
            member = chr(random.randrange(65,90))   #upper case English characters
        elif choice == 3:
            member = chr(random.randrange(97,122))  #lower case English characters
        else:
            member = chr(random.randrange(33,47))   #special characters
        passwd.append(member)
        passwd_return = ''.join(passwd)
    return passwd_return

def main():
    passwd_require_length = input('the length of password: ')
    passwd_initial = []
    passwd_final = passwd_generator(passwd_initial , passwd_require_length)
    print passwd_final



if __name__ == '__main__':
    main()
