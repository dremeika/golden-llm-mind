import argparse
import os
import re
import shutil

import requests


parser = argparse.ArgumentParser(
    description='Download "Auksinis protas" episode')
parser.add_argument(
    'url', metavar='url', type=str,
    help='URL of the episode on https://www.lrt.lt/')


def main() -> None:
    if shutil.which('cvlc') is None:
        print("VLC is not installed. Exiting...")
        exit(1)

    episode_url = parser.parse_args().url
    print(f"Episode URL: '{episode_url}'")
    recording_url_match = re.search(r'(/mediateka/irasas/\d+)', episode_url)
    if recording_url_match is None:
        print("URL is not valid. Exiting...")
        exit(1)
    recording_url = recording_url_match.group(0)
    print(f"Recording URL: '{recording_url}'")

    video_info = requests.get(
        f"https://www.lrt.lt/servisai/stream_url/vod/media_info/?url={recording_url}").json()
    print(f"Episode title: '{video_info['title']}'")
    video_playlist_url = video_info['playlist_item']['file']
    print(f"Episode playlist: {video_playlist_url}")

    audio_file_name = recording_url.replace('/', '_').strip('_') + '.mp3'
    print(f"Downloding episode audio to '{audio_file_name}'")
    vlc_command = f"""cvlc {video_playlist_url} --no-sout-video --sout-audio --sout="#transcode{{acodec=mp3,ab=320,channels=1,samplerate=48000}}:std{{access=file,mux=raw,dst={audio_file_name}}}" vlc://quit"""
    print(f"Executing VLC command: '{vlc_command}'")
    os.system(vlc_command)


if __name__ == '__main__':
    main()
