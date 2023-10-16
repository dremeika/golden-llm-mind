
from model import Player, R1Answer, R1Question


class GPT35Player(Player):

    def play(self, question: R1Question) -> R1Answer:
        raise NotImplementedError()
