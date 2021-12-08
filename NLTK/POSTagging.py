import nltk

from nltk.tokenize import sent_tokenize, word_tokenize

text = word_tokenize("And now for something completely different")
nltk.pos_tag(text)

print(nltk.pos_tag(text))
