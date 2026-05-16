# Trabalho Prático: Pipeline Escalar e Superescalar
Arquitetura de Computadores III - Engenharia de Computação (PUC Minas)

Este repositório contém as ferramentas de simulação, scripts de automação e o relatório técnico para o estudo de paralelismo em nível de instrução (ILP) em microarquiteturas RISC-V.

## Estrutura do Projeto

### Automação e Análise (Agentes)
O projeto utiliza um sistema de agentes Python para processar os dados e gerar o relatório:
*   `gerenciador_tp.py`: Script principal que coordena o fluxo de trabalho.
*   `agente_questoes.py`: Resolve as questões técnicas embutidas nos arquivos assembly.
*   `agente_relatorio.py`: Consolida os resultados e gera o código LaTeX.
*   `agente_revisor.py`: Realiza a auditoria técnica do conteúdo gerado.
*   `agent_comparador.py`: Compara integridade entre arquivos.
*   `agent_inconsistencia.py`: Valida o relatório final contra os requisitos do `main.pdf`.

### Documentação
*   `relatorio.pdf`: Relatório técnico final consolidado.
*   `relatorio.tex`: Código-fonte LaTeX do relatório.
*   `main.pdf`: Documento de requisitos e roteiro do trabalho.

### Simulações (Assembly RISC-V)
*   `s1` a `s5`: Sequências para análise de hazards de pipeline escalar.
*   `t1` e `t2`: Sequências para análise do Algoritmo de Tomasulo (OoO).

## Como Reproduzir os Resultados

### Pré-requisitos
*   Python 3.10+
*   Distribuição LaTeX (ex: TeX Live) para compilação do relatório.

### Instalação de Dependências
```bash
pip install google-generativeai python-dotenv
```

### Execução do Fluxo de Trabalho
1.  Configure sua chave de API no arquivo `.env`:
    ```text
    GOOGLE_API_KEY=SUA_CHAVE_AQUI
    ```
2.  Execute o gerenciador para processar os dados e gerar o `.tex`:
    ```bash
    python3 gerenciador_tp.py
    ```
3.  Compile o relatório final:
    ```bash
    pdflatex relatorio.tex
    ```

### Validação de Requisitos
Para garantir que o relatório atende a todas as exigências do roteiro:
```bash
python3 agent_inconsistencia.py
```

## Link do Repositório
[https://github.com/IagoVRomeiro/AC3-Trabalho](https://github.com/IagoVRomeiro/AC3-Trabalho)
