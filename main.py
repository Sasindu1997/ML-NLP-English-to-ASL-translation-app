# Importing required libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer


# # List of sample sentences that we want to tokenize
# # sentences = ['I love my dog',
# #              'I love my cat',
# #              ]
# #
# # # intializing a tokenizer that can index
# # # num_words is the maximum number words that can be kept
# # # tokenizer will automatically help in choosing most frequent words
# # tokenizer = Tokenizer(num_words = 100)
# #
# # # fitting the sentences to using created tokenizer object
# # tokenizer.fit_on_texts(sentences)
# #
# # # the full list of words is available as the tokenizer's word index
# # word_index = tokenizer.word_index
# #
# # # the result will be a dictionary, key being the words and the values being the token for that word
# # print(word_index)


sentences = ['I love my dog',
             'I love my cat',
             'you love my dog!'
             ]

tokenizer = Tokenizer(num_words = 100)
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

# Exoectec resulting dictionary without a new token for "dog!"
print(word_index)