🤖 OpenAI Prompt Executor - Projeto Python
1. 📘 Visão Geral do Projeto

O OpenAI Prompt Executor é um projeto em Python desenvolvido para demonstrar como conectar-se à API da OpenAI, enviar prompts e receber respostas automáticas de modelos de linguagem como o GPT-3.5-Turbo ou GPT-4.

O projeto tem como foco fins educacionais, servindo como base para integrar recursos de IA generativa em aplicações Python de forma segura, modular e reutilizável.

2. 🎯 Objetivos do Projeto

O projeto foi desenvolvido com os seguintes objetivos:

Demonstrar a autenticação e uso da API da OpenAI.

Exibir exemplos de requisições seguras usando variáveis de ambiente.

Implementar tratamento de erros para lidar com falhas de rede ou autenticação.

Fornecer um exemplo prático e reutilizável para estudantes e desenvolvedores.

Facilitar a integração de modelos GPT em scripts e aplicações Python.

3. 🧩 Estrutura do Projeto

Abaixo está a estrutura de diretórios e arquivos principais do projeto:

openai-prompt-executor/
├── executar_prompt.py     # 🧠 Script principal que executa o prompt
└── requirements.txt       # 📋 Lista de dependências Python

4. ⚙️ Configuração do Ambiente
4.1 📦 Instalar Dependências

Crie um arquivo chamado requirements.txt com o seguinte conteúdo:

openai


Em seguida, instale as dependências executando:

pip install -r requirements.txt

4.2 🔐 Configurar a Chave da API da OpenAI

Para autenticar sua aplicação, é necessário configurar sua chave de API.
Você pode obtê-la em:
🔑 https://platform.openai.com/api-keys

💻 Windows (CMD ou PowerShell)
setx OPENAI_API_KEY "sua-chave-secreta-aqui"


Feche e reabra o terminal após definir a variável.

🐧 macOS / Linux
export OPENAI_API_KEY="sua-chave-secreta-aqui"


Para manter permanente, adicione esta linha ao arquivo ~/.bashrc ou ~/.zshrc.

5. 🚀 Executando o Projeto

Após configurar o ambiente e a chave da API, execute o script principal:

python executar_prompt.py


O script enviará um prompt de exemplo para o modelo da OpenAI e exibirá a resposta no console.

6. 🧠 Código Principal (executar_prompt.py)
import os
from openai import OpenAI

def executar_prompt_openai(prompt):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro ao executar o prompt: {e}"

if __name__ == "__main__":
    prompt = "Explique de forma simples o que é aprendizado de máquina."
    print("Enviando prompt para a OpenAI...\n")
    resposta = executar_prompt_openai(prompt)
    print("--- Resposta da OpenAI ---")
    print(resposta)
    print("---------------------------")

7. 💬 Exemplo de Saída
Enviando prompt para a OpenAI...

--- Resposta da OpenAI ---
Aprendizado de máquina é um ramo da inteligência artificial que permite que sistemas aprendam padrões a partir de dados, sem serem programados explicitamente.
---------------------------

8. 🛠️ Solução de Problemas (Troubleshooting)
❌ Erro: invalid_api_key (401)

Esse erro ocorre quando a chave de API está incorreta ou ausente.

✅ Soluções:

Gere uma nova chave no painel da OpenAI.

Verifique se a variável de ambiente foi configurada corretamente.

Feche e reabra o terminal após definir a variável.

❌ Erro: insufficient_quota (429)

Esse erro indica falta de créditos na conta da OpenAI.

✅ Soluções:

Verifique sua conta em: OpenAI Billing

Adicione um método de pagamento ativo.

Crie uma nova conta se seus créditos de teste expiraram.

9. 📚 Recursos e Links Úteis
Recurso	Link
📘 Documentação da API OpenAI	https://platform.openai.com/docs

🔑 Página de Chaves de API	https://platform.openai.com/api-keys

💳 Faturamento (Billing)	https://platform.openai.com/account/billing

🐍 Biblioteca OpenAI para Python	https://github.com/openai/openai-python
10. 👨‍💻 Autor

OpenAI Prompt Executor foi desenvolvido com fins educacionais e demonstrativos, para auxiliar desenvolvedores a integrar IA em seus projetos Python.

✨ Explorando o poder da IA com Python — de forma simples, modular e segura! 🚀