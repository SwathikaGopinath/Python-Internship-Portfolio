from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    results = None

    if request.method == "POST":

        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])

      
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        power = num1 ** num2

        try:
            division = num1 / num2
            floor_division = num1 // num2
            modulus = num1 % num2

        except ZeroDivisionError:
            division = "Cannot divide by zero"
            floor_division = "Cannot divide by zero"
            modulus = "Cannot divide by zero"

        results = {
            "Addition": addition,
            "Subtraction": subtraction,
            "Multiplication": multiplication,
            "Division": division,
            "Floor Division": floor_division,
            "Modulus": modulus,
            "Power": power
        }

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)