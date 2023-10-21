from abc import ABC, abstractmethod


class R1Question:

    def __init__(self, question: str, options: list[str], answer: str) -> None:
        self.question = question
        self.options = options
        self.answer = answer

    def __str__(self) -> str:
        return f"Q: {self.question}\nO: {self.options}\nA: {self.answer}"


class R1Answer:

    def __init__(self, question: R1Question, answer: str) -> None:
        self.question = question
        self.answer = answer


class R2Question:

    def __init__(self, question: str, hints: list[str], answer: str) -> None:
        self.question = question
        self.answer = answer
        self.hints = hints

    def __str__(self) -> str:
        return f"Q: {self.question}\nH: {self.hints}\nA: {self.answer}"


class R2Answer:

    def __init__(self, question: R2Question, answer: str) -> None:
        self.question = question
        self.answer = answer


class R3Question:

    def __init__(self, question: str, choices: list[str], answers: list[tuple[str, str]]) -> None:
        self.question = question
        self.choices = choices
        self.answers = answers

    def __str__(self) -> str:
        return f"Q: {self.question}\nC: {self.choices}\nA: {self.answers}"


class R3Answer:

    def __init__(self, question: R3Question, answer: str) -> None:
        self.question = question
        self.answer = answer


class R4Question:

    def __init__(self, question: str, answer: str) -> None:
        self.question = question
        self.answer = answer

    def __str__(self) -> str:
        return f"Q: {self.question}\nA: {self.answer}"


class Episode:

    def __init__(self, url: str,
                 round1: list[R1Question], round2: list[R2Question],
                 round3: list[R3Question], round4: list[R4Question]) -> None:
        self.url = url
        self.round1 = round1
        self.round2 = round2
        self.round3 = round3
        self.round4 = round4


class Player(ABC):

    @abstractmethod
    def play_round1(self, question: R1Question) -> R1Answer:
        pass

    @abstractmethod
    def play_round2(self, question: R2Question, used_hints: list[str]) -> R2Answer:
        pass

    @abstractmethod
    def play_round3(self, question: R3Question, query: str) -> R3Answer:
        pass
