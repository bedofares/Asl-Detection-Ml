import pyttsx3

def WriteText():
    writtenText = input('Write text here')
    return writtenText

def speakText(command):
    # Use female voice
    voice_id_female = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    # Use male voice
    voice_id_male = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"

    engine = pyttsx3.init()

    # set speech rate/frequency
    engine.setProperty('rate', 100)
    # engine.setProperty('volume', 1)
    # voices = engine.getProperty('voices')

    # set voice gender
    engine.setProperty('voice', voice_id_female)

    engine.say(command)
    # run and wait method, it processes the voice commands.
    engine.runAndWait()

speakText(WriteText())
