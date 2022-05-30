import os
from flask import Flask, request, redirect, send_file, url_for, render_template
from werkzeug.utils import secure_filename
import ProcessImage

UPLOAD_FOLDER = 'static/data/pdf'
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(f"{UPLOAD_FOLDER}/{filename}")
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template("index.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    ProcessImage.init(filename)
    return redirect(url_for('downloadFile'))

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "PDF.zip"
    return send_file(path, as_attachment=True )

@app.route('/template')
def downloadTemplate ():
    pathTemplate = "static/data/CSV/TemplateUTF.csv"
    return send_file(pathTemplate, as_attachment=True )
    
if __name__ == '__main__':
  app.run(debug=True)


