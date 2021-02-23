# -*- coding: utf8 -*-

import re
import pysrt
import goslate


def translation(subs):
    gs = goslate.Goslate()
    subs_text = ''
    for sub in subs:
        subs_text = subs_text + ' ' + remove_chars(sub.text)
    subs_text = re.sub(r"[^A-Za-zА-Яа-я\s+\n+\d+]+", '', subs_text)
    subs_text = subs_text.lower().split()
    subs_text = ' .?. '.join(subs_text)
    subs_text = subs_text.replace('.?. the .?.', '.?. то .?.')
    subs_text = subs_text.replace('.?. an .?.', '.?. вышеуказанный .?.')
    subs_text = gs.translate(subs_text, 'ru')
    subs_text = subs_text.split("?")
    for i in range(len(subs_text)):
        subs_text[i] = subs_text[i].replace(".", '')
    return subs_text


def remove_chars(text):
    chars = ['- ', '§', '<i>', '<b>', '</i>', '</b>', '♪']
    for char in chars:
        text = text.replace(char, '')
    return text


if __name__ == '__main__':
    subs = pysrt.open('103.srt')
    translation(subs)
