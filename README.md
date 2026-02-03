# API Nutricional com Gemini AI

Esta é uma API robusta desenvolvida com FastAPI que fornece informações nutricionais detalhadas de alimentos utilizando a inteligência artificial do Google Gemini. A API conta com um sistema de cache local em SQLite para otimizar a performance e reduzir chamadas externas.

## 🚀 Tecnologias

- **Python 3.12+**
- **FastAPI**: Framework web moderno e de alta performance.
- **SQLAlchemy**: ORM para persistência de dados.
- **SQLite**: Banco de dados leve para cache nutricional.
- **Google Generative AI (Gemini)**: Motor de IA para extração de dados nutricionais.
- **Pydantic**: Validação de dados e configurações.

## 📂 Arquitetura do Projeto

O projeto segue uma estrutura modular para facilitar a manutenção e escalabilidade:

```text
diet_api/
├── app/
│   ├── core/           # Configurações centrais (Banco de dados)
│   ├── models/         # Modelos do SQLAlchemy
│   ├── schemas/        # Esquemas de validação Pydantic
│   ├── services/       # Lógica de negócio e clientes de API externa
│   └── main.py         # Ponto de entrada da aplicação
├── .env                # Variáveis de ambiente (Segredos)
├── nutrition.db        # Banco de dados SQLite (Gerado automaticamente)
└── pyproject.toml      # Gerenciamento de dependências
```

## 🛠️ Configuração e Instalação

### 1. Clonar o repositório
```bash
git clone <url-do-repositorio>
cd diet_api
```

### 2. Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com sua chave da API do Gemini:
```env
GEMINI_API_KEY=SuaChaveAqui
```

### 3. Instalar dependências
Utilizando `pip`:
```bash
pip install fastapi uvicorn sqlalchemy google-generativeai python-dotenv
```

## 🏃 Como Executar

Para iniciar o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

## 📖 Documentação da API

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Exemplo de Uso

**Endpoint:** `GET /nutrition`

**Parâmetros:**
- `quantidade`: Ex: "100g", "2 colheres", "1 unidade"
- `alimento`: Nome do alimento (Ex: "frango", "maçã")

**Exemplo de Requisição:**
```bash
curl "http://127.0.0.1:8000/nutrition?quantidade=100g&alimento=banana"
```

## 🛡️ Funcionalidades

- **Cache Inteligente**: Antes de consultar a IA, a API verifica se o alimento e a quantidade já existem no banco de dados local.
- **Normalização**: As chaves de busca são normalizadas para evitar duplicidade no cache (ex: "Maçã" e "maçã" são tratados como o mesmo item).
- **Respostas em JSON**: A IA é instruída a responder estritamente em formato JSON para garantir a integridade dos dados.
