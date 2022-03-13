import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

textInput = "These are short, famous texts in English from classic sources like the Bible or Shakespeare. Some texts " \
            "have word definitions and explanations to help you. Some of these texts are written in an old style of " \
            "English. Try to understand them, because the English that we speak today is based on what our great, " \
            "great, great, great grandparents spoke before! Of course, not all these texts were originally written in " \
            "English. The Bible, for example, is a translation. But they are all well known in English today and many " \
            "of them express beautiful thoughts "

#
# covert text input to lowercase
#
lower_case_text = textInput.lower()

#
# cleaned_text - remove punctuation
#
cleaned_text = lower_case_text.translate(str.maketrans('', '', string.punctuation))

#
# tokenizing - sentence tokenizing, word tokenizing
#
tokenized_text = word_tokenize(cleaned_text)

#
# provide language to remove stopwords
#
stop_words = set(stopwords.words("English"))

#
# remove stopwords
#
filtered_sentence = [w for w in tokenized_text if not w in stop_words]
#
# add pos tagging
#
pos_tagged_text = nltk.pos_tag(filtered_sentence)

#
# stemming
#
ps = PorterStemmer()

# for w in tokenized_text:
#     print(ps.stem(w))

#
# output
#
print(pos_tagged_text)