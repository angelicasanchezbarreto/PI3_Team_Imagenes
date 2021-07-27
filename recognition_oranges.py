import re
import numpy as np

from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

from os import listdir

from tensorflow.python.keras.backend import cos

import json


height, length = 128,128

fruit_type = "oranges"

model='models/model_oranges/model_oranges.h5'
weight='models/model_oranges/weights_oranges.h5'

convolutional_neural_netwoks = load_model(model)

convolutional_neural_netwoks.load_weights(weight)


def load_models(pathmodel, pathweight):
    cnn = load_model(pathmodel)
    cnn.load_weights(pathweight)
    return cnn


def load_image(img, altura,largo):
    final_value = load_img(img, target_size=(altura,largo))
    final_value = img_to_array(final_value)
    final_value = np.expand_dims(final_value,axis=0)
    return final_value

correct_counter = 0
incorrect_counter = 0
corroborate_counter = 0

final_list=[]


def recognition_oranges(file):
    x = load_img(file, target_size=(height, length))
    x = img_to_array(x)
    x=np.expand_dims(x, axis=0)
    arreglo=convolutional_neural_netwoks.predict(x)
    resultado = arreglo[0]
    #print(resultado)
    respuesta = np.argmax(resultado)
    #print(respuesta)
    if(respuesta == 0):
        global correct_counter
        correct_counter = correct_counter + 1
    if(respuesta == 1):
        global incorrect_counter
        #print("Otros")
        incorrect_counter = incorrect_counter + 1
    return respuesta


def get_final_list():
    final_list.append(correct_counter)
    final_list.append(corroborate_counter)
    final_list.append(incorrect_counter)
    print(final_list)


""" for image in listdir("dataset/train/rottenapples"):
    print("----------")
    print(image)
    recognition("dataset/train/rottenapples/" + image)
    #print(image)  """


""" if(fruit_type == 0):
    output = recognition("test_images/fresh_apple.jpg")
    output2 = recognition("test_images/rotten_apple.jpg")
elif(fruit_type == 1):
    recognition("test_images/fresh_orange.jpg")
    recognition("test_images/rotten_orange.jpg")
elif(fruit_type == 2):
    recognition("test_images/fresh_banana.jpg")
    recognition("test_images/rotten_banana.jpg") """

#get_final_list()


state = recognition_oranges("test_images/oranges_fresh.jpg") #IMAGEN INGRESADA POR EL APLICATIVO
output = {"state" : str(state), "fruit" : fruit_type}
with open('data.json','w', encoding='utf-8') as f:
    f.write(json.dumps(output))




