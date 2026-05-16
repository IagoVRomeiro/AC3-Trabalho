import os
import google.generativeai as genai
from dotenv import load_dotenv
from agente_questoes import AgenteQuestoes
from agente_relatorio import AgenteRelatorio
from agente_revisor import AgenteRevisor
from agente_cronograma import AgenteCronograma

# Configuração da API
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    diretorio = "/home/iago/Downloads/AC3/"
    
    print("🚀 Iniciando o Gerenciador do Trabalho Prático...\n")
    
    # 1. Gerar o Cronograma
    agente_cron = AgenteCronograma()
    crono_md = agente_cron.gerar_cronograma()
    with open(os.path.join(diretorio, "cronograma_detalhado.md"), "w", encoding="utf-8") as f:
        f.write(crono_md)
        
    # 2. Resolver as Questões
    agente_quest = AgenteQuestoes()
    respostas = agente_quest.resolver_questoes(diretorio)
    with open(os.path.join(diretorio, "respostas_questoes.md"), "w", encoding="utf-8") as f:
        f.write(respostas)
        
    # 3. Gerar o Relatório
    print("📝 Lendo referências e gerando relatório LaTeX...")
    agente_rel = AgenteRelatorio()
    
    # Preferência: Usar relatorio.pdf como rascunho base se existir (via OCR manual ou leitura prévia)
    # Aqui vamos assumir que o rascunho.txt pode conter o texto extraído ou ser o rascunho manual.
    try:
        with open(os.path.join(diretorio, "rascunho.txt"), "r", encoding="utf-8") as f:
            rascunho = f.read()
    except FileNotFoundError:
        rascunho = "Rascunho não encontrado. Usando dados dos agentes."
        
    try:
        with open(os.path.join(diretorio, "respostas_questoes.md"), "r", encoding="utf-8") as f:
            respostas_ia = f.read()
    except FileNotFoundError:
        respostas_ia = ""

    codigos = agente_quest.ler_arquivos(diretorio)
    latex_code = agente_rel.gerar_latex_consolidado(rascunho + "\n\n--- RESPOSTAS GERADAS PELA IA (INSERIR OBRIGATORIAMENTE NO TEXTO) ---\n" + respostas_ia, codigos)
    
    # Limpeza de formatação markdown caso a IA retorne com crases
    latex_code = latex_code.replace("```latex\n", "").replace("```", "").strip()
        
    caminho_tex = os.path.join(diretorio, "relatorio.tex")
    with open(caminho_tex, "w", encoding="utf-8") as f:
        f.write(latex_code)
    print("✅ Relatório LaTeX gerado e salvo em 'relatorio.tex'.")
        
    # 4. Auditar o Relatório
    agente_rev = AgenteRevisor()
    auditoria = agente_rev.auditar_relatorio(caminho_tex)
    with open(os.path.join(diretorio, "auditoria_relatorio.md"), "w", encoding="utf-8") as f:
        f.write(auditoria)
        
    print("\n🎉 Processo completo concluído! Todos os agentes finalizaram suas tarefas.")

if __name__ == "__main__":
    main()