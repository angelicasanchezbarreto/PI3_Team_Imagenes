import json
import os
from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import jsonify
from recognition_apples import *
from recognition_bananas import *
from recognition_oranges import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./test_images"
formatos = set(['jpg','png','gif','jpeg'])

def validar(filename):
    return "." in filename and filename.rsplit(".",1)[1] in formatos



@app.route('/')
def upload_img():
    return render_template('buttons.html')



@app.route('/apples', methods=['GET'])
def apples():
    return render_template('apples.html')

@app.route('/bananas', methods=['GET'])
def bananas():
    return render_template('bananas.html')

@app.route('/oranges', methods=['GET'])
def oranges():
    return render_template('oranges.html')



@app.route('/apples' ,methods=['POST'])
def uploaderApples():
    if request.method == 'POST':
        if "file" not in request.files:
            return "the form has no file part"
        f = request.files['file']
        if f.filename == "":
            return "No file selected"
        if f and validar(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            #fruit_type = "apples"
            state = recognition_apples("test_images/"+filename)
            output = {"state" : str(state), "fruit" : fruit_type}
            with open('data.json','w', encoding='utf-8') as f:
                f.write(json.dumps(output))
            if int(state) == 0:
                return "The apples are fresh"
            elif int(state) == 1:
                return "The apples are rotten"
            else:
                return "Imagen no aceptada"
        return "Imagen no permitida"
   

@app.route('/bananas' ,methods=['POST'])
def uploaderBananas():
    if request.method == 'POST':
        if "file" not in request.files:
            return "the form has no file part"
        f = request.files['file']
        if f.filename == "":
            return "No file selected"
        if f and validar(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            #fruit_type = "bananas"
            state = recognition_bananas("test_images/"+filename)
            output = {"state" : str(state), "fruit" : fruit_type}
            with open('data.json','w', encoding='utf-8') as f:
                f.write(json.dumps(output))
            if int(state) == 0:
                return "The bananas are fresh"
            elif int(state) == 1:
                return "The bananas are rotten"
            else:
                return "Imagen no aceptada"
        return "Imagen no permitida"
    

@app.route('/oranges' ,methods=['POST'])
def uploaderOranges():
    if request.method == 'POST':
        if "file" not in request.files:
            return "the form has no file part"
        f = request.files['file']
        if f.filename == "":
            return "No file selected"
        if f and validar(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            #fruit_type = "oranges"
            state = recognition_oranges("test_images/"+filename)
            output = {"state" : str(state), "fruit" : fruit_type}
            with open('data.json','w', encoding='utf-8') as f:
                f.write(json.dumps(output))
            if int(state) == 0:
                return "The oranges are fresh"
            elif int(state) == 1:
                return "The oranges are rotten"
            else:
                return "Imagen no aceptada"
        return "Imagen no permitida"
    

    


if __name__ == '__main__':
    app.run(debug=True, port=4000)
