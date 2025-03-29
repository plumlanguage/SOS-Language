bits 64
section .data
    msg db 'Hello,SOS!', 0Dh, 0Ah, 0

section .text
global main
extern GetStdHandle, WriteFile, ExitProcess

main:
    mov rcx, -11
    call GetStdHandle
    mov rcx, rax
    lea rdx, [rel msg]
    mov r8d, 13
    xor r9, r9
    push 0
    sub rsp, 32
    call WriteFile
    mov rcx, 0
    call ExitProcess