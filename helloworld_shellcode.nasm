section .text

global _start

_start:

	xor eax,eax
	push eax
	push 0x0a646c72
	push 0x6f77206f
	push 0x6c6c6568
	mov ecx,esp

	push 12
	pop edx
	push 0x1
	pop ebx
	inc eax
	push eax
	mov al,4
	int 80h

	pop eax
	xor ebx,ebx
	int 80h	
