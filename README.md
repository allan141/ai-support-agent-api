# AI Support Agent API

API inteligente para atendimento automatizado de clientes, desenvolvida com FastAPI e hospedada na Microsoft Azure.

---

## Sobre o projeto

O AI Support Agent API simula um sistema moderno de suporte ao cliente, capaz de:

- Receber tickets de atendimento  
- Classificar mensagens automaticamente por categoria  
- Detectar urgência do problema  
- Gerar respostas automáticas com IA  
- Armazenar dados em banco relacional e NoSQL  
- Exibir métricas operacionais  

Projeto desenvolvido com foco em portfólio profissional para vagas de Backend, Full Stack, Cloud e IA.

---

## Tecnologias Utilizadas

### Backend

- Python  
- FastAPI  
- Uvicorn  
- Gunicorn  

### Banco de Dados

- Azure PostgreSQL Flexible Server  
- MongoDB Atlas  

### Inteligência Artificial

- Scikit-Learn  
- Hugging Face API  

### Cloud / DevOps

- Microsoft Azure App Service  
- GitHub  
- GitHub Actions  

---

## Deploy Online

### API

https://ai-support-agent-api-allan-drabbbbhbqf8fbb6.brazilsouth-01.azurewebsites.net

### Swagger Docs

https://ai-support-agent-api-allan-drabbbbhbqf8fbb6.brazilsouth-01.azurewebsites.net/docs

---

## Funcionalidades

### Criar Ticket

**POST** `/tickets`

#### Request

```json
{
  "customer_id": 1,
  "message": "Meu pedido está atrasado e ninguém responde"
}
```

#### Response

```json
{
  "id": 1,
  "customer_id": 1,
  "message": "Meu pedido está atrasado e ninguém responde",
  "category": "logistica",
  "urgency": "alta"
}
```

---

### Análise Inteligente

**POST** `/agent/analyze`

Analisa a mensagem e retorna:

- Categoria  
- Urgência  
- Resposta automática  

---

### Métricas

**GET** `/metrics`

```json
{
  "total_tickets": 5,
  "urgent_tickets": 4,
  "categories": {
    "logistica": 4,
    "suporte_tecnico": 1
  }
}
```

---

## Estrutura do Projeto

```txt
app/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── mongo.py
├── ai_agent.py
├── ml_classifier.py
└── rpa.py
```

---

## Diferenciais do Projeto

- Projeto real hospedado em nuvem  
- Integração com IA  
- Banco SQL + NoSQL  
- API documentada  
- Estrutura profissional  
- Aplicação pronta para escalar  

---

## Objetivo

Demonstrar habilidades práticas em:

- Desenvolvimento Backend  
- APIs REST  
- Cloud Computing  
- Inteligência Artificial aplicada  
- Banco de dados  
- Deploy em produção  

---

## Autor

**Allan Arthur Cavalcante**

GitHub:  
https://github.com/allan141

LinkedIn:  
https://www.linkedin.com/in/allancavalcante-dev/
