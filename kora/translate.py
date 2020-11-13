"""
Google Translate
"""

import os
os.system('pip install googletrans')

from googletrans import Translator
translator = Translator()


def to_en(text):
    t = translator.translate(text, dest='en')
    return t.text

def to_th(text):
    t = translator.translate(text, dest='th')
    return t.text

def many(texts, to='th'):
    translations = translator.translate(texts, dest=to)
    return [t.text for t in translations]
