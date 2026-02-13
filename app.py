from flask import Flask, render_template, request
import re

app = Flask(__name__)

vowels = "aeiouAEIOU"

# ENCODE FUNCTION
def encode(text):
    result = ""
    for ch in text:
        if ch in vowels:
            result += ch + "pa"
        else:
            result += ch
    return result

# DECODE FUNCTION
def decode(text):
    return re.sub(r'([aeiouAEIOU])pa', r'\1', text)


@app.route("/", methods=["GET", "POST"])
def home():
    output = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        action = request.form.get("action")

        if action == "encode":
            output = encode(text)
        elif action == "decode":
            output = decode(text)

    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)