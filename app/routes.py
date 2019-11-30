from flask import render_template, request, send_from_directory
from app import app
from app.pages_data import *
from app.answers_data import *

tasks_amount = int(0)


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

    if answer == answers[page_no]:
        tasks_amount += 1
        return render_template('result.html', check_result=True, tasks_amount = tasks_amount, page=pages[page_no])
    else:
        return render_template('result.html', check_result=False, tasks_amount = tasks_amount, page=pages[page_no])


@app.route('/sign/<to_do>')
def sign_up(to_do):
    return render_template('account.html', to_do=to_do)








