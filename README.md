# Trabalho Prático: Pipeline Escalar e Superescalar
Arquitetura de Computadores III - Engenharia de Computação (PUC Minas)

Este repositório contém as sequências de instruções assembly e o relatório técnico final para o estudo de paralelismo em nível de instrução (ILP) em microarquiteturas RISC-V.

## Estrutura do Projeto

### Documentacao
*   relatorio.pdf: Relatório técnico final consolidado, contendo a análise de hazards, predição de desvios e simulação do Algoritmo de Tomasulo.
*   relatorio.tex: Código-fonte LaTeX do relatório.
*   main.pdf: Documento de requisitos e roteiro original do trabalho.

### Simulacoes (Assembly RISC-V)
*   **Pipeline Escalar (s1_raw_chain.s a s5_branches.s)**: Sequências projetadas para quantificar o impacto de Data Hazards (RAW, WAR, WAW) e Control Hazards, validando a eficácia de técnicas de Forwarding e Predição Dinâmica.
*   **Pipeline Superescalar (t1_tomasulo_raw.s e t2_tomasulo_war_waw.s)**: Trechos de código para análise de execução fora de ordem (OoO) utilizando o Algoritmo de Tomasulo, demonstrando a resolução de conflitos via Estações de Reserva e RAT.

## Reprodução dos Resultados

Os resultados apresentados no relatório podem ser validados utilizando o simulador [Ripes](https://github.com/mortbopet/Ripes). Para cada sequência:
1. Carregue o arquivo .s correspondente no simulador.
2. Configure o processador para "5-Stage Processor".
3. Alterne as opções de "Enable Forwarding" e os tipos de "Branch Predictor" conforme as configurações descritas nas tabelas de resultados do relatório.

## Link do Repositório
https://github.com/IagoVRomeiro/AC3-Trabalho
