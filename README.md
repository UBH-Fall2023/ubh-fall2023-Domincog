# Developer Documentation

## Overview

This project's function is to record and transcribe audio in real time, analyze the transcribed text for validity, and use text-to-speech to clarify any misinformation detected.

## Modules and Functions

### `audio.py`

Responsible for audio capture and transcription.

- Functions:
  - `void record_audio(int duration, String output_path)`
    - Records live audio for a `duration` in seconds and saves it to `output_path`.
  - `String transcribe(String audio_path)`
    - Transcribes audio from `audio_path` into text and returns the string.

### `tts.py`

Manages conversion from text to speech and playing audio files.

- Functions:
  - `void text_to_wav(String text, String filename)`
    - Converts `text` into a TTS audio file and saves it to `filename`.
  - `void play_audio(String filename)`
    - Plays the audio file specified by `filename`.

### `validity.py`

Analyzes the transcribed text for validity and misinformation.

- Functions:
  - `Dictionary check_validity(String text)`
    - Analyzes `text` and returns a dictionary with validity status and misinformation details.

### `main.py`

Orchestrates the use of functions from `audio.py`, `tts.py`, and `validity.py` to form the full program workflow.

- Functions:
  - `void main()`
    - The entry point for the program to start the process.








# UB Hacking Fall 2023 Rules 
- Teams can consist of between 1 and 4 people.
- To have your submission be considered for judging, you must submit a 2-5 minute video along with your project. Try to keep it as concise as possible!
- The projects submitted for judging cannot have been started prior to the start of the hackathon. In other words, teams can plan their projects in great detail, but they cannot begin writing code until they arrive at the hackathon.
- Additionally, we are partnering with MLH this year, which means that our hackers must follow their code of conduct which can be found below.
- Any and all resources used must be open source and specified in either the project, or the project description.
- Your project must be publically available and under source control in this repository.
- Prior to submitting to devpost, your project must be fully committed and pushed to this repository.
- The link to this repository must be available on your devpost submission.
- Projects can not have been submitted to another event, including other hackathons this weekend.
- [Code of Conduct](https://drive.google.com/file/d/1RH_TtRu6EOHSbOoiSj2h1Q4jswtVILzE/view)
- [MLH Code of Conduct](https://static.mlh.io/docs/mlh-code-of-conduct.pdf)
