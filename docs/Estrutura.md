# Estrutura do projeto

``` console
📁 /medassist/
│
├── app/
│   ├── models/          # Estrutura dos dados
│   ├── services/        # Lógica de negócio
│   ├── routes/          # Rotas da API
│   ├── tasks/           # Agendamentos e automações
│   ├── whatsapp/        # Integração com WhatsApp
│   └── utils/           # Helpers
│
├── db/                  # Conexão com banco
├── .env                 # Variáveis de ambiente (Twilio, Mongo, etc.)
├── requirements.txt
└── main.py              # Início da aplicação

```