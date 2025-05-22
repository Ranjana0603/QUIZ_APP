from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Load questions from JSON file
def load_questions():
    with open(os.path.join(app.root_path, 'questions.json'), 'r') as f:
        return json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/questions')
def get_questions():
    questions = load_questions()
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)
