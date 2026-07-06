from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        sentence = request.form["string"]

        result = {
            "Uppercase": sentence.upper(),
            "Lowercase": sentence.lower(),
            "Title Case": sentence.title(),
            "Character Count": len(sentence),
            "Word Count": len(sentence.split()),
            "Reversed": sentence[::-1]
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)