
import re
from model import R1Question, R2Question, R3Question, R4Question


def parse_url(text: str) -> str:

    url_match = re.match(r"^URL:\s*(\S+)\s*$", text, re.MULTILINE)
    if url_match is None:
        raise ValueError("URL not found")
    return url_match.group(1)


def parse_round1(text: str) -> list[R1Question]:

    round1_pattern = r".+I turas\n(.*)\nII turas.+"
    round1_match = re.match(round1_pattern, text, re.DOTALL)
    if round1_match is None:
        raise ValueError("Round 1 not found")
    round1_text = round1_match.group(1)

    block_pattern = r"(K: .+?A: .+?)\n\n"
    block_matches = re.findall(block_pattern, round1_text, re.DOTALL)

    result = []
    for block in block_matches:
        question_pattern = r"K:\s*(.+?)\n"
        options_pattern = r"\w\)\s*(.+?)\n"
        answer_pattern = r"A:\s*(.+?)$"

        question = re.search(question_pattern, block).group(1)
        options = re.findall(options_pattern, block)
        answer = re.search(answer_pattern, block).group(1)

        result.append(R1Question(question, options, answer))
    return result


def parse_round2(text: str) -> list[R2Question]:

    round2_match = re.match(r".+II turas\n(.*)\nIII turas.+", text, re.DOTALL)
    if round2_match is None:
        raise ValueError("Round 2 not found")
    round2_text = round2_match.group(1)
    return []


def parse_round3(text: str) -> list[R3Question]:

    round3_match = re.match(r".+III turas\n(.*)\nIV turas.+", text, re.DOTALL)
    if round3_match is None:
        raise ValueError("Round 3 not found")
    round3_text = round3_match.group(1)
    return []


def parse_round4(text: str) -> list[R4Question]:

    round4_match = re.match(r".+IV turas\n(.*)$", text, re.DOTALL)
    if round4_match is None:
        raise ValueError("Round 4 not found")
    round4_text = round4_match.group(1)
    return []