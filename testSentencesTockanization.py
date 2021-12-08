# Importing required libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences


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

#
# sentences = ['I love my dog',
#              'I love my cat',
#              'you love my dog!'
#              ]
#
# tokenizer = Tokenizer(num_words = 100)
# tokenizer.fit_on_texts(sentences)
# word_index = tokenizer.word_index

# Exoectec resulting dictionary without a new token for "dog!"
# print(word_index)
#
#
#
# sentences = ['I love my dog',
#              'I love my cat',
#              'you love my dog!',
#              'Do you think my dog is amazing?',
#              ]
#
# tokenizer = Tokenizer(num_words = 100)
# tokenizer.fit_on_texts(sentences)
# word_index = tokenizer.word_index

# this creates sequence of tokens representing each sentence
# sequences = tokenizer.texts_to_sequences(sentences)
#
# print(word_index)
# print(sequences)
#
#
#
# test_data = ['i really love my dog',
#              'my dog loves my manatee',
#              ]

# test_seq = tokenizer.texts_to_sequences(test_data)
#
# print(test_seq)
#
#
# sentences = ['I love my dog',
#              'I love my cat',
#              'you love my dog!',
#              'Do you think my dog is amazing?',
#              ]

# adding a "out of vocabulary" word to the tokenizer
# tokenizer = Tokenizer(num_words = 100,oov_token="<OOV>")
# tokenizer.fit_on_texts(sentences)
# word_index = tokenizer.word_index
# sequences = tokenizer.texts_to_sequences(sentences)
#
# test_data = ['i really love my dog',
#              'my dog loves my manatee',
#              ]
#
# test_seq = tokenizer.texts_to_sequences(test_data)
#
# print(word_index)
# print(test_seq)


sentences = ['I love my dog',
             'I love my cat',
             'you love my dog!',
             'Do you think my dog is amazing?',
             ]

tokenizer = Tokenizer(num_words = 100,oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(sentences)

# padding sequences
padded = pad_sequences(sequences)

print(word_index)
print(sequences)
print(padded)