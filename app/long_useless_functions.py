import json


def digit(s):
    s1 = ''
    for i in range(len(s)):
        if s[i].isdigit() or s[i] == '.':
            s1 += s[i]
    return s1


def exists(log, pas):
    with open('app/person_data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    if log in data:
        if pas == data[log]['password']:
            return True
        return False
    else:
        return False


def get_tasks(log):
    with open('app/person_data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    return data[log]['tasks_done']


def get_page(log):
    with open('app/person_data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    return data[log]['page']


def change_tasks(log):
    with open('app/person_data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    data[log]['tasks_done'] += 1
    with open('app/person_data.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(data, ensure_ascii=False))


def change_page(log, page):
    with open('app/person_data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    data[log]['page'] = page
    with open('app/person_data.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(data, ensure_ascii=False))