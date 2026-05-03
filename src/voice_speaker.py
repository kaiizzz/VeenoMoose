from TTS.api import TTS
import sounddevice as sd

# Load a good model
tts = TTS(model_name="tts_models/en/vctk/vits")

text = "Hello Kai, this is a much more natural voice."

# Generate speech
audio = tts.tts(text)

# Play it
sd.play(audio, samplerate=22050)
sd.wait()