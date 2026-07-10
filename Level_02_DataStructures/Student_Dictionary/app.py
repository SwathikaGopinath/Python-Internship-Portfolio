from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    keys = ["name", "age", "grade", "subject"]
    student = {}

    for key in keys:
        student[key] = request.form.get(key)

    # Update Grade
    student["grade"] = request.form.get("updated_grade")

    # Add Passed
    student["passed"] = True

    return render_template("result.html", student=student)


if __name__ == "__main__":
    app.run(debug=True)