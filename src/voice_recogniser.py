import speech_recognition as sr

class VoiceToText():
    def __init__(self, device_index=None):
        self.r = sr.Recognizer()

        self.r.dynamic_energy_threshold = True
        self.r.pause_threshold = 1.3
        self.r.non_speaking_duration = 0.3

        self.mic = sr.Microphone(device_index=device_index)

        print("Adjusting for ambient noise...")
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source, duration=2)

    def get_voice(self):
        while True:
            with self.mic as source:
                print("Waiting for speech...")
                audio = self.r.listen(source)  # ← blocks until you speak

            try:
                text = self.r.recognize_google(audio)
                print(f"You said: {text}")
                return text

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError:
                print("API unavailable")

if __name__ == "__main__":
    print(sr.Microphone.list_microphone_names())

    vtt = VoiceToText(device_index=1)  # try your Yeti GX
    vtt.get_voice()