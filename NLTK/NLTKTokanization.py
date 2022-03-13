from nltk.tokenize import sent_tokenize, word_tokenize
import os

file = os.path.abspath("C:/Users/Acer/PycharmProjects/tfModel/Dataset/maize/yield_1981.nc4")

# tokenizing - sentence tokenizing, word tokenizing

textInput = "These are short, famous texts in English from classic sources like the Bible or Shakespeare. Some texts have word definitions and explanations to help you. Some of these texts are written in an old style of English. Try to understand them, because the English that we speak today is based on what our great, great, great, great grandparents spoke before! Of course, not all these texts were originally written in English. The Bible, for example, is a translation. But they are all well known in English today, and many of them express beautiful thoughts. "

# dataset1 = open("C:/Users/Acer/Py/charmProjects/tfModel/Dataset/maize/yield_1981.nc4", "r")
# print(dataset1.read())

# print(sent_tokenize(textInput));

print(word_tokenize(textInput));

# for i in word_tokenize(dataset1):
#     print(i)
