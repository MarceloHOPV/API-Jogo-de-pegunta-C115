# Guia de Uso do Software de Perguntas e Respostas

Este guia explica como configurar e usar o software de perguntas e respostas baseado em **FastAPI**. Ele cobre desde a instalação das dependências até a interação com o servidor, onde o cliente pode enviar respostas para as questões.

## 1. Instalação das Dependências

### 1.1. **Clonando o Repositório**

Primeiro, clone o repositório do projeto:

```bash
git clone <URL_do_repositório>
cd <nome_do_repositório>
```

# 1.2. Criando e Ativando um Ambiente Virtual
(Opcional se não quiser pule para o passo 1.3)

```bash
python -m venv env
```
## Ative o Ambiente virtual
 No windows
 ```bash
.\env\Scripts\activate
```
Se não der certo tente sem o ponto

No mac
```bash
source env/bin/activate
```

# 1.3. Instalando as Dependências
```bash
pip install -r requirements.txt
```

# 2. Executando o Servidor
```bash
uvicorn API:app --reload
```

# Guia de Uso do Software de Perguntas e Respostas

Este guia explica como configurar e usar o software de perguntas e respostas baseado em **FastAPI**. Ele cobre desde a instalação das dependências até a interação com o servidor, onde o cliente pode enviar respostas para as questões.

## 3. Interagindo com o Servidor

### 3.1. **Obter as Perguntas Usando o Swagger UI**

A maneira mais simples de interagir com a API é através da interface do **Swagger UI** fornecida pelo FastAPI. Para acessar a interface, siga os passos abaixo:

1. **Execute o servidor FastAPI**:
    - Primeiro, inicie o servidor usando o comando:
    ```bash
    uvicorn API:app --reload
    ```

2. **Abra a interface Swagger UI**:
    - No seu navegador, acesse a URL:
    ```
    http://127.0.0.1:8000/docs
    ```

3. **Obtendo as Perguntas**:
    - Na interface do Swagger UI, você verá a documentação da API.
    - Clique no endpoint `GET /questions/{start_index}`.
    - Após isso, insira o índice **`0`** no campo `start_index` e clique em **"Try it out!"**.
    - O servidor retornará as 3 primeiras perguntas sem o campo `is_correct`.
    - Caso queira ver outra perguntas pode colocar o index 3 pois existem 6 perguntas no software

**Exemplo de Resposta:**
```json
[
    {
        "question_text": "0️⃣ Qual a menor unidade de memória em um computador?",
        "choices": [
            {"choice_text": "Bit"},
            {"choice_text": "Byte"},
            {"choice_text": "Palavra (Word)"},
            {"choice_text": "Registrador"}
        ]
    },
    {
        "question_text": "1️⃣ Qual é a memória mais rápida em um computador?",
        "choices": [
            {"choice_text": "Registrador"},
            {"choice_text": "Cache"},
            {"choice_text": "RAM"},
            {"choice_text": "Disco Rígido"}
        ]
    },
    {
        "question_text": "2️⃣ Qual destas linguagens de programação é compilada?",
        "choices": [
            {"choice_text": "Python"},
            {"choice_text": "C++"},
            {"choice_text": "JavaScript"},
            {"choice_text": "PHP"}
        ]
    }
]
```

## 3.2. Enviar as Respostas Usando o Swagger UI

Após o cliente responder as perguntas, ele pode **enviar as respostas** através do Swagger UI.

1. **No Swagger UI**, encontre o endpoint `POST /submit_answers`.
2. Clique em **"Try it out!"**.
3. No campo de entrada, insira as respostas no seguinte formato:

### Formato do JSON:
```json
[
    {"question_id": 0, "answer": "Bit"},
    {"question_id": 1, "answer": "Registrador"},
    {"question_id": 2, "answer": "C++"}
]


