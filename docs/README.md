# 💊 RPA de Controle de Medicamentos Pessoais

Este projeto é um sistema de automação com Python para controle pessoal de medicamentos. Ele realiza scraping de preços em farmácias online, armazena informações em MongoDB e AWS S3, envia lembretes por e-mail e oferece um dashboard via Flask. A estrutura é pensada para expansão futura com análises de preços e previsões de gastos.

## ========= EM CONSTRUÇÃO =========

## 📁 Estrutura do Projeto

```
rpa_medicamentos/
├── scraping/            # Scripts para buscar preços de medicamentos
│   └── buscar_precos.py
├── db/                  # Conexões com MongoDB e AWS S3
│   ├── mongo_connect.py
│   └── s3_utils.py
├── scripts/             # Automação de lembretes por e-mail
│   ├── lembrete_email.py
│   └── agendador.py
├── dashboard/           # Mini API com Flask
│   └── flask_app.py
├── data/                # Arquivo JSON de medicamentos cadastrados
│   └── medicamentos.json
├── .env                 # Variáveis de ambiente (MongoDB, AWS, e-mail)
├── main.py              # Execução principal (scraping + salvamento)
└── README.md
```

---

## ⚙️ Funcionalidades

* 🔎 Web Scraping de preços em farmácias (ex: Ultrafarma)
* 🗓️ Armazenamento de dados em MongoDB
* ☁️ Upload de receitas ou documentos médicos para AWS S3
* 📧 Envio de lembretes de medicamentos por e-mail
* 🌐 API em Flask para exibir medicamentos cadastrados
* 📊 Estrutura pronta para dashboards e análise de preços

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/rpa_medicamentos.git
cd rpa_medicamentos
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # ou venv\\Scripts\\activate no Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Se não tiver um `requirements.txt`, crie com:

```bash
pip freeze > requirements.txt
```

### 4. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz com as seguintes variáveis:

```env
MONGO_URI=mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net
AWS_ACCESS_KEY=SEU_ACESSO
AWS_SECRET_KEY=SUA_CHAVE
```

### 5. Execute o script principal

```bash
python main.py
```

---

## 🧲 Exemplos de uso

* Buscar preços de “dipirona 500mg” e salvar no banco
* Visualizar medicamentos no browser via `localhost:5000/medicamentos`
* Enviar lembretes automáticos com `agendador.py`

---

## 📊 Futuras melhorias

* Dashboards em Streamlit, Dash ou Power BI
* Previsão de gastos com Prophet ou regressão
* Análise de farmácias mais baratas por medicamento
* Interface web com login para cuidadores
* Integração com Google Calendar ou WhatsApp

---

## 📌 Requisitos

* Python 3.9+
* MongoDB Atlas (gratuito)
* AWS S3 (plano Free Tier)
* Conta de e-mail com SMTP (ex: Gmail)
* Familiaridade básica com web scraping e automações

---

## 🧠 Contribuição

Este projeto é pessoal, mas colaborações são bem-vindas para torná-lo mais robusto e completo!

---

## 👨‍💻 Autora

Michelle Sanseverino
[LinkedIn](https://www.linkedin.com/in/michelle-sanseverino) | [GitHub](https://github.com/michellesanseverino)
