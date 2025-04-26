from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
def get_questions():
    conn =  sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    conn.close()
    return questions
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/quiz",methods=["GET","POST"])
def quiz():
    questions = get_questions()
    if request.method == "POST":
        score = 0
        for q in questions:
            selected = request.form.get(f"question{q[0]}")
            if selected and int(selected) == q[6]:
                score += 1
        return redirect(url_for('result',score=score,total=len(questions)))
    return render_template("quiz.html",questions=questions)
@app.route("/result")
def result():
    score = request.args.get('score', type=int)
    total = request.args.get('total', type=int)
    return render_template("result.html",score=score,total=total)

if __name__ =="__main__":
    app.run(debug=True)