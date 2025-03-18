from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from API import BaseModel
from typing import List

from pydantic import BaseModel
from typing import List

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool = None  # 'is_correct' será removido para exibição

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]
