import os
import google.generativeai as genai

class AgenteRevisor:
    """Agente responsável por auditar o relatório LaTeX contra a estrutura de referência."""
    def __init__(self, model_name="models/gemini-2.5-flash"):
        self.model = genai.GenerativeModel(model_name)

    def auditar_relatorio(self, caminho_tex):
        print("🧐 Lendo o relatório LaTeX para auditoria...")
        if not os.path.exists(caminho_tex):
            return f"Erro: Arquivo {caminho_tex} não encontrado."
            
        with open(caminho_tex, "r", encoding="utf-8") as f:
            conteudo_tex = f.read()

        prompt = f"""
        Você é um professor universitário e avaliador acadêmico extremamente rigoroso.
        Sua tarefa é ler o código LaTeX de um relatório e verificar se ele mantém a estrutura do relatório original de referência.

        ESTRUTURA DE REFERÊNCIA ESPERADA:
        1. INTRODUÇÃO
        2. FUNDAMENTAÇÃO TEÓRICA
        3. METODOLOGIA
        4. RESULTADOS A: PIPELINE ESCALAR
        5. RESULTADOS B: ARQUITETURA SUPERESCALAR E TOMASULO
        6. ANÁLISE INTEGRADA E LEIS DE DESEMPENHO
        7. ANÁLISE DOS QUESTIONÁRIOS DE LABORATÓRIO
        8. CONCLUSÃO
        9. REFERÊNCIAS
        A. APÊNDICES

        Sua Saída:
        Crie um checklist detalhado validando se a transição entre o conteúdo antigo e as novas análises foi suave e se a fidelidade ao original foi mantida.
        Aponte se algo essencial foi perdido ou se o nome "Relatório Final" foi indevidamente utilizado.
        
        --- CÓDIGO LATEX DO RELATÓRIO ATUAL ---
        {conteudo_tex}
        """
        
        print("⚖️ Avaliando a fidelidade à referência...")
        response = self.model.generate_content(prompt)
        return response.text