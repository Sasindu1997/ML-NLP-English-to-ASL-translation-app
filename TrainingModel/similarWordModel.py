import bs4 as bs
import urllib.request
import re
import nltk
from gensim.models import Word2Vec

scrapped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Machine_learning')
article = scrapped_data .read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text

try:
    import string
    from nltk.corpus import stopwords
    import nltk
except Exception as e:
    print(e)


class PreProcessText(object):

    def __init__(self):
        pass

    def __remove_punctuation(self, text):
        """
        Takes a String
        return : Return a String
        """
        message = []
        for x in text:
            if x in string.punctuation:
                pass
            else:
                message.append(x)
        message = ''.join(message)

        return message

    def __remove_stopwords(self, text):
        """
        Takes a String
        return List
        """
        words= []
        for x in text.split():

            if x.lower() in stopwords.words('english'):
                pass
            else:
                words.append(x)
        return words


    def token_words(self,text=''):
        """
        Takes String
        Return Token also called  list of words that is used to
        Train the Model
        """
        message = self.__remove_punctuation(text)
        words = self.__remove_stopwords(message)
        return words



flag = nltk.download("stopwords")

if (flag == "False" or flag == False):
    print("Failed to Download Stop Words")
else:
    print("Downloaded Stop words ...... ")
    helper = PreProcessText()
    #words = helper.token_words(text=txt)
    words = helper.token_words(text=article_text)



#model = Word2Vec([words], min_count=1)
model = Word2Vec([words], vector_size=100, window=5, min_count=1, workers=4)
vocabulary = model.wv.vocab
sim_words = model.wv.most_similar('machine')
sim_words