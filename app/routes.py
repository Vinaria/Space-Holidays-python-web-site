from flask import render_template, request, send_from_directory
from app import app
from app.pages_data import *
from app.answers_data import *
from app.long_useless_functions import *
import json
import os

tasks_amount = 0
login = ''
registered = False
page = '/'


@app.route('/')
@app.route('/index')
def root():
    return render_template('index.html', registered = registered, login = login, page=page)


@app.route('/pages/<page_no>/')
def handle_pages(page_no):
    global tasks_amount
    if page_no not in pages.keys():
        return "Couldn't find page(..", 404

    if login:
        change_page(login, page_no)

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
        if registered:
            change_tasks(login, page_no)
            tasks_amount = get_tasks(login)

        return render_template('answer_result.html', check_result=True, tasks_amount=tasks_amount, page=pages[page_no], answered=True)
    else:
        return render_template('answer_result.html', check_result=False, tasks_amount=tasks_amount, page=pages[page_no])


@app.route('/signup_page/')
def reg_page():
    return render_template('sign_up.html')


@app.route('/signin_page/')
def enter_page():
    return render_template('sign_in.html')


@app.route('/signup_page/signup', methods=['POST', 'GET'])
def registration():
    login = request.form.get('log')
    pas1 = request.form.get('pas1')
    pas2 = request.form.get('pas2')

    with open('app/person_data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)

    if pas1 == pas2 and not(login in data):
        data[login] = {'password': pas1, 'status': 'user', 'tasks_done': [], 'page': '/'}

        with open('app/person_data.json', 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(data, ensure_ascii=False))

        return render_template('regist_result.html', result=True)
    else:
        return render_template('regist_result.html', result=False)


@app.route('/signin_page/signin', methods=['POST', 'GET'])
def sign_in():
    log = request.form.get('log')
    pas = request.form.get('pas')

    global login, registered, tasks_amount, page

    if exists(log, pas):
        login = log
        tasks_amount = get_tasks(login)
        page = get_page(login)
        result = registered = True
    else:
        result = False

    return render_template('enter_result.html', result = result)
