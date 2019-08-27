from googletrans import Translator

def Translation(msg, dest='en'):
    translator = Translator()
    translation = translator.translate(msg, dest)
    return translation.text
