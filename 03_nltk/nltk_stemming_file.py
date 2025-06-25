from nltk.stem import PorterStemmer

stemming = PorterStemmer()
words = ['eats','eating','eaten','goes','going','gone','write','writing']

for word in words:
    print(f"{word} --> {stemming.stem(word)}")