import sys
sys.path.insert(0, r'C:\Users\georg\Downloads\WinstonAi\ai_assistant')


from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.root_path = os.path.dirname(os.path.abspath(__file__))  # Specify the app root path
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #main.winstonAi()
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/songs', methods=['POST', 'GET'])
def songs():
    if request.method == 'POST':
        # Check if a file was submitted
        if 'song_file' not in request.files:
            return 'No file part'

        song_file = request.files['song_file']

        # If the user submits an empty form without selecting a file
        if song_file.filename == '':
            return 'No selected file'

        # Check if the file has an allowed extension (in this case, only .mp3 files are allowed)
        if song_file and song_file.filename.endswith('.mp3'):
            # Save the file to a specific folder, e.g., 'static/songs'
            filename = secure_filename(song_file.filename)
            song_file.save(os.path.join(app.root_path, 'Songs', filename))

            # Save the filename or any other information related to the file in the database if needed
            # For simplicity, I'll only store the filename in the 'content' field of the Todo model.
            task_content = filename
            new_task = Todo(content=task_content)

            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/songs')

            except:
                return 'There was an issue adding your task'

        else:
            return 'Invalid file format. Only .mp3 files are allowed.'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('songs.html', tasks=tasks)
    

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)


    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/songs')
    except:
        return 'There was a problem deleting you'

@app.route('/issues')
def issues():
    return render_template('issues.html')

if __name__ == "__main__":
    app.run(debug=True)
