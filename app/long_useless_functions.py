import json


def digit(s):
    s1 = ''
    for i in range(len(s)):
        if s[i].isdigit() or s[i] == '.':
            s1 += s[i]
    return s1


def totaldigit(s):
    s1 = ''
    for a in s:
        if '0123456789'.find(a) != -1:
            s1 += a
    return int(s1)


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
    count = 0
    for a in data[log]['tasks_done']:
        if a:
            count += 1
    return count


def get_page(log):
    with open('app/person_data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    return data[log]['page']


def change_tasks(log, page_no):
    with open('app/person_data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)

    tasks = data[log]['tasks_done']
    task_no = totaldigit(page_no) - 1

    while len(tasks) <= task_no + 1:
        tasks.append(0)

    tasks[task_no] = 1

    with open('app/person_data.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(data, ensure_ascii=False))


def change_page(log, page):
    with open('app/person_data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    data[log]['page'] = page
    with open('app/person_data.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(data, ensure_ascii=False))