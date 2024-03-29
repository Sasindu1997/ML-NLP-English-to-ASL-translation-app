from nltk.corpus import wordnet

syns = wordnet.synsets("program")

#synset
print(syns[0].name())

#filter the word
print(syns[0].lemmas()[0].name())

#definition of a word
print(syns[0].definition())

#examples
print(syns[0].examples())

#synonyms and antonyms

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name)

print(set(synonyms))
print(set(antonyms))

#check word similarity as a percentage

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("cat.n.01")
w2 = wordnet.synset("cactus.n.01")
print(w1.wup_similarity(w2))