from typing import List, Literal, Union
SUPPORTED_LANGS:List[str] = ["en", "es"]
SUPPORTED_LANGS_TYPE_EXP = Union[Literal["en"], Literal["es"]]

LANG_REQ_CONFIG:dict[SUPPORTED_LANGS_TYPE_EXP, str] = {
    "en": "Matthew",
    "es": "Mia"
}

# TODO: Check US QWERTY keys
LANG_TO_QWERTY_KEYS:dict[SUPPORTED_LANGS_TYPE_EXP, List[str]] = {
    "es": [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
        "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
        "a", "s", "d", "f", "g", "h", "j", "k", "l", "ñ",
        "z", "x", "c", "v", "b", "n", "m"
    ], 
    "en": [
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
        "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
        "a", "s", "d", "f", "g", "h", "j", "k", "l",
        "z", "x", "c", "v", "b", "n", "m"
    ]
}