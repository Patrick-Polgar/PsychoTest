""" psycho_app """

from flask import Flask, render_template, request, jsonify
from calculate_result import calculate_result

app = Flask(__name__)

# Define the list of questions
questions = [
	"1. What do you think, do you know yourself good enough?",
    "2. Do you enjoy to speak with many people?",
    "3. Do you like to speak about your emotions with your friends?",
    "4. Are you an optimist?",
    "5. Do you like to be in a community?",
    "6. Do you like to share your ideas with others?",
    "7. Do you like to play with the children?",
    "8. Do you hate to read everyday alone?",
    "9. Do you like to walk among people on the street?",
    "10.Do you think, being alone for a long time is boring?"
]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        answers = request.form
        result = calculate_result(answers)
    return render_template("home.html", questions=questions, result=result)

@app.route('/show_result', methods=['POST'])
def show_result():
    answers = {}
    data = request.form
    for i in range(0, 10):
        answer = data.get(questions[i])
        if answer:
            answers[str(i)] = answer
    result = calculate_result(answers)
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
