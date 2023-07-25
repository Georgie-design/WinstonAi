import sys
sys.path.insert(0, r'C:\Users\georg\Downloads\WinstonAi\ai_assistant')
from psutil import NoSuchProcess
import psutil
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
from main import winstonAi
import subprocess




def is_process_running(script_path):
    process_name = os.path.basename(script_path)
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        if process.info['cmdline'] is not None and process_name in process.info['cmdline']:
            return True
    return False

def start_process(script_path):
    try:
        subprocess.Popen(["python", script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
        print(f"{script_path} is now turned on.")
    except Exception as e:
        print(f"Error starting {script_path}: {e}")

def stop_process(script_path):
    process_name = os.path.basename(script_path)
    try:
        for process in psutil.process_iter(['pid', 'name', 'cmdline']):
            if process.info['cmdline'] is not None and process_name in process.info['cmdline']:
                subprocess.run(["TASKKILL", "/F", "/PID", str(process.info['pid'])])
                print(f"{process_name} is now turned off.")
                return
        print(f"No running process found for {process_name}.")
    except Exception as e:
        print(f"Error stopping {process_name}: {e}")





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\georg\Downloads\WinstonAi\data\databases\database.db'


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
        if request.form.get('start_winston') == 'on':
            if not is_process_running("main.py"):
                start_process("main.py")
            return render_template('winstonOn.html')
        elif request.form.get('stop_winston') == 'off':
            if is_process_running("main.py"):
                stop_process("main.py")
            return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/winstonOn', methods=['GET'])
def winston_on():
    return render_template('winstonOn.html')


# Your other routes and code...




















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
        return 'There was a problem deleting your song'

@app.route('/issues')
def issues():
    return render_template('issues.html')

if __name__ == "__main__":
    app.run(debug=True)
