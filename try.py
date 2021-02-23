import pysrt
import json
import goslate

subs = pysrt.open('101.srt')
gs = goslate.Goslate()


def gen_sub(current_sub):
    text = current_sub.text
    time_start = timestarttofloat(current_sub)
    time_end = timeendtofloat(current_sub)

    sub = {
        'text': text,
        'time_start': time_start,
        'time_end': time_end
    }

    return sub


def write_json(sub_dict):
    try:
        data = json.load(open('subs.json'))
    except:
        data = []

    data.append(sub_dict)

    with open('subs.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def timestarttofloat(time_s):
    return time_s.start.seconds + 60 * time_s.start.minutes + 3600 * time_s.start.hours + time_s.start.milliseconds / 1000


def timeendtofloat(time_s):
    return time_s.end.seconds + 60 * time_s.end.minutes + 3600 * time_s.end.hours + time_s.end.milliseconds / 1000


for i in range(len(subs)):
    write_json(gen_sub(subs[i]))
