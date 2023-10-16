import argparse

from episode_parser import parse_episode
from openai_players import GPT35Player


parser = argparse.ArgumentParser(
    description='Play "Auksinis protas" episode by LLM')
parser.add_argument(
    '-e', '--episode', required=True, type=str, help='Path to the episode text file')
parser.add_argument(
    '-r', '--round', required=True, type=int, choices=[1, 2, 3, 4], help='Round to play')
parser.add_argument(
    '-l', '--llm', required=True, type=str, choices=['gpt-3.5'], help='LLM to play with')

players = {
    'gpt-3.5': GPT35Player()
}


def main(episode_file: str, round: int, llm: str) -> None:
    print(f"Playing episode file '{episode_file}' round '{round}' with LLM '{llm}'")

    episode = parse_episode(episode_file)
    player = players[llm]

    if round == 1:
        for question in episode.round1:
            player.play(question)


if __name__ == '__main__':
    args = parser.parse_args()
    main(args.episode, args.round, args.llm)

