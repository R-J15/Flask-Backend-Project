from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == 'POST':
        text_string = request.form['text_string']
        regex = request.form['regex']
        matches = re.findall(regex, text_string)
        return render_template('index.html', matches=matches)
    else:
        return render_template('index.html')
   

if __name__ == '__main__':
    app.run(debug=True)