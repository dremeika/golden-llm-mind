import argparse
import json
import os
import time
import azure.cognitiveservices.speech as speechsdk


parser = argparse.ArgumentParser(
    description='Transcribe episode')
parser.add_argument(
    'audio_file', metavar='audio_file', type=str,
    help='File path of the episode audio file')


class BinaryFileReaderCallback(speechsdk.audio.PullAudioInputStreamCallback):
    def __init__(self, filename: str):
        super().__init__()
        self._file_h = open(filename, "rb")

    def read(self, buffer: memoryview) -> int:
        try:
            size = buffer.nbytes
            frames = self._file_h.read(size)
            buffer[:len(frames)] = frames
            return len(frames)
        except Exception as ex:
            print('Exception in `read`: {}'.format(ex))
            raise

    def close(self) -> None:
        try:
            self._file_h.close()
        except Exception as ex:
            print('Exception in `close`: {}'.format(ex))
            raise


def transcribe(audio_file: str) -> None:
    print(f"Transcribing audio '{audio_file}' using Azure Speech SDK")

    callback = BinaryFileReaderCallback(audio_file)
    format = speechsdk.audio.AudioStreamFormat(
        compressed_stream_format=speechsdk.AudioStreamContainerFormat.MP3)
    stream = speechsdk.audio.PullAudioInputStream(
        stream_format=format, pull_stream_callback=callback)

    speech_config = speechsdk.SpeechConfig(
        subscription=os.environ.get('AZURE_SUBSCRIPTION_KEY'),
        region=os.environ.get('AZURE_SERVICE_REGION'))
    speech_config.speech_recognition_language = 'lt-LT'
    speech_config.request_word_level_timestamps()
    speech_config.enable_dictation()

    audio_config = speechsdk.audio.AudioConfig(stream=stream)

    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config)

    with open(audio_file.replace('.mp3', '.txt'), 'a') as text_file:
        finished = False

        def stop_recognition_callback(event):
            print(f"Recognition Stopped: [{event}]")
            nonlocal finished
            finished = True

        def recognized_callback(event):
            data = json.loads(event.result.json)
            text = data['DisplayText']
            offset_ms = data['Offset'] / 10000
            print(f"Recognized: [{text}] starting at [{offset_ms / 1000}] sec.")
            text_file.write(text + '\n')
            text_file.flush()

        speech_recognizer.session_started.connect(
            lambda evt: print(f"Recognition Started: [{evt}]"))
        speech_recognizer.session_stopped.connect(
            lambda evt: print(f"Recognition Stopped: [{evt}]"))
        speech_recognizer.recognized.connect(recognized_callback)
        speech_recognizer.session_stopped.connect(stop_recognition_callback)
        speech_recognizer.canceled.connect(stop_recognition_callback)

        speech_recognizer.start_continuous_recognition()
        while not finished:
            time.sleep(.5)
        speech_recognizer.stop_continuous_recognition()


if __name__ == '__main__':
    audio_file = parser.parse_args().audio_file
    transcribe(audio_file)
