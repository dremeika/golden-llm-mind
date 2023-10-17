from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
)

from model import Player, R1Answer, R1Question

q1_prompt_template = ChatPromptTemplate.from_messages([
    "Tu esi protmūšio dalyvis. Tavo užduotis yra atsakyti į klausimus",
    """
    Klausimas: {question}
    Atsakymo variantai: {options}
    Atsakymas: """
])


class GPT35Player(Player):

    def __init__(self) -> None:
        self.chat = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

    def play_round1(self, question: R1Question) -> R1Answer:
        prediction = self.chat(
            q1_prompt_template
            .format_prompt(question=question.question, options=", ".join(question.options))
            .to_messages())
        return R1Answer(question=question, answer=prediction.content)


class GPT4Player(Player):

    def __init__(self) -> None:
        self.chat = ChatOpenAI(temperature=0, model_name='gpt-4')

    def play_round1(self, question: R1Question) -> R1Answer:
        prediction = self.chat(
            q1_prompt_template
            .format_prompt(question=question.question, options=", ".join(question.options))
            .to_messages())
        return R1Answer(question=question, answer=prediction.content)
