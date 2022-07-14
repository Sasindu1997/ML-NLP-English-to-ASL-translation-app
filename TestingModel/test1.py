from NLTK.testModel1 import *
import os
import tensorflow as tf
from tensorflow import keras

Input2 = 'I am going to home.'

new_model = tf.keras.models.load_model(r'C:\Users\Acer\PycharmProjects\tfModel\testFunctions\saved_model\similar_word_model.h5')
result = testModelFunc(Input2, new_model)
print("result")
print(result)