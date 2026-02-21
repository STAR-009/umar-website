from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
import os

app.config['Umar-website-2'] = os.environ.get("Umar-website-2")
app.config['lrvc stqe sxtd ymxj'] = os.environ.get("lrvc stqe sxtd ymxj")
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get("Umar-website-2")

mail = Mail(app)

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

@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        service = request.form["service"]

        msg = Message(
            subject="New Client Booking!",
            recipients=["YOUR_GMAIL@gmail.com"],
            body=f"""
New booking received!

Name: {name}
Email: {email}
Service: {service}
"""
        )

        mail.send(msg)

        return redirect(url_for("book"))

    return render_template("book.html")

@app.route("/success")
def success():
    return "<h2>Payment successful! We will contact you shortly.</h2>"

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
