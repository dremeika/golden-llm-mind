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
    for question in round1_questions:
        if (not question.question or len(question.options) != 3 or question.answer not in question.options):
            print(f"Invalid question: {question}")

    round2_questions = parse_round2(text)
    print(f"Round 2 questions: {len(round2_questions)}")
    for question in round2_questions:
        if (not question.question or len(question.hints) != 4 or not question.answer):
            print(f"Invalid question: {question}")

    round3_questions = parse_round3(text)
    print(f"Round 3 questions: {len(round3_questions)}")
    for question in round3_questions:
        invalid_choices = [a[1] for a in question.answers if a[1] not in question.choices]
        if (not question.question or len(question.choices) != 2 or len(question.answers) != 20 or invalid_choices):
            print(f"Invalid question: {question}")

    round4_questions = parse_round4(text)
    print(f"Round 4 questions: {len(round4_questions)}")
    for question in round4_questions:
        if (not question.question or not question.answer):
            print(f"Invalid question: {question}")


if __name__ == '__main__':
    validate(parser.parse_args().episode_file)
