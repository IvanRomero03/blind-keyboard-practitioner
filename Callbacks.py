import keyboard
from consts import *
import os
from time import sleep
from AudioUtil import TextToSpeech, DownloadAudioFile, playAudio


past:str = ""

def addToCache(key:str, lang:SUPPORTED_LANGS_TYPE_EXP) -> None:
    global past
    if(key == "space"):
        playAudio(os.getcwd() + "\\audio_files\\" + lang + "\\Util\\espacio.mp3")
        key = " "
        lastWord = past.split(" ")[-1]
        url = TextToSpeech(lastWord, lang)
        DownloadAudioFile(url, lastWord, os.getcwd() + "\\audio_files\\temp\\" + lang + "\\")
        past += key
        playAudio(os.getcwd() + "\\audio_files\\temp\\" + lang + "\\" + lastWord + ".mp3")
        os.remove(os.getcwd() + "\\audio_files\\temp\\" + lang + "\\" + lastWord + ".mp3")
        print(past, end="\r")
        return
        #Read past word
    if(key == "enter"):
        playAudio(os.getcwd() + "\\audio_files\\" + lang + "\\Util\\enter.mp3")
        #Read past sentence and clear cache
        url = TextToSpeech(past, lang)
        DownloadAudioFile(url, past, os.getcwd() + "\\audio_files\\temp\\" + lang + "\\")
        playAudio(os.getcwd() + "\\audio_files\\temp\\" + lang + "\\" + past + ".mp3")
        os.remove(os.getcwd() + "\\audio_files\\temp\\" + lang + "\\" + past + ".mp3")
        past = ""
        print(past, end="\r")
        return
    if(key == "backspace"):
        playAudio(os.getcwd() + "\\audio_files\\" + lang + "\\Util\\retroceso.mp3")
        past = past[:-1]
        print(past, end="\r")
        return
    past += key
    print(past, end="\r")


def individualCallback(x: keyboard.KeyboardEvent, wd: str, lang:SUPPORTED_LANGS_TYPE_EXP) -> None:
    if(x.name is not None and x.name in LANG_TO_QWERTY_KEYS[lang]):
        playAudio(f"{wd}\\{x.name}.mp3")
        sleep(0.1)

def individualCallback2(key: str, wd: str, lang:SUPPORTED_LANGS_TYPE_EXP) -> None:
    global past
    #print(, end="")
    addToCache(key, lang)
    if(key in LANG_TO_QWERTY_KEYS[lang]):
        if(key == "ñ"):
            key = "nn"
        filename = wd + "\\" + key + ".mp3"
        playAudio(filename)

def individualCallback3(key: str, wd: str, lang:SUPPORTED_LANGS_TYPE_EXP) -> None:
    global past
    print(key)
    addToCache(key, lang)

def defineCallbacks(lang: SUPPORTED_LANGS_TYPE_EXP) -> None:
    '''
    defineCallbacks defines the callbacks for each key in the language

    ### Parameters
    ----------
    | Name | Type | Description |
    | :--- | :--- | :--- |
    | lang | SUPPORTED_LANGS_TYPE_EXP | The language to define the callbacks for |

    ----------
    ### Returns
    -------
    None
    '''
    wd = os.getcwd()
    wd += "\\audio_files\\" + lang

    for key in LANG_TO_QWERTY_KEYS[lang]:
        #keyboard.add_hotkey(key, lambda: playAudio(wd + "\\" + key + ".mp3"))
        #keyboard.hook(lambda: playAudio(wd + "\\" + key + ".mp3"))
        #keyboard.hook_key(key, lambda: playAudio(wd + "\\" + key + ".mp3"))
        #keyboard.hook_key(key, lambda x: print(x.name))
        #keyboard.hook_key(key, lambda x: individualCallback(x, wd, lang))
        keyboard.add_hotkey(key, lambda x, y: individualCallback2(x, wd, lang), args=(key, "was pressed") )
    for key in ["space", "enter", "backspace"]:
        keyboard.add_hotkey(key, lambda x, y: individualCallback3(x, wd, lang), args=(key, "was pressed") )



     