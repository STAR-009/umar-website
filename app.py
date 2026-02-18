from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    # Add project list if you want dynamic later
    return render_template("portfolio.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Save messages here
        return redirect(url_for('contact'))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
