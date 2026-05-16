import google.generativeai as genai

class AgenteRelatorio:
    """Gera o arquivo LaTeX consolidado respeitando o relatório existente como referência."""
    def __init__(self, model_name="models/gemini-2.5-flash"):
        self.model = genai.GenerativeModel(model_name)

    def gerar_latex_consolidado(self, rascunho, codigos):
        print("📝 Agente de Relatório consolidando dados com base na referência...")
        
        # Tenta ler a referência do PDF se o arquivo existir
        try:
            with open("/home/iago/Downloads/AC3/relatorio_referencia.txt", "r", encoding="utf-8") as f:
                referencia = f.read()
        except FileNotFoundError:
            referencia = "Referência do PDF não encontrada."

        prompt = f"""
        Você é um professor de Arquitetura de Computadores e especialista em LaTeX.
        Sua tarefa é atualizar um relatório acadêmico existente, mantendo sua estrutura e estilo originais, mas incorporando análises técnicas densas e cálculos precisos.

        DIRETRIZ OBRIGATÓRIA:
        - NÃO use o nome "Relatório Final". O arquivo deve ser apenas "Relatório de Atividades".
        - Use o conteúdo da REFERÊNCIA DO PDF como base principal.
        - Integre TODOS os cálculos, tabelas de CPI, e análises técnicas contidas no RASCUNHO nas seções apropriadas.
        - Garanta que a seção de RESULTADOS A e B contenha a densidade técnica exigida (fórmulas, valores de CPI/IPC, latências de Tomasulo).

        ESTRUTURA DE SEÇÕES (Siga fielmente a ordem da referência):
        1. INTRODUÇÃO
        2. FUNDAMENTAÇÃO TEÓRICA (Mantenha densa: Pipeline, Hazards, Tomasulo, CDB, Memória)
        3. METODOLOGIA
        4. RESULTADOS A (Integre dados de S1, S3, S5: CPI, bolhas, eficácia da predição)
        5. RESULTADOS B (Integre dados de T1, T2: Latências DIVD, ciclos de Write Result, renomeação de registradores)
        6. ANÁLISE INTEGRADORA (Inclua o IPC Comparativo: Escalar vs Superescalar vs Tomasulo)
        7. CONCLUSÃO
        8. REFERÊNCIAS
        A. APÊNDICES (Inclua os códigos Assembly completos)

        DADOS PARA INTEGRAR:
        --- REFERÊNCIA DO PDF EXISTENTE ---
        {referencia}

        --- NOVO RASCUNHO (RESULTADOS DO AGENTE DE QUESTÕES) ---
        {rascunho}
        
        --- CÓDIGOS ASSEMBLY ---
        {codigos}
        
        INSTRUÇÕES LaTeX:
        - Use documentclass article, 12pt, geometry(margin=2.5cm), e pacotes: amsmath, graphicx, booktabs, hyperref, setspace.
        - Retorne APENAS o código LaTeX puro, sem blocos de código markdown.
        """
        response = self.model.generate_content(prompt)
        return response.text