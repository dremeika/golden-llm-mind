import argparse

from episode_parser import parse_url, parse_round1, parse_round2, parse_round3, parse_round4


parser = argparse.ArgumentParser(
    description='Validate episode text file')
parser.add_argument(
    'episode_file', metavar='episode_file', type=str,
    help='Path to the episode text file')


def validate(episode_file: str) -> None:
    print(f"Validating episode file '{episode_file}'")

    with open(episode_file, 'r') as f:
        text = f.read()

    url = parse_url(text)
    print(f"URL: {url}")

    round1_questions = parse_round1(text)
    print(f"Round 1 questions: {len(round1_questions)}")

    round2_questions = parse_round2(text)
    print(f"Round 2 questions: {len(round2_questions)}")

    round3_questions = parse_round3(text)
    print(f"Round 3 questions: {len(round3_questions)}")

    round4_questions = parse_round4(text)
    print(f"Round 4 questions: {len(round4_questions)}")


if __name__ == '__main__':
    validate(parser.parse_args().episode_file)
