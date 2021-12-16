#!/usr/bin/env python

import sys

def get_mode():
    while True:
        print("Welcome to the hex2oct2int converter program ..\n")
    
        print("Enter the choice from which you want a conversion to be conducted ..")
        print("Enter : (o) : Octal     (h) : Hex      (i) : int ")
        
        mode1 = raw_input()

        print("Enter the choice to which you want the conversion ..")
        print("Enter : (o) : Octal     (h) : Hex      (i) : int ")

        mode2 = raw_input()

        if mode1 in " o h i ".split() and mode2 in "o h i".split():
            return mode1,mode2
        else:
            print("Please enter again correctly ..")

def main():
    mode = get_mode()

    if mode[0] == "o" and mode[1] == "h" :
        num = input("Enter the octal number :")
        num = int(num)

        decimal_value = 0
        base = 1

        while (num):
            last = num % 10
            num = int(num/10)
            decimal_value += last * base
            base = base * 8

        print(hex(decimal_value))


    elif mode[0] == "o" and mode[1] == "i":
        num = input("Enter the octal number :")
        num = int(num)

        decimal_value = 0
        base = 1

        while (num):
            last = num % 10
            num = int(num/10)
            decimal_value += last * base
            base = base * 8

        print(decimal_value)

    elif mode[0] == "h" and mode[1] == "o":
        num = input("Enter the hex number : ")
        print(oct(num))

    elif mode[0] == "i" and mode[1] == "o":
        num = input("Enter the integer : ")
        print(oct(num))

    elif mode[0] == "i" and mode[1] == "h":
        num = input("Enter the integer:")
        print(hex(num))

    elif mode[0] == "h" and mode[1] == "i":
        num = input("Enter the hexadecimal : ")
        print(int(num))
    else:
        print("Run the program again ... ")
        print("Something went wrong (Input/Processing)")

    sys.exit(0);

main()
    
    
