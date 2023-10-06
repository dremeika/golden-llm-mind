# Validates that show text file is in correct format.

import argparse


parser = argparse.ArgumentParser(
    description='Validate episode text file')
parser.add_argument(
    'episode_file', metavar='episode_file', type=str,
    help='Path to the episode text file')


def validate(eipisode_file: str) -> None:
    print(f"Validating episode file '{eipisode_file}'")


if __name__ == '__main__':
    validate(parser.parse_args().episode_file)
