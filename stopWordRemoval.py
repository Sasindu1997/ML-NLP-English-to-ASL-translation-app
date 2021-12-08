import nltk

# download NLTK to the project
# nltk.download()

data = 0

stopWords = nltk.corpus.stopwords.words('english');


def remove_stopwords(txt_tokenized):
    txt_clean = [word for word in txt_tokenized if word not in stopWords]
    return txt_clean


data['msg-no-sw'] = data['msg_clean_tokenized'].apply(lambda x: remove_stopwords(x))
data.head()
