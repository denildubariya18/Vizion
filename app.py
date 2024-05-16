from readingscreen import *
from flask import Flask, redirect, render_template

app = Flask(__name__)
braille=''
text=''
@app.route('/')
def starting():
    return render_template('index.html', braille=braille, text=text)


@app.route('/imagetobraille')
def imagetoBraille():
    global braille
    global text
    text=ImageToText()
    braille=TextToBraille()
    return redirect('/')


@app.route('/speechtobraille')
def speechToBraille():
    global text
    global braille
    text=SpeechToText()
    braille= TextToBraille()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
    