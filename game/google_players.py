from model import Player, R4Question, R4Answer, R3Question, R3Answer, R2Question, R2Answer, R1Question, R1Answer

from langchain.llms import VertexAI
from langchain.prompts import PromptTemplate

q1_prompt = PromptTemplate.from_template("""Klausimas: {question}
Atsakymo variantai: {options}
Atsakymas: """)


class VertexAIPlayer(Player):

    def __init__(self) -> None:
        self.llm = VertexAI(model_name='text-bison', temperature=0)

    def play_round1(self, question: R1Question) -> R1Answer:
        chain = q1_prompt | self.llm
        result = chain.invoke({'question': question.question, 'options': "\n".join(question.options)})
        return R1Answer(question=question, answer=result.strip())

    def play_round2(self, question: R2Question, used_hints: list[str]) -> R2Answer:
        pass

    def play_round3(self, question: R3Question, query: str) -> R3Answer:
        pass

    def play_round4(self, question: R4Question) -> R4Answer:
        pass
