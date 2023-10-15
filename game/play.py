import argparse


parser = argparse.ArgumentParser(
    description='Play "Auksinis protas" episode by LLM')
parser.add_argument(
    '-e', '--episode', required=True, type=str, help='Path to the episode text file')
parser.add_argument(
    '-r', '--round', required=True, type=int, choices=[1, 2, 3, 4], help='Round to play')
parser.add_argument(
    '-l', '--llm', required=True, type=str, choices=['gpt-3.5'], help='LLM to play with')


def main(episode_file: str, round: int, llm: str) -> None:
    print(f"Playing episode file '{episode_file}' round '{round}' with LLM '{llm}'")


if __name__ == '__main__':
    args = parser.parse_args()
    main(args.episode, args.round, args.llm)