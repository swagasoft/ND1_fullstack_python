from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import sys
#  Flask_APP=app.py flask run starting a flask app


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/postgres'
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    # completed = db.Column(db.Boolean, nullable=False)

    def __repr__(self) -> str:
        return f'<Todo {self.id}  {self.description}  >'

db.create_all()

@app.route('/')
def index():
    new_data =  Todo.query.all()
    print('See ', new_data)
    return render_template('index.html', data=new_data)


@app.route('/todos/create', methods=['POST'])
def create_todo():
    try:
        description = request.form.get('description','')
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo():
    pass