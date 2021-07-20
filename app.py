import json
import os
from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import jsonify
from recognition import * 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./test_images"
formatos = set(['jpg','png','gif','jpeg'])

def validar(filename):
    return "." in filename and filename.rsplit(".",1)[1] in formatos



@app.route('/')
def upload_img():
    return render_template('form.html')


@app.route('/apples' ,methods=['POST'])
def uploader():
    if request.method == 'POST':
        if "file" not in request.files:
            return "the form has no file part"
        f = request.files['file']
        if f.filename == "":
            return "No file selected"
        if f and validar(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            fruit_type = "apples"
            state = recognition("test_images/"+filename)
            #fruit = fruit_type
            if int(state) == 0:
                return "The apples is fresh"
            elif int(state) == 1:
                return "The apples is rotten"
            else:
                return "Imagen no aceptada"
        return "Imagen no permitida"


@app.route('/oranges' ,methods=['POST'])
def uploader():
    if request.method == 'POST':
        if "file" not in request.files:
            return "the form has no file part"
        f = request.files['file']
        if f.filename == "":
            return "No file selected"
        if f and validar(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            fruit_type = "oranges"
            state = recognition("test_images/"+filename)
            #fruit = fruit_type
            if int(state) == 0:
                return "The orange is fresh"
            elif int(state) == 1:
                return "The orange is rotten"
            else:
                return "Imagen no aceptada"
        return "Imagen no permitida"


@app.route('/bananas' ,methods=['POST'])
def uploader():
    if request.method == 'POST':
        if "file" not in request.files:
            return "the form has no file part"
        f = request.files['file']
        if f.filename == "":
            return "No file selected"
        if f and validar(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            fruit_type = "bananas"
            state = recognition("test_images/"+filename)
            #fruit = fruit_type
            if int(state) == 0:
                return "The bananas is fresh"
            elif int(state) == 1:
                return "The bananas is rotten"
            else:
                return "Imagen no aceptada"
        return "Imagen no permitida"


if __name__ == '__main__':
    app.run(debug=True, port=4000)
