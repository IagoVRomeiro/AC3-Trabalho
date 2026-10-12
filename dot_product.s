# ==========================================================
# TP2 - Simulação de Pipeline e Hazards (Arq. de Computadores III)
# Produto escalar (dot product) de dois vetores de inteiros
# Arquitetura: RISC-V (RV32IM) - simulador Ripes
#
# Resultado esperado em a0: 220
#   1*10 + 2*9 + 3*8 + 4*7 + 5*6 + 6*5 + 7*4 + 8*3 + 9*2 + 10*1
# ==========================================================

.data
# Vetor A com 10 elementos (cada .word ocupa 4 bytes)
vetorA:   .word 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# Vetor B com 10 elementos
vetorB:   .word 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

.text
.globl main
main:
    la   t0, vetorA        # t0 = ponteiro para o início de A
    la   t1, vetorB        # t1 = ponteiro para o início de B
    li   t2, 10            # t2 = contador de iterações (tamanho dos vetores)
    li   a0, 0             # a0 = acumulador do produto escalar (resultado final)

loop:
    lw   t4, 0(t0)         # t4 = A[i]
    lw   t5, 0(t1)         # t5 = B[i]
    mul  t6, t4, t5        # t6 = A[i] * B[i]
                           #   -> RAW em t5 (lw -> mul): load-use hazard
    add  a0, a0, t6        # acumula: a0 += t6
                           #   -> RAW em t6 (mul -> add)
    addi t0, t0, 4         # avança ponteiro de A para o próximo inteiro
    addi t1, t1, 4         # avança ponteiro de B para o próximo inteiro
    addi t2, t2, -1        # decrementa o contador
    bne  t2, zero, loop    # BRANCH DE FIM DE LAÇO: repete enquanto t2 != 0
                           #   -> RAW em t2 (addi -> bne) + hazard de controle

fim:
    li   a7, 10            # ecall 10 = encerrar o programa no Ripes
    ecall
