import keyboard
from consts import *
from AudioUtil import playAudio
import os
from time import sleep


def individualCallback(x: keyboard.KeyboardEvent, wd: str, lang:SUPPORTED_LANGS_TYPE_EXP) -> None:
    if(x.name is not None and x.name in LANG_TO_QWERTY_KEYS[lang]):
        playAudio(f"{wd}\\{x.name}.mp3")
        sleep(0.1)

def individualCallback2(key: str, wd: str, lang:SUPPORTED_LANGS_TYPE_EXP) -> None:
    print(key, end="\r")
    if(key in LANG_TO_QWERTY_KEYS[lang]):
        if(key == "ñ"):
            key = "nn"
        filename = wd + "\\" + key + ".mp3"
        playAudio(filename)
        #playAudio(f"{wd}\\{key}.mp3")

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



     