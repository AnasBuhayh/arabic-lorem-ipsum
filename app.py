from flask import Flask, render_template, request, url_for
import arrand.arrandom

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    title = request.form['title']
    text = arrand.arrandom.sample(category = "text", max_length=2, vocalized=False)
    return render_template('index.html', text=text)

if __name__ == "__main__":
    app.run()