from flask import Flask, render_template, request

app = Flask(__name__)

cart = []

@app.route("/", methods=["GET", "POST"])
def home():

    expensive_item = None
    cheap_item = None

    if request.method == "POST":

        action = request.form["action"]

        if action == "add":

            item = request.form["item"]
            price = int(request.form["price"])

            cart.append((item, price))

        elif action == "analyze":

            if cart:

                expensive_item = max(cart, key=lambda x: x[1])
                cheap_item = min(cart, key=lambda x: x[1])

    return render_template(
        "index.html",
        cart=cart,
        expensive_item=expensive_item,
        cheap_item=cheap_item
    )


if __name__ == "__main__":
    app.run(debug=True)