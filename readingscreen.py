import speech_recognition as sr
import pyttsx3
import cv2
import mss
import numpy
import pytesseract
import pyttsx3


def ImageToText():
    mon = {'top': 180, 'left': 0, 'width': 1600, 'height': 800}
    with mss.mss() as sct:
        im = numpy.asarray(sct.grab(mon))
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(im)
        fp = open("txt.txt", "w+")
        fp.write(text)
        fp.close()
        return text


def TextToBraille():
    file = open("txt.txt", "r")
    text = file.read()
    file.close()
    braille_map = {
        'a': '⠁',
        'b': '⠃',
        'c': '⠉',
        'd': '⠙',
        'e': '⠑',
        'f': '⠋',
        'g': '⠛',
        'h': '⠓',
        'i': '⠊',
        'j': '⠚',
        'k': '⠅',
        'l': '⠇',
        'm': '⠍',
        'n': '⠝',
        'o': '⠕',
        'p': '⠏',
        'q': '⠟',
        'r': '⠗',
        's': '⠎',
        't': '⠞',
        'u': '⠥',
        'v': '⠧',
        'w': '⠺',
        'x': '⠭',
        'y': '⠽',
        'z': '⠵',
        '1': '⠼⠁',
        '2': '⠼⠃',
        '3': '⠼⠉',
        '4': '⠼⠙',
        '5': '⠼⠑',
        '6': '⠼⠋',
        '7': '⠼⠛',
        '8': '⠼⠓',
        '9': '⠼⠊',
        '0': '⠼⠚',
        '!': '⠖',
        '(': '⠶',
        ')': '⠶',
        '-': '⠤',
        '{': '⠸⠜',
        '[': '⠶⠠',
        ']': '⠶⠠',
        '}': '⠸⠜',
        ':': '⠒',
        ';': '⠆',
        ',': '⠂',
        '.': '⠲',
        '/': '⠌',
        '?': '⠦',
        ' ': ' ',
        '\n': '\n'
    }
    final_string = ""
    for char in text:
        char = char.lower()
        if char in braille_map:
            final_string += braille_map[char]
        else:
            continue

    print(final_string)
    file = open("braille.txt", "w+", encoding="utf-8")
    file.write(final_string)
    return final_string


def SpeechToText():
    r = sr.Recognizer()
    MyText = ""

    def SpeakText(command):
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.1)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            SpeakText(MyText)
            fp = open("txt.txt", "w+")
            fp.write(MyText)
            fp.close()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")
    return MyText
