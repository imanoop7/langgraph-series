from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field



class Reflection(BaseModel):
    missing : str = Field(description="Critique of what is missing")
    superfloous : str = Field(description="Critique of what is superfloous")


class AnswerQuestion(BaseModel):
    answer : str = Field(description="250 word detailed answer to the question.")
    reflection : Reflection = Field(description="Your Reflection on the intial answer")
    search_quires: List[str] = Field(description="1-3 seach for researching improvements to address the critique of your current answer.")



class ReviseAnswer(AnswerQuestion):
    refernce: List[str] = Field(description="Citations moticating your updated answer")
    
    
     