from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Stores movies temporarily while the app is running
movie_list = []


@app.route("/")
def home():
    return render_template("index.html", movies=movie_list)


@app.route("/add", methods=["POST"])
def add_movie():
    movie = request.form.get("movie", "").strip().upper()

    if movie:
        if movie not in movie_list:
            movie_list.append(movie)

    return redirect(url_for("home"))


@app.route("/sort")
def sort_movies():
    movie_list.sort()
    return redirect(url_for("home"))


@app.route("/delete/<movie>")
def delete_movie(movie):
    movie = movie.upper()

    if movie in movie_list:
        movie_list.remove(movie)

    return redirect(url_for("home"))


@app.route("/clear")
def clear_movies():
    movie_list.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)