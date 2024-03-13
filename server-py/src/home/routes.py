from src.home import home
from flask import Flask, render_template, request, url_for, redirect
from src.extensions import mongo

@home.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        mongo.db.todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('home.index'))

    all_todos = mongo.db.todos.find()
    return render_template('index.html', todos=all_todos)

@home.route('/result', methods=('GET', 'POST'))
def result():
    all_todos = mongo.db.todos.find()
    return render_template('index.html', todos=all_todos)