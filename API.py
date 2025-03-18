from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4, UUID
from Models import ChoiceBase, QuestionBase

app = FastAPI()

# Banco de dados fictício com as questões
db: List[QuestionBase] = [
    QuestionBase(
        question_text="0️⃣ Qual a menor unidade de memória em um computador?",
        choices=[
            ChoiceBase(choice_text="Bit", is_correct=True),
            ChoiceBase(choice_text="Byte", is_correct=False),
            ChoiceBase(choice_text="Palavra (Word)", is_correct=False),
            ChoiceBase(choice_text="Registrador", is_correct=False)
        ]
    ),
    QuestionBase(
        question_text="1️⃣ Qual é a memória mais rápida em um computador?",
        choices=[
            ChoiceBase(choice_text="Registrador", is_correct=True),
            ChoiceBase(choice_text="Cache", is_correct=False),
            ChoiceBase(choice_text="RAM", is_correct=False),
            ChoiceBase(choice_text="Disco Rígido", is_correct=False)
        ]
    ),
    QuestionBase(
        question_text="2️⃣ Qual destas linguagens de programação é compilada?",
        choices=[
            ChoiceBase(choice_text="Python", is_correct=False),
            ChoiceBase(choice_text="C++", is_correct=True),
            ChoiceBase(choice_text="JavaScript", is_correct=False),
            ChoiceBase(choice_text="PHP", is_correct=False)
        ]
    ),
    QuestionBase(
        question_text="3️⃣ Qual destas é uma linguagem de programação de baixo nível?",
        choices=[
            ChoiceBase(choice_text="Assembly", is_correct=True),
            ChoiceBase(choice_text="Python", is_correct=False),
            ChoiceBase(choice_text="JavaScript", is_correct=False),
            ChoiceBase(choice_text="Swift", is_correct=False)
        ]
    ),
    QuestionBase(
        question_text="4️⃣ O que é um Sistema Operacional?",
        choices=[
            ChoiceBase(choice_text="Um software que gerencia o hardware e os aplicativos", is_correct=True),
            ChoiceBase(choice_text="Um programa antivírus", is_correct=False),
            ChoiceBase(choice_text="Uma linguagem de programação", is_correct=False),
            ChoiceBase(choice_text="Uma ferramenta de edição de texto", is_correct=True)
        ]
    ),
    QuestionBase(
        question_text="5️⃣ Qual é o objetivo da virtualização em sistemas computacionais?",
        choices=[
            ChoiceBase(choice_text="Acelerar a CPU", is_correct=False),
            ChoiceBase(choice_text="Criar ambientes isolados para rodar diferentes sistemas", is_correct=True),
            ChoiceBase(choice_text="Aumentar a capacidade de armazenamento", is_correct=False),
            ChoiceBase(choice_text="Melhorar a conexão com a internet", is_correct=False)
        ]
    )
]

# Modelo para enviar respostas
class Answer(BaseModel):
    question_id: int
    answer: str

# Remover o campo is_correct das opções antes de enviar as questões para o cliente
from typing import List
from Models import ChoiceBase, QuestionBase

def remove_is_correct_from_choices(question: QuestionBase):
    # Criando uma nova instância da escolha, mas sem o campo 'is_correct'
    new_choices = [
        ChoiceBase(choice_text=choice.choice_text) for choice in question.choices
    ]
    # Retorna a questão com as novas escolhas, sem o campo 'is_correct'
    return QuestionBase(
        question_text=question.question_text,
        choices=new_choices
    )


# Endpoint para enviar 3 questões para o cliente
@app.get("/questions/{start_index}", response_model=List[QuestionBase])
async def get_questions(start_index: int):
    if start_index >= len(db):
        raise HTTPException(status_code=404, detail="No more questions.")
    
    # Envia 3 perguntas por vez sem o campo 'is_correct'
    questions_to_send = db[start_index:start_index + 3]
    return [remove_is_correct_from_choices(q) for q in questions_to_send]

# Endpoint para o cliente enviar suas respostas
@app.post("/submit_answers")
async def submit_answers(answers: List[Answer]):
    acertos = 0
    resultado = []

    for answer in answers:
        # Verifica se a resposta do cliente está correta
        question = db[answer.question_id]
        correct_answer = next((choice for choice in question.choices if choice.choice_text == answer.answer), None)

        if correct_answer and correct_answer.is_correct:
            acertos += 1
            resultado.append(f"Pergunta {answer.question_id + 1}: Correto ✅")
        else:
            resultado.append(f"Pergunta {answer.question_id + 1}: Errado ❌ (Correta: {next(choice.choice_text for choice in question.choices if choice.is_correct)})")

    return {
        "acertos": acertos,
        "resultado": resultado
    }
