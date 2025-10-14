🤖 OpenAI Prompt Executor - Projeto Python

Este projeto demonstra como usar a API da OpenAI para executar um prompt e receber uma resposta automática de um modelo de linguagem como o GPT-3.5-Turbo.

⚙️ Configuração
1. 📦 Instalar dependências

Crie um arquivo requirements.txt com o conteúdo:

openai


Em seguida, instale as dependências:

pip install -r requirements.txt

2. 🔐 Configurar chave da API da OpenAI

Você precisa de uma chave de API válida para autenticação.

🔑 Passo 1 — Obter a chave

Acesse o painel da OpenAI e gere uma nova chave:
👉 https://platform.openai.com/api-keys

🧭 Passo 2 — Configurar variável de ambiente

Windows (CMD ou PowerShell):

setx OPENAI_API_KEY "sua-chave-secreta-aqui"


Feche e reabra o terminal após definir a variável.

macOS / Linux:

export OPENAI_API_KEY="sua-chave-secreta-aqui"


Para tornar permanente, adicione essa linha ao arquivo ~/.bashrc ou ~/.zshrc.

🚀 Executar o Projeto

Execute o script principal no terminal:

python executar_prompt.py


O script enviará um prompt de exemplo para a API e exibirá a resposta diretamente no console.

✨ Funcionalidades

✅ Conexão Segura: Usa variáveis de ambiente para gerenciar a chave da API.
🧩 Função Modular: A lógica está encapsulada na função executar_prompt_openai().
🛡️ Tratamento de Erros: Usa try...except para capturar erros de conexão ou autenticação.
💬 Compatível com GPT-3.5 e GPT-4.
📘 Exemplo pronto para uso.

📁 Estrutura do Projeto
openai-prompt-executor/
├── executar_prompt.py     # 🧠 Script principal de execução
└── requirements.txt       # 📋 Dependências Python

🧠 Exemplo de Saída
Enviando prompt para a OpenAI...

--- Resposta da OpenAI ---
A distância média da Terra até a Lua é de aproximadamente 384.400 km.
---------------------------

🧰 Solução de Problemas
❌ Erro: invalid_api_key (401)

🔍 Verifique:

Se a variável OPENAI_API_KEY está configurada corretamente

Se a chave não expirou

Reinicie o terminal

❌ Erro: insufficient_quota (429)

💰 Motivo: Conta sem créditos disponíveis
✅ Solução: Adicione um método de pagamento em
👉 https://platform.openai.com/account/billing

🔗 Links Úteis

📚 Documentação da API OpenAI

🔑 Gerenciar Chaves de API

💵 Faturamento e Créditos

🐍 Biblioteca OpenAI Python (GitHub)

📜 Licença

Este projeto foi desenvolvido para fins educacionais e demonstração.
Sinta-se livre para adaptar e expandir conforme necessário.

✨ OpenAI Prompt Executor — explorando o poder da IA com Python 🚀
