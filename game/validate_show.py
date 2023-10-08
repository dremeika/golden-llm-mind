import argparse
import re

from model import R1Question, R2Question, R3Question, R4Question

parser = argparse.ArgumentParser(
    description='Validate episode text file')
parser.add_argument(
    'episode_file', metavar='episode_file', type=str,
    help='Path to the episode text file')


def parse_round1(round1_match: re.Match) -> list[R1Question]:
    return []


def parse_round2(round1_match: re.Match) -> list[R2Question]:
    return []


def parse_round3(round1_match: re.Match) -> list[R3Question]:
    return []


def parse_round4(round1_match: re.Match) -> list[R4Question]:
    return []


def validate(episode_file: str) -> None:
    print(f"Validating episode file '{episode_file}'")

    with open(episode_file, 'r') as f:
        text = f.read()

    url = re.match(r"^URL:\s*(\S+)\s*$", text, re.MULTILINE).group(1)
    print(f"URL: {url}")

    round1_match = re.match(r".+I turas\n(.*)\nII turas.+", text, re.DOTALL)
    round1_questions = parse_round1(round1_match)

    round2_match = re.match(r".+II turas\n(.*)\nIII turas.+", text, re.DOTALL)
    round2_questions = parse_round2(round2_match)

    round3_match = re.match(r".+III turas\n(.*)\nIV turas.+", text, re.DOTALL)
    round3_questions = parse_round3(round3_match)

    round4_match = re.match(r".+IV turas\n(.*)$", text, re.DOTALL)
    round4_questions = parse_round4(round4_match)


if __name__ == '__main__':
    validate(parser.parse_args().episode_file)
