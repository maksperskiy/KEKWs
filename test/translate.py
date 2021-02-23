import goslate

text = "Hello World"

gs = goslate.Goslate()
translatedText = gs.translate(open('101Dalmatians.srt'), 'ru')

translation = '\n'.join(translatedText)

print(translation)