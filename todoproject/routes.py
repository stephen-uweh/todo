import os
from todoproject import app, db
from flask import jsonify, request, Flask, make_response
from todoproject.models import Todo
import uuid

@app.route('/all')
def all():
    todo_list = Todo.query.all()
    data = []
    for todo in todo_list:
        todo_data = {}
        todo_data['id'] = todo.id
        todo_data['due'] = todo.due
        todo_data['state'] = todo.state
        todo_data['description'] = todo.description
        data.append(todo_data)
    return jsonify({'Todo': data})


@app.route('/todo/<id>', methods=['GET'])
def todo(id):
    todo = Todo.query.filter_by(id=id).first()
    if not todo:
        return jsonify({'Message': 'Not Found'},404)
    data = {}
    data['id'] = todo.id
    data['due'] = todo.due
    data['state'] = todo.state
    data['description'] = todo.description
    return jsonify({'Product' : data})


@app.route("/todo/add", methods=['POST'])
def add_todo():
    data = request.get_json()
    todo = Todo(due=data['due'], state='pending',description=data['description'])
    db.session.add(todo)
    db.session.commit()
    return jsonify({'Message' : 'Todo added'}, 200)


@app.route('/todo/<id>/edit', methods=['POST'])
def edit_todo(id):
    todo = Todo.query.filter_by(id=id).first()
    data = request.get_json()
    if 'due' in data:
        todo.due = data['due']
    if 'state' in data:
        todo.state = data['state']
    if 'description' in data:
        todo.description = data['description']
    db.session.commit()
    return jsonify({'Message': 'Todo updated'})

@app.route('/todo/<id>/cancel', methods=['POST'])
def cancel_todo(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.state = 'Cancelled'
    db.session.commit()
    return jsonify({'Message': 'Todo cancelled'})


@app.route('/todo/<id>/complete', methods=['POST'])
def complete_todo(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.state = 'Done'
    db.session.commit()
    return jsonify({'Message': 'Todo completed'})


@app.route("/todo/<id>/delete", methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.filter_by(id=id).first()
    if not todo:
        return jsonify({'Message': 'Not Found'},404)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'Message' : 'Todo has been deleted'})