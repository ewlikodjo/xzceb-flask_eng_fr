"""
#from machinetranslation import translator
from machinetranslation.translator import english_to_french, french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to French"


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to English"


@app.route("/")
def renderIndexPage():
    # Write the code to render template


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
"""

from flask import Flask, render_template, request
from machinetranslation.translator import english_to_french, french_to_english

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=['POST'])
def englishToFrench():
    textToTranslate = request.form['textToTranslate']
    translatedText = english_to_french(textToTranslate)
    return translatedText

@app.route("/frenchToEnglish", methods=['POST'])
def frenchToEnglish():
    textToTranslate = request.form['textToTranslate']
    translatedText = french_to_english(textToTranslate)
    return translatedText

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
