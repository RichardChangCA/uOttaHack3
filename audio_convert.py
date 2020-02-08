from pdb import set_trace
from utils import convert_mp3_to_wav
from speech_recognition import AudioFile , Recognizer
import speech_recognition as sr


def speech_recog(file_name="input_sample/audio/introduction_ml.mp3", duration=10):
    convert_mp3_to_wav("input_sample/audio/introduction_ml.mp3")

    result = 0

    class_audio = AudioFile("input_sample/audio/introduction_ml.wav")
    set_trace()
    recongizer = Recognizer()

    with class_audio as src_audio:
        audio = recongizer.record(src_audio, duration=duration)
        print(recongizer.recognize_google(audio))

speech_recog()