import os
import tensorflow as tf
from tensorflow import keras

print(tf.version.VERSION)

new_model = tf.keras.models.load_model(r'C:\Users\Acer\PycharmProjects\tfModel\testFunctions\saved_model\similar_word_model.h5')
# new_model = tf.keras.models.load_model('text_processing_model.h5')

# Show the model architecture
new_model.summary()
# new_model.summary()

