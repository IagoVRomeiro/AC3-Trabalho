import google.generativeai as genai

class AgenteCronograma:
    """Agente responsável por gerar um checklist interativo e detalhado do cronograma do trabalho."""
    def __init__(self, model_name="models/gemini-2.5-flash"):
        self.model = genai.GenerativeModel(model_name)

    def gerar_cronograma(self):
        print("📅 Gerando cronograma de atividades detalhado...")
        
        prompt = """
        Você é um gerente de projetos ágil e monitor especialista em Arquitetura de Computadores.
        O aluno possui o seguinte cronograma de 18 dias para entregar um Trabalho Prático sobre Pipeline Escalar, Superescalar e Tomasulo:

        Dias 1–2: Preparação (Formação do grupo; instalação do simulador; leitura do roteiro) - Entregável: Simulador configurado.
        Dias 3–5: Parte A (Sim. S1–S5 nas configurações a e b; diagrama de estágios manual para S2) - Entregável: Tabelas CPI + diagrama S2.
        Dias 6–7: Parte A (Sim. configs c, d e e; escalonamento estático de S2; preditor de 2 bits para S5) - Entregável: Tabela consolidada + gráfico.
        Dias 8–10: Parte B (Simulação manual do Tomasulo T1 e T2 ciclo a ciclo) - Entregável: Tabelas completas Tomasulo.
        Dias 11–12: Parte B (Renomeação de registradores S4: grafo, RAT, ILP máximo) - Entregável: Sequência renomeada + grafo.
        Dias 13–14: Parte B (Simulação das configurações C1–C5; coleta de IPC) - Entregável: Tabela IPC + gráfico speedup.
        Dias 15–16: Integração (Análise integradora Seção 5; curva de evolução; cálculo IPC efetivo) - Entregável: Rascunho da integração.
        Dia 17: Relatório (Redação e revisão do relatório final; figuras definitivas) - Entregável: Rascunho completo.
        Dia 18: Entrega (Submissão e repositório Git) - Entregável: Relatório final + link Git.

        Sua tarefa:
        1. Crie um documento Markdown estruturando um Checklist Diário (Dia 1 até Dia 18).
        2. Use caixas de seleção `[ ]` para cada subtarefa.
        3. Adicione pequenas "Dicas do Monitor" em cada bloco, lembrando o aluno de detalhes técnicos cruciais (ex: lembrete de que Load-Use causa 1 bolha irredutível, latência de 8 ciclos no DIV do Tomasulo, como fazer gráfico de speedup no Excel/Python, etc).
        4. Seja motivador, claro e organizado.
        """
        
        print("🧠 Consultando o Gemini para estruturar o plano de ação...")
        response = self.model.generate_content(prompt)
        return response.text

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
    agente = AgenteCronograma()
    cronograma_md = agente.gerar_cronograma()
    
    with open("/home/iago/Downloads/AC3/cronograma_detalhado.md", "w", encoding="utf-8") as f:
        f.write(cronograma_md)
    print("✅ Checklist de cronograma gerado e salvo em 'cronograma_detalhado.md'.")