from flask import Flask, render_template, request, redirect

app = Flask(__name__)

questions = ['Do you like Italian?', 'Do you like Japenese?', 'Do you like Mexican?', 'Do you like Indian?']

def load_answers():
    try:
        with open('survey_answers.txt', 'r') as file:
            return [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_answers(answers):
    with open('survey_answers.txt', 'a') as file:
        file.write(','.join(answers) + '\n')

answers = load_answers()

@app.route('/')
def index():
    return render_template('survey.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    user_answers = [request.form[f'question_{i}'] for i in range(len(questions))]
    save_answers(user_answers)
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('result.html', questions=questions, answers=answers)

if __name__ == '__main__':
    app.run( host="0.0.0.0", port=5000)
