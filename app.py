from flask import Flask, render_template, url_for, request, redirect
from googletrans import Translator

translator = Translator()

app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', tr="", en="")


@app.route('/trtoen/<content>', methods=['GET', 'POST'])
def trtoen(content):
    if request.method == 'POST':
        try:
            content = request.form.get('content', ' ')
            res = (translator.translate(content, src='tr', dest='en')).text
            render_template('index.html', tr=content, en=res)
            return redirect(url_for('trtoen', content=content))
        except:
            return "Error in translate"
    else:
        res = (translator.translate(content, src='tr', dest='en')).text
        return render_template('index.html', tr=content, en=res)


@app.route('/entotr/<content>', methods=['GET', 'POST'])
def entotr(content):
    if request.method == 'POST':
        try:
            content = request.form.get('content', ' ')
            res = (translator.translate(content, src='en', dest='tr')).text
            render_template('index.html', tr=res, en=content)
            return redirect(url_for('entotr', content=content))  # IM NOT SURE MIGHT CHANGE L8R
        except:
            return "Error in translate"
    else:
        res = (translator.translate(content, src='en', dest='tr')).text
        return render_template('index.html', tr=res, en=content)


if __name__ == '__main__':
    app.run()
