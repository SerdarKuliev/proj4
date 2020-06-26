from googletrans import Translator

with open("text_4_translate.txt", "w", encoding='utf-8') as ser:
    with open("text_4.txt", "r", encoding='utf-8') as ser1:
        text=ser1.read()
    ser.write(Translator().translate(text, dest='ru').text)