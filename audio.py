# запись с микрофона
import speech_recognition as sr
r = sr.Recognizer()
print(sr.__version__)
task = ""
while task != "пока":
    with sr.Microphone as source:
        audio = r.listen(source)
        task = r.recognize_google(audio, language='RU-ru').lower()
        print(task)
    input()


# for device_index in sr.Microphone.list_working_microphones():
#     m = sr.Microphone(device_index=device_index)
#     print(m)
#     break
# else:
#     print("No working microphones found!")
# import pyaudio
# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     print(p.get_device_info_by_index(i)['name'])


# print(sr.Microphone)
# list_mic = sr.Microphone.list_microphone_names()
# for i in range(0, len(list_mic)):
#     print(i, list_mic[i])

# mic = sr.Microphone(device_index=1)

# obtain audio from the microphone
r = sr.Recognizer()
# with mic as source:
#     print("Скажите число А!")
#     audio = r.listen(source)
# try:
#     a = r.recognize_google(audio, language='ru-RU')
#     print("Google Speech Recognition thinks you said " + a)
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))
