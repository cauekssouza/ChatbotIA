# Chatbot IA com Feedback Inteligente

## Descrição
Este projeto é um **chatbot com IA** desenvolvido em Python e Streamlit, que integra:
- **LLM (Gemini API)** para geração de respostas inteligentes
- **Vector Store (ChromaDB)** para armazenamento e recuperação de contexto
- **Sistema de feedback em tempo real** para melhoria contínua do prompt
- **Ferramentas externas via API** (ViaCEP e PokéAPI)

O objetivo é demonstrar habilidades em desenvolvimento de interfaces, integração com APIs, uso de vector stores e orquestração de agentes.

---

## Funcionalidades
- Chat interativo com histórico visível
- Feedback do usuário sobre respostas (Boa, Regular, Ruim)
- Atualização dinâmica do prompt com base nos feedbacks
- Visualização do prompt atual e histórico de versões
- Botões para limpar histórico de chat, feedbacks e prompts
- Integração com APIs externas:
  - **ViaCEP**: consulta de CEP
  - **PokéAPI**: dados de Pokémon (incluindo tipos)

---

## Tecnologias
- **Python 3.12**
- **Streamlit** 
- **Gemini API** 
- **ChromaDB** 
- **Docker** + **docker-compose**
- **Requests**

---

             

# Local
1. Crie um ambiente virtual:
python -m venv venv
source venv/bin/activate   
venv\Scripts\activate      

2. Instale as dependências:
pip install -r requirements.txt

3. Crie um arquivo .env com sua chave:
GEMINI_API_KEY=coloque_sua_chave_aqui

4. Execute o projeto:
streamlit run app/main.py

5. Acessar em: http://localhost:8501

---


# Docker
1. Crie o arquivo .env com sua chave:
GEMINI_API_KEY=coloque_sua_chave_aqui

2. Crie arquivo Dockerfile e docker-compose.yml

3. execute docker compose up --build

4. Acessar em: http://localhost:8501

---

# Teste Unitários
Este projeto inclui testes automatizados para validar funcionalidades essenciais, como:

Integração com a API do ViaCEP

Integração com a PokéAPI

Sistema de feedback e atualização de prompt

Integração com o LLM (Gemini)

---

# Executando os testes
1. Ative seu ambiente virtual:
source venv/bin/activate   
venv\Scripts\activate      

2. Execute os testes com pytest

3. Exemplo de teste para PokéAPI:
from app.tools import consultar_pokemon

def test_consultar_pokemon():
    result = consultar_pokemon("pikachu")
    assert "nome" in result
    assert "altura" in result
    assert "peso" in result

3. Exemplo de teste para ViaCEP:
from app.tools import consultar_cep

def test_consultar_cep():
    result = consultar_cep("01001-000")
    assert "cep" in result
    assert result["cep"] == "01001-000"
    assert "localidade" in result

---

# Critérios atendidos
Chat com LLM (Gemini)

Feedback em tempo real

Vector Store (ChromaDB)

APIs externas (ViaCEP, PokéAPI)

Dockerização

Testes unitários

Documentação clara

---

## 📄 Licença
Este projeto está licenciado sob a licença MIT.  
Você pode usar, copiar, modificar e distribuir livremente, desde que mantenha o aviso de direitos autorais e a licença original.

