import os
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.preprocessing.image import image_dataset_from_directory

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout,Flatten,Dense, Activation
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K
from tensorflow import keras

import numpy as np  


K.clear_session()


#Entrenamiento
training_data = 'images/images_bananas/train'
#Validacion
validation_data = 'images/images_bananas/test'


#Parametros Globales

#Numero de veces que se va a iterar sobre el set de entrenamiento
epochs=100
#Tamaño de imagenes que voy a procesar
height, length=128,128
#Numero de imagenes que se mandara a la computadora a procesar en cada paso 
batch_size=10

#Numero imagenes en el set de entrenamiento
steps=40

#Numero de imagenes en el set de validacion
steps_validation=40

#Filtros para aplicar en cada convolucion
filtrosConvl1=32
filtrosConvl2=64

#Tamaño de filtro1
tamano_filtro1=(3,3)

#Tamaño de filtro2
tamano_filtro2=(2,2)


#Tamaño de filtro de mas pooling
tamano_pool=(2,2)

clases=2

#ajuste para acercarse a la solucion optima
lr=0.0005


#PreProcesamiento de Imagenes

#Para el entrenamiento
training_data_gen  = ImageDataGenerator(
    rescale=1./255
)

#Para la validacion
validation_data_gen = ImageDataGenerator(
    rescale=1./255,
)

img_training = training_data_gen.flow_from_directory(
    training_data,
    target_size=(128,128),
    batch_size=batch_size,
    class_mode='categorical',
)

#Crea el set de prueba
img_validation = validation_data_gen.flow_from_directory(
    validation_data,
    target_size=(128,128),
    batch_size=batch_size,
    class_mode='categorical',
)


print(img_training.class_indices)


#Creacion del Convolutional Neural Networks
#El secreto para hacer mas eficiente y preciso el codigo es agregar mas capas convolucionales o mas capas conectadas.
#CONVOLUCION

#Iniciar el CNN
convolutional_neural_netwoks = Sequential()

#Primera parte: Convolucion
convolutional_neural_netwoks.add(Convolution2D(input_shape=(128,128,3), filters=32 ,kernel_size=3, strides=3, activation='relu'))

#Segunda parte: Agrupacion
convolutional_neural_netwoks.add(MaxPooling2D(pool_size=tamano_pool))

#Primera parte: Convolucion 1.2
convolutional_neural_netwoks.add(Convolution2D(filters=64,kernel_size=3, activation='relu'))
convolutional_neural_netwoks.add(MaxPooling2D(pool_size=tamano_pool))

#Primera parte: Convolucion 1.3
convolutional_neural_netwoks.add(Convolution2D(filters=128,kernel_size=3, activation='relu'))
convolutional_neural_netwoks.add(MaxPooling2D(pool_size=tamano_pool))


#Primera parte: Convolucion 1.4
#convolutional_neural_netwoks.add(Convolution2D(filters=256,kernel_size=3, activation='relu'))
#convolutional_neural_netwoks.add(MaxPooling2D(pool_size=tamano_pool))

#Primera parte: Convolucion 1.5
#convolutional_neural_netwoks.add(Convolution2D(filters=512,kernel_size=3, activation='relu'))
#convolutional_neural_netwoks.add(MaxPooling2D(pool_size=tamano_pool))


#Tercera parte: Aplanamiento

convolutional_neural_netwoks.add(Flatten())

#Cuarta parte: Conexion Completo

convolutional_neural_netwoks.add(Dense(units=128,activation='sigmoid'))

#Quinta parte: Capa de salida

convolutional_neural_netwoks.add(Dense(clases, activation='sigmoid'))

#convolutional_neural_netwoks.add(Dropout(0.5))

#Compilacion

#opt = keras.optimizers.Adam(learning_rate=lr)  


convolutional_neural_netwoks.compile( optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'] )


#Parte 2 compilacion - Encajando RNC en las imagenes
convolutional_neural_netwoks.fit(img_training, steps_per_epoch=steps, epochs=epochs, validation_data=img_validation, validation_steps = steps_validation, verbose=1)


convolutional_neural_netwoks.summary()


convolutional_neural_netwoks.save('models/model_bananas/model_bananas.h5')
convolutional_neural_netwoks.save_weights('models/model_bananas/weights_bananas.h5')

