#Tradutor de textos em Python

from translate import Translator

s = Translator(from_lang="CHOOSE A LANGUAGE",to_lang="CHOOSE A LANGUAGE")

res = s.translate("PUT THE TEXT HERE")

print(res)
