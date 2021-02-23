# -*- coding: utf8 -*-

import pysrt
import json
import translate_splitting as tr


def gen_sub(sub_srt, translated_text):
    count = 0
    subs = []
    for i in range(len(sub_srt)):
        text = tr.remove_chars(sub_srt[i].text).split()
        text_ru = translated_text[count:(count + len(text))]
        text_ru_full = translated_text[i]
        time_start = time_to_float(sub_srt[i].start)
        time_end = time_to_float(sub_srt[i].end)
        sub = {
            'text': text,
            'text_ru': text_ru,
            'text_ru_full': text_ru,
            'time_start': time_start,
            'time_end': time_end
        }
        count = count + len(text)
        subs.append(sub)
    return subs


def write_json(sub_dict, name):
    with open(name[0:-3] + 'json', 'w', encoding='utf-8') as file:
        json.dump(sub_dict, file, indent=1, ensure_ascii=False)


def time_to_float(time):
    return time.seconds + 60 * time.minutes + 3600 * time.hours + time.milliseconds / 1000


def run(sub_name):
    write_json(gen_sub(pysrt.open(sub_name),
                       tr.translation(pysrt.open(sub_name))),
               sub_name)


if __name__ == "__main__":
    run('104.srt')
