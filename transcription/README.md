# Download & Transcribe

## Requirements

VLC for downloading stream to audio file:

`sudo apt install vlc libgstreamer1.0-0`

Poetry for Python:

[https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)


## Setup

`poetry install`

## Downloading an episode

Episodes can be found in https://www.lrt.lt/mediateka/video/auksinis-protas

Downloading one episode as audio file: 

`poetry run python transcription/download.py "https://www.lrt.lt/mediateka/irasas/2000275675/auksinis-protas-kelintais-metais-kauno-zalgirio-arena-perkope-milijono-lankytoju-riba"` 

Will download to `mediateka_irasas_2000275675.mp3`

## Transcribing an episode

Transcription is done using Azure Speech SDK. To use the API environment variables `AZURE_SUBSCRIPTION_KEY` and `AZURE_SERVICE_REGION` must be set. Read [Speech Service documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/get-started-speech-to-text) on how to obtain them. 

Transcribing the downloaded episode:

```bash
export AZURE_SUBSCRIPTION_KEY="your key"
export AZURE_SERVICE_REGION="your service region"
poetry run python transcription/transcribe.py mediateka_irasas_2000295122.mp3
```

After running for the lenght of the episode it will produce `mediateka_irasas_2000295122.txt`. The file will be appended during the time and can be used for reading.