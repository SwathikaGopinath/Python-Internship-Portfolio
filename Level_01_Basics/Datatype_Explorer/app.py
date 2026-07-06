from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        string_value = request.form["string"]
        integer_value = int(request.form["integer"])
        float_value = float(request.form["float"])
        boolean_value = request.form["boolean"].lower() == "true"
        none_value = None

        results = {
            "String": (string_value, type(string_value).__name__),
            "Integer": (integer_value, type(integer_value).__name__),
            "Float": (float_value, type(float_value).__name__),
            "Boolean": (boolean_value, type(boolean_value).__name__),
            "None": (none_value, type(none_value).__name__)
        }

        return render_template("index.html", results=results)

    return render_template("index.html", results=None)


if __name__ == "__main__":
    app.run(debug=True)