import argparse
from consts import *
from Callbacks import defineCallbacks
from DownloadLang import isLangLoaded, loadLang
import keyboard


def main():
    # posible arguments to pass to the program:
    # -h, --help show this help message and exit
    # -l, --lang language to use Suporting: es or en right now

    parser = argparse.ArgumentParser("This is a program to help blind people to learn to write with the keyboard")
    parser.add_argument("-l", "--lang", help="language to use", default="es")
    # parser.add_argument("-h", "--help", help="show this help message and exit", action="store_true")

    args = parser.parse_args()
    lang = args.lang.lower()

    if lang not in SUPPORTED_LANGS:
        print(f"Language {lang} not supported")
        return
    
    if not isLangLoaded(lang):
        loadLang(lang)
    
    defineCallbacks(lang)

    print("Press ESC to exit")
    keyboard.wait("esc")

if __name__ == "__main__":
    main()