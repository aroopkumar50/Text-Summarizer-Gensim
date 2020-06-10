from flask import Flask, render_template, request
import docx2txt
from summarize import summarize
app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/summary', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['myfile']
        file_extension = f.filename.split('.', 1)[1].lower()
        content = ""
        if file_extension == 'docx':
            content = docx2txt.process(f)
        else:
            content = f.read().decode('utf-8')
        summary = summarize(content)
        return render_template('summary.html', summary=summary)


if __name__ == '__main__':
    app.run(debug=True)
