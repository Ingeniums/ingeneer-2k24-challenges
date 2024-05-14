global _start
_start:
    jmp L01
crazy:
    mov rax, 0x6c77706b5a4d4477
    push rax
    xor rcx, rcx
    mov ecx, 10
    mov rsi, 0
    lea rbx, [lol]
loop:
    mov al, byte [rbx+rsi]
    xor al, byte [rsp+rsi]
    mov [rsp+rsi], al
    inc rsi
    loop loop    

    mov ecx, 11
    mov rsi, 10
loop1:
    mov al, [rsp+rsi]
    test rsi, 1
    jnz odd
even:
    add al, 2
    mov [rsp+rsi], al
    inc rsi
    loop loop1
    jmp crazy2
odd:
    sub al, 3
    mov [rsp+rsi], al
    inc rsi
    loop loop1
crazy2:
    lea r8, [rsp+21]
    mov rsi, 0
    xor eax, eax
    xor edi, edi
    xor ebx, ebx
    mov rcx, 11
    mov r9, 11
loop2:
    mov bl, [r8+rsi]
    lea rax, [rsi+8]
    mov edx, 0
    idiv r9
    mov [lil+rdx], bl
    inc rsi
    loop loop2

    mov rcx, 11
    mov rsi, 0
loop3:
    mov al, [lil+rsi]
    mov [r8+rsi], al
    inc rsi
    loop loop3
 


P02:
    push rcx
    jmp L03
L01:
    mov rdx, 0x4d3541736f45565f
    jmp P01
L03:
    mov rbx, 0x3746665d39364c35
P03:
    push rbx
    jmp crazy
P01:
    push 0xa
    push rdx
L02:
    mov rcx, 0x534b6e6c332f736b
    jmp P02


lol:
    db '4', 't', '#', '=', 0x19, 'D', 0x03, 'Y', 'j', '4'
section .bss
lil:
    resb 11
