from flask import render_template, request, send_from_directory
from app import app
from app.pages_data import *
from app.answers_data import *
import json
import os

tasks_amount = 0


def digit(s):
    s1 = ''
    for i in range(len(s)):
        if s[i].isdigit() or s[i] == '.':
            s1 += s[i]
    return s1


def exists(log, pas):
    with open('app/person_data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)

    if (log in data) and (pas in data[log['password']]):
        return True
    else:
        return False


@app.route('/')
@app.route('/index')
def root():
    return render_template('index.html')


@app.route('/pages/<page_no>/')
def handle_pages(page_no):
    global tasks_amount
    if page_no not in pages.keys():
        return 'Error 404', 404
    return render_template('page.html', page=pages[page_no], tasks_amount=tasks_amount)


@app.route('/static/<path:file>')
def get_images(file):
    return send_from_directory(app.static_folder, file)


@app.route('/pages/<page_no>/giving_answer', methods=['POST', 'get'])
def answer_check(page_no):
    global tasks_amount
    answer = request.form.get('answer')
    answer = digit(answer)

    if answer == answers[page_no]:
        tasks_amount += 1
        return render_template('result.html', check_result=True, tasks_amount=tasks_amount, page=pages[page_no], answered=True)
    else:
        return render_template('result.html', check_result=False, tasks_amount=tasks_amount, page=pages[page_no])


@app.route('/signup', methods=['POST', 'GET'])
def registration():
    login = request.form.get('log')
    pas1 = request.form.get('pas1')
    pas2 = request.form.get('pas2')

    with open('app.person_data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)

    if pas1 == pas2 and login not in data:
        data.add(login['password'])
        data[login['password']] = pas1

        with open('person_data.json', 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(data, ensure_ascii=False))

        return render_template('regist_result.html', result=True)
    else:
        return render_template('regist_result.html', result=False)


@app.route('/signin', methods=['POST', 'GET'])
def sign_in():
    login = request.form.get('log')
    pas = request.form.get('pas')

    if exists(login, pas):

        return render_template('index.html', registered=True)
    else:
        return render_template('cant_sign_in.html')
