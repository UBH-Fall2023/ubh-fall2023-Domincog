import pyaudio
import wave
import openai

def record_audio(duration, file_path):
    # Create a PyAudio instance.
    pa = pyaudio.PyAudio()

    # Open a stream for recording.
    stream = pa.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        input=True,
        frames_per_buffer=1024
    )

    # Create a wave file for storing the recording.
    wf = wave.open(file_path, "wb")
    wf.setnchannels(1)
    wf.setsampwidth(pa.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)

    # Start recording.
    frames_per_buffer = 1024
    n_buffers = duration * 44100 // frames_per_buffer
    for i in range(n_buffers):
        data = stream.read(frames_per_buffer)
        wf.writeframes(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    pa.terminate()  # Terminate the PyAudio instance

    # Close the wave file.
    wf.close()

    # Return the path to the WAV file, no conversion to MP3
    return file_path


def transcribe(file_path):
    # Get the OpenAI API key from the environment variable.
    openai.api_key = "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"

    # Read the audio file and transcribe it using OpenAI.
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            model="whisper-1", 
            file=audio_file
        )
    
    return transcript


def main():
    audio_file_path = "recording.wav"
    # Record audio and save as WAV file
    record_audio(10, audio_file_path)
    # Transcribe the audio file
    transcription = transcribe(audio_file_path)
    print(transcription)

if __name__ == "__main__":
    main()
