import pyaudio
import wave
import ffmpeg
import os

def record_and_convert_audio():
    # Create a PyAudio instance.
    pa = pyaudio.PyAudio()

    # Open a stream for recording.
    stream = pa.open(
        format=pyaudio.FORMAT_PCM16,
        channels=1,
        rate=44100,
        input=True
    )

    # Create a wave file for storing the recording.
    wf = wave.open("recording.wav", "wb")
    wf.setnchannels(1)
    wf.setframerate(44100)

    # Start recording.
    for i in range(10):
        stream.read(44100)

    # Stop recording.
    stream.stop_stream()
    stream.close()

    # Close the wave file.
    wf.close()

    # Convert the WAV file to an MP3 file.
    audiofile = "recording.mp3"
    input_wav = "recording.wav"
    (
        ffmpeg.input(input_wav)
        .output(audiofile)
        .run(overwrite_output=True)
    )
    # Return the path to the generated MP3 file
    return audiofile

if __name__ == "__main__":
    audio_file_path = record_and_convert_audio()
    print(f"Audio file saved at: {audio_file_path}")