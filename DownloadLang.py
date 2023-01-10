import os
from consts import *
from AudioUtil import TextToSpeech, DownloadAudioFile


def isLangLoaded(lang: SUPPORTED_LANGS_TYPE_EXP) -> bool:
    '''
    isLangLoaded checks if a language is loaded

    ### Parameters
    ----------
    | Name | Type | Description |
    | :--- | :--- | :--- |
    | lang | SUPPORTED_LANGS_TYPE_EXP | The language to check |

    ----------
    ### Returns
    -------
    bool
        True if the language is loaded, False otherwise
    '''

    wd = os.getcwd()
    if(os.path.isdir(wd + "\\audio_files\\" + lang)):
        return True
    return False

def loadLang(lang: SUPPORTED_LANGS_TYPE_EXP) -> None:
    '''
    loadLang loads a language

    ### Parameters
    ----------
    | Name | Type | Description |
    | :--- | :--- | :--- |
    | lang | SUPPORTED_LANGS_TYPE_EXP | The language to load |

    ----------
    ### Returns
    -------
    None
    '''

    if(isLangLoaded(lang)):
        print(f"Language {lang} already loaded")
        return
    wd = os.getcwd() + "\\audio_files\\"
    os.mkdir(wd + lang)
    for key in LANG_TO_QWERTY_KEYS[lang]:
        print(f"Downloading {key} audio file")
        src = TextToSpeech(key, lang)
        DownloadAudioFile(src, key, wd + lang + "\\")
    return