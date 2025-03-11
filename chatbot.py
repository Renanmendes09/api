import google.generativeai as genai

# Configuração da API (INSIRA SUA CHAVE)
API_KEY = "AIzaSyDmkj8zwPqKwrFR72RDw-RFaLZeD9ZA2zs"

# Valida se a chave foi inserida corretamente
if not API_KEY:
    raise ValueError("⚠️ ERRO: Insira sua chave de API Gemini no código!")

# Configura a API do Gemini
genai.configure(api_key=API_KEY)

# Inicializa a sessão do chatbot com histórico
model = genai.GenerativeModel("gemini-1.5-pro")
chat_session = model.start_chat(history=[])

# Nome do chatbot (altere aqui)
CHATBOT_NOME = "Sara"

def chat():
    print(f"\n✨ Olá! Eu sou {CHATBOT_NOME}, sua assistente virtual. Como posso te ajudar hoje?\n")
    print("💡 Dica: Digite 'sair' para encerrar a conversa.\n")

    while True:
        try:
            # Entrada do usuário
            user_input = input("Você 🧑: ").strip()
            if user_input.lower() in ["sair", "exit", "desistir"]:
                print(f"\n👋 Foi ótimo conversar com você! Até a próxima. 💙")
                break
            
            # Envia mensagem e obtém resposta do modelo
            response = chat_session.send_message(user_input)

            # Exibe a resposta formatada com nome e emojis
            bot_response = response.text
            print(f"\n{CHATBOT_NOME} 🤖: {bot_response}\n")

        except Exception as e:
            print(f"⚠️ Opa! Algo deu errado. Erro: {e}")
            break  # Encerra o chat em caso de erro crítico

# Inicia o chatbot
if __name__ == "__main__":
    chat()
