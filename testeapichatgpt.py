import os
from openai import OpenAI

def executar_prompt_openai(prompt_usuario: str):
    """
    Conecta-se à API da OpenAI, envia um prompt e retorna a resposta do modelo.

    Args:
        prompt_usuario: O prompt/pergunta que você quer enviar para a IA.

    Returns:
        A resposta de texto do modelo ou uma mensagem de erro.
    """
    try:
        # Carrega a chave de API da variável de ambiente
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "Erro: A variável de ambiente OPENAI_API_KEY não foi definida."

        # Inicializa o cliente da OpenAI
        client = OpenAI(api_key=api_key)

        print("Enviando prompt para a OpenAI...")

        # Cria a chamada para a API de Chat Completions
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Modelo que você deseja usar (ex: "gpt-4", "gpt-3.5-turbo")
            messages=[
                {"role": "system", "content": "Você é um assistente prestativo."},
                {"role": "user", "content": prompt_usuario}
            ]
        )

        # Extrai e retorna o conteúdo da resposta
        resposta = completion.choices[0].message.content
        return resposta

    except Exception as e:
        return f"Ocorreu um erro ao conectar com a OpenAI: {e}"

# --- Exemplo de como usar a função ---
if __name__ == "__main__":
    # Defina aqui o prompt que você quer enviar
    meu_prompt = "Qual é a distância da Terra até a Lua em quilômetros?"

    # Chama a função e armazena a resposta
    resultado = executar_prompt_openai(meu_prompt)

    # Imprime o resultado
    print("\n--- Resposta da OpenAI ---")
    print(resultado)
    print("---------------------------\n")