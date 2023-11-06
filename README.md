# Golden LLM Mind

An experiment on how well LLMs could score in Lithuanian quiz
show ["Auksinis Protas"](https://www.lrt.lt/mediateka/video/auksinis-protas)

## LLM Competition Results

LLMs were competing in show aired on [2023-09-22](shows/2023-09-22.txt), [2023-05-29](shows/2023-05-29.txt), [2023-10-28](shows/2023-10-28.txt).

LLMs were scored a bit differently than human players:

- **Round 1**: 1 point for each correct answer
- **Round 2**: 4 points for a guess with 1 hint, 3 points for a guess with 2 hints, 2 points for a guess with 3 hints, 1
  point for a guess with 4 hints
- **Round 3**: 1 point for each correct answer and no point burning after incorrect guess
- **Round 4**: 1 point for each correct answer

### Results

|                                             | Show       | Round 1 | Round 2 | Round 3 | Round 4 | Total |
|---------------------------------------------|------------|---------|---------|---------|---------|-------|
| [GPT 4](results/2023-09-22-gpt-4.txt)       | 2023-09-22 | 6       | 11      | 53      | 1       | 71    |
| [GPT 3.5](results/2023-09-22-gpt-3.5.txt)   | 2023-09-22 | 3       | 9       | 44      | 1       | 57    |
| [PaLM 2](results/2023-09-22-bison-text.txt) | 2023-09-22 | 6       | 11      | 51      | 0       | 68    |
| [GPT 4](results/2023-05-29-gpt-4.txt)       | 2023-05-29 | 6       | 5       | 41      | 2       | 54    |
| [GPT 3.5](results/2023-05-29-gpt-3.5.txt)   | 2023-05-29 | 3       | 4       | 30      | 0       | 37    |
| [PaLM 2](results/2023-05-29-bison-text.txt) | 2023-05-29 | 5       | 8       | 37      | 1       | 51    |
| [GPT 4](results/2023-10-28-gpt-4.txt)       | 2023-10-28 | 8       | 12      | 39      | 2       | 61    |
| [GPT 3.5](results/2023-10-28-gpt-3.5.txt)   | 2023-10-28 | 4       | 5       | 36      | 1       | 46    |
| [PaLM 2](results/2023-10-28-bison-text.txt) | 2023-10-28 | 5       | 24      | 36      | 2       | 67    |

**Total**

| Model    | Score |
|----------|-------|
| GPT 4    | 186   |
| PaLM 2   | 186   |
| GPT 3.5  | 140   |

## Playing the Game

```commandline
cd game
poetry install
poetry run python play.py -e ../shows/2023-10-28.txt -r 1 -l palm
```
NOTE:
 - To play with GPT-3.5 or GPT-4, OpenAI API key need to be exported before playing: `export OPENAI_API_KEY="..."`
 - To play with PALM-2 via VertexAI, authentication to Google Cloud is required. For example `gcloud auth application-default login`


## Transcribing a Show

Detailed instructions on how to download and transcribe a show can be found in [Download & Transcribe](transcription/README.md).

## Golden Semiconductors Mind

![Golden LLM Mind](./golden-mind.jpg)
