from translate import Translator
import time

while 1:
    text = input('请输入英文：')
    translator = Translator(to_lang='zh')
    translation = translator.translate(text)
    print(translation)

