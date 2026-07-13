from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    unique_words = []
    duplicate_count = None

    if request.method == "POST":

        sentence = request.form["sentence"]

        words = sentence.split()

        unique_words = list(set(words))

        duplicate_count = len(words) - len(unique_words)

    return render_template(
        "index.html",
        unique_words=unique_words,
        duplicate_count=duplicate_count
    )


if __name__ == "__main__":
    app.run(debug=True)