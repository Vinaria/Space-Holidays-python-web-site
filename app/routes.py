from flask import render_template, request, send_from_directory
from app import app
from app.pages_data import *
from app.answers_data import *


@app.route('/')
@app.route('/index')
def root():
    return render_template('index.html')


@app.route('/pages/<page_no>/')
def handle_pages(page_no):
    if page_no not in pages.keys():
        return 'Error 404', 404
    return render_template('page.html', page=pages[page_no])


@app.route('/static/<path:file>')
def get_images(file):
    return send_from_directory(app.static_folder, file)


@app.route('/pages/<task>', methods=['post', 'get'])
def answer_check(task):
    answer = request.form.get('answer')

    if answer == answers[task]:
        return render_template('result.html', result=True)
    else:
        return render_template('result.html', result=False)






