class R1Question:

    def __init__(self, question: str, options: list[str], answer: str) -> None:
        self.question = question
        self.options = options
        self.answer = answer


class R2Question:

    def __init__(self, question: str, hints: list[str], answer: str) -> None:
        self.question = question
        self.answer = answer
        self.hints = hints


class R3Question:

    def __init__(self, question: str, choices: list[str], answers: list[tuple[str, str]]) -> None:
        self.question = question
        self.choices = choices
        self.answers = answers


class R4Question:

    def __init__(self, question: str, answer: str) -> None:
        self.question = question
        self.answer = answer
