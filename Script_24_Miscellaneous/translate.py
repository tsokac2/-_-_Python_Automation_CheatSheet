from googletrans import Translator

translator = Translator()

translation = translator.translate('Oa ,ai oe?', dest='en').text

print(translation)