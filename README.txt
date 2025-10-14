# 🤖 OpenAI Prompt Executor - Projeto Python

## 📋 Sobre o Projeto

O **OpenAI Prompt Executor** é um script Python que demonstra como **conectar-se à API da OpenAI** para executar um **prompt** e receber uma **resposta automática** de um modelo de linguagem, como o **GPT-3.5-Turbo**.  

Este projeto foi desenvolvido para fins educacionais e serve como base para integrar modelos da OpenAI em aplicações Python de forma **segura, modular e reutilizável**.

---

## 🎯 Objetivos

- Demonstrar a autenticação e uso da API da OpenAI  
- Executar prompts e exibir respostas de modelos GPT  
- Mostrar boas práticas no uso de **variáveis de ambiente**  
- Implementar **tratamento de erros** em requisições  
- Fornecer um exemplo funcional e de fácil reutilização  

---

## 🏗️ Estrutura do Projeto

openai-prompt-executor/
├── executar_prompt.py # 🧠 Script principal de execução do prompt
└── requirements.txt # 📦 Lista de dependências Python

yaml
Copy code

---

## ⚙️ Configuração

### 1️⃣ Instalar Dependências

Crie um arquivo **`requirements.txt`** com o seguinte conteúdo:

openai

javascript
Copy code

Depois, instale as dependências com o comando:

```bash
pip install -r requirements.txt
2️⃣ Configurar a Chave de API da OpenAI
Você precisa de uma chave de API para autenticação.

🔑 Passo 1 — Obter a Chave
Acesse o painel da OpenAI:
👉 https://platform.openai.com/api-keys

Crie (ou copie) sua chave secreta.

🧱 Passo 2 — Configurar como Variável de Ambiente (Recomendado)
💻 Windows (CMD ou PowerShell)
bash
Copy code
setx OPENAI_API_KEY "sua-chave-secreta-aqui"
Feche e reabra o terminal após definir a variável.

🐧 macOS / Linux
bash
Copy code
export OPENAI_API_KEY="sua-chave-secreta-aqui"
Para tornar permanente, adicione a linha ao arquivo ~/.bashrc ou ~/.zshrc.

🚀 Como Executar
Após instalar as dependências e configurar a chave de API, execute o script principal:

bash
Copy code
python executar_prompt.py
O script enviará um prompt de exemplo à API da OpenAI e imprimirá a resposta diretamente no console.

✨ Funcionalidades
✅ Conexão Segura:
Usa variáveis de ambiente para proteger sua chave da API.

🧩 Função Modular:
Toda a lógica está dentro da função executar_prompt_openai(), facilitando a reutilização.

🛡️ Tratamento de Erros:
Inclui try...except para capturar erros de autenticação e conexão.

💬 Exemplo de Uso:
O bloco if __name__ == "__main__": demonstra como utilizar a função principal.

🤖 Compatível com Modelos de Chat:
Utiliza o endpoint chat.completions, compatível com GPT-3.5-Turbo e GPT-4.

🧩 Estrutura do Código
🐍 executar_prompt.py
python
Copy code
import os
from openai import OpenAI

def executar_prompt_openai(prompt: str):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    print("Enviando prompt para a OpenAI...\n")
    resposta = executar_prompt_openai("Qual é a distância média da Terra até a Lua?")
    print("\n--- Resposta da OpenAI ---")
    print(resposta)
    print("---------------------------")
📸 Exemplo de Execução
css
Copy code
Enviando prompt para a OpenAI...

--- Resposta da OpenAI ---
A distância média da Terra até a Lua é de aproximadamente 384.400 quilômetros.
Essa distância pode variar um pouco porque a órbita da Lua não é perfeitamente circular.
---------------------------
🔧 Troubleshooting
❌ Erro de Autenticação (invalid_api_key - Erro 401)
Sua chave de API está incorreta, expirada ou não configurada.

✅ Soluções:

Verifique sua chave no Painel da OpenAI

Feche e reabra o terminal após usar setx ou export

Certifique-se de incluir as aspas ao definir a variável

❌ Erro de Cota Insuficiente (insufficient_quota - Erro 429)
Sua conta OpenAI não possui créditos disponíveis.

💳 Soluções:

Verifique se seus créditos de teste expiraram

Adicione um método de pagamento em:
OpenAI Billing

🔗 Links Úteis
📚 Documentação da API da OpenAI
🔑 Página de Chaves de API
💵 Página de Faturamento (Billing)
🐍 Biblioteca OpenAI para Python (GitHub)

📜 Licença
Este projeto é distribuído para fins educacionais e demonstrativos, sem fins comerciais.
Desenvolvido com ❤️ em Python para explorar o poder das APIs da OpenAI.

🤖 OpenAI Prompt Executor — conectando ideias humanas à inteligência artificial.

yaml
Copy code

---

Deseja que eu adicione **badges** (como "Feito em Python", "Usa OpenAI API", "Versão 1.0") e um **screenshot estilizado** da execução no terminal (com emojis e destaque de resposta)? Isso deixaria o README ainda mais atraente no GitHub.






