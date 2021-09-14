from flask import Flask, render_template, request, url_for
from text_gen import generate_text
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    word_count = request.form['word_count']
    
    try:
        word_count = int(word_count)
        if word_count >= 1 and word_count <= 5500:
            text = generate_text(word_count)
        else:
            text = "العدد الأقصى للكلمات هو 5500 كلمة"
    except ValueError:
        text = "أرجوا إدخال رقم"

    return render_template('index.html', text=text)

if __name__ == "__main__":
    app.run()