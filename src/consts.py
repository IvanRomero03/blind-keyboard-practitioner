from typing import List, Dict, Literal, Union, Tuple
SUPPORTED_LANGS:List[str] = ["en", "es"]
SUPPORTED_LANGS_TYPE_EXP = Union[Literal["en"], Literal["es"]]

LANG_REQ_CONFIG:dict[SUPPORTED_LANGS_TYPE_EXP, str] = {
    "en": "Matthew",
    "es": "Mia"
}