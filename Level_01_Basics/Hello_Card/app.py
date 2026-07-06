from flask import Flask, render_template, request

# Create the Flask application
app = Flask(__name__)


# Homepage
@app.route("/", methods=["GET", "POST"])
def home():

    # Initially no result
    message = None

    # When the form is submitted
    if request.method == "POST":

        # Get data from HTML form
        name = request.form["name"].title()
        age = int(request.form["age"])

        # Create the message
        message = (
            f"Hello {name}! "
            f"You are {age} years old. "
            f"You will turn {age + 1} next year."
        )

    # Send data to HTML
    return render_template("index.html", message=message)


# Run the server
if __name__ == "__main__":
    app.run(debug=True)