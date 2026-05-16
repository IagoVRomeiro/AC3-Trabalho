import os
import google.generativeai as genai

class AgenteQuestoes:
    """Agente responsável por extrair e responder questões embutidas nos arquivos de assembly."""
    def __init__(self, model_name="models/gemini-2.5-flash"):
        self.model = genai.GenerativeModel(model_name)

    def ler_arquivos(self, diretorio):
        arquivos_alvo = [
            "s1_raw_chain.s", "s2_loop_raw_branch.s", "s3_load_use.s", "s4_war_waw.s", "s5_branches.s",
            "t1_tomasulo_raw.s", "t2_tomasulo_war_waw.s"
        ]
        conteudo_consolidado = ""
        
        for arquivo in arquivos_alvo:
            caminho_completo = os.path.join(diretorio, arquivo)
            if os.path.exists(caminho_completo):
                with open(caminho_completo, 'r', encoding='utf-8') as f:
                    conteudo_consolidado += f"\n\n--- ARQUIVO: {arquivo} ---\n"
                    conteudo_consolidado += f.read()
            else:
                print(f"Aviso: Arquivo {arquivo} não encontrado no diretório {diretorio}.")
                
        return conteudo_consolidado

    def resolver_questoes(self, diretorio="./"):
        print("🔍 Lendo arquivos de assembly e procurando por questões...")
        conteudo_arquivos = self.ler_arquivos(diretorio)
        
        if not conteudo_arquivos.strip():
            return "Nenhum conteúdo encontrado para análise."

        prompt = f"""
        Você é um professor e engenheiro especialista em Arquitetura de Computadores.
        Sua tarefa é atuar como um assistente de resolução para um Trabalho Prático completo sobre Pipeline Escalar e Superescalar.
        
        DIRETRIZES DO TRABALHO PRÁTICO (O que você deve resolver explicitamente):
        
        PARTE A — Pipeline Escalar (Arquivos S1 a S5):
        1. Roteiro de Simulação: Calcule CPI e número de stalls para configurações com/sem forwarding e predição (estática, 1-bit, 2-bits).
        2. Diagrama: Trace o diagrama de estágios para as 3 primeiras iterações do loop, identificando stalls e forwarding.
        3. Load-Use (S3): Demonstre analiticamente por que o load-use hazard não pode ser eliminado por forwarding e requere stall de 1 ciclo. Mostre o escalonamento pelo compilador.
        4. Escalonamento: Aplique escalonamento estático para eliminar stalls sempre que possível.
        5. Predição (S5): Construa a tabela de histórico do preditor de 2 bits (autômato de 4 estados) para os desvios e calcule a taxa de acerto.
        6. Análise Requerida: Calcule speedup, identifique o fator afetado na fórmula de tempo (Tempo = Ninst × CPI × Tciclo) e justifique por que 2-bits supera 1-bit.
        
        PARTE B — Pipeline Superescalar e Tomasulo (Arquivos T1, T2 e S4):
        1. Algoritmo de Tomasulo (T1 e T2): Preencha ciclo a ciclo as tabelas de: Instruction Status, Reservation Station, Register Result Status e CDB Broadcasts. Assuma as latências fornecidas: ADD.D(2), MUL.D(4), DIV.D(8). Despacho de 1 instrução por ciclo, em ordem.
        2. Renomeação de Registradores (S4): Identifique dependências RAW, WAR e WAW. Aplique renomeação manual usando uma Register Alias Table (RAT) com 16 registradores físicos (P0-P15). Calcule o ILP máximo após a renomeação assumindo recursos ilimitados.
        3. Simulação Superescalar: Calcule o IPC e analise o tamanho do ROB para configurações OoO variadas (C1 a C5). Aplique a Lei de Amdahl ao ILP para descobrir a fração não paralelizável de cada sequência.
        
        PARTE 5 — Análise Integradora — Do Escalar ao Superescalar:
        1. Curva de Evolução (S2): Discuta e estime os valores para a curva teórica de CPI/IPC aplicando progressivamente: (a) base, (b) + forwarding, (c) + predição 2-bits, (d) + escalonamento estático, (e) + 2-wide in-order, (f) + OoO 2-wide, (g) + OoO 4-wide. Discuta o retorno decrescente.
        2. Cálculo de IPC Efetivo: Calcule usando a fórmula IPCef = IPCideal / (1 + fdesvio * (1 - precisao) * penalidade) com os dados: IPCideal=3.2, fdesvio=0.30, precisao=0.95, penalidade=15.
        3. Paradoxo da Dependência de Memória: Explique como o hardware garante correção semântica ao reordenar loads/stores (Store Buffers, Memory Disambiguation).
        4. Comparação Arquitetural: VLIW (escalonamento estático) vs. Interlocking (hardware in-order) vs. Algoritmo de Tomasulo (OoO dinâmico). Cite vantagens, desvantagens e cenários ideais.

        Sua Saída:
        Apresente um documento Markdown bem estruturado contendo a resolução detalhada, matemática e técnica de TODOS esses tópicos. 
        Use os códigos fornecidos na seção abaixo como base para seus cálculos.

        --- CÓDIGOS ASSEMBLY ---
        {conteudo_arquivos}
        """
        
        print("🧠 Gerando respostas com o Gemini...")
        response = self.model.generate_content(prompt)
        return response.text

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
    agente = AgenteQuestoes()
    respostas = agente.resolver_questoes("/home/iago/Downloads/AC3/")
    
    with open("/home/iago/Downloads/AC3/respostas_questoes.md", "w", encoding="utf-8") as f:
        f.write(respostas)
    print("✅ Respostas geradas e salvas em 'respostas_questoes.md'.")
