import requests
import json
from consts import *
from typing import Literal, Union


def TextToSpeech(inputText: str, lang:SUPPORTED_LANGS_TYPE_EXP = "es") -> str:
    '''
    TextToSpeech converts text to speech and returns the url of the audio file

    ### Parameters
    ----------
    | Name | Type | Description |
    | :--- | :--- | :--- |
    | inputText | str | The text to convert to speech |

    ----------
    ### Returns
    -------
    str
        The url of the audio file
    '''
    T2S_API_URL = "https://ttsmp3.com/makemp3_new.php"
    parceText = inputText.replace(" ", "%20")
    payload = "msg=" + parceText + "&lang=" + LANG_REQ_CONFIG[lang] + "&source=ttsmp3"
    "&lang=Matthew&source=ttsmp3"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
    }
    response = requests.request(
        "POST", T2S_API_URL, data=payload, headers=headers)
    jsonResponse = json.loads(response.text)
    return jsonResponse["URL"]

def DownloadAudioFile(url: str, filename: str, path: str = "") -> None:
    '''
    DownloadAudioFile downloads the audio file from the url and saves it to the specified path

    ### Parameters
    ----------
    | Name | Type | Description |
    | :--- | :--- | :--- |
    | url | str | The url of the audio file to download |
    | | | |
    | filename | str | The name of the file to save the audio file as |
    | | | |
    | path | str, optional | The path to save the audio file to, by default "" |

    ----------
    ### Returns
    -------
    None
    '''
    audio = requests.get(url)

    with open(path + filename + ".mp3", "wb") as f:
        f.write(audio.content)