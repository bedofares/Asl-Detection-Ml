# import the module
import speech_recognition as sr




# initialize the recognizer
recognizer = sr.Recognizer()
textList = list()



def speechRecg():
    while True:
        try:
            with sr.Microphone() as mic:
                # clear background noise
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                print("Start Recording........")
                # capture the audio
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text.lower()
                textList.append(text)
                print(f"Recognized : {text}")
                if text == "stop please":
                    print("Thank you for using our app")
                    joined_string = " ".join(textList)
                    print("Whole transcript : " , textList)
                    print(joined_string)
                    break;

        except sr.UnknownValueError:  # error: recognizer does not understand
            print('I did not get that')
            continue
        except sr.RequestError:
            print('Sorry, the service is down')  # error: recognizer is not connected
            continue

speechRecg()
