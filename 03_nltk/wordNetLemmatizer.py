from nltk.stem import WordNetLemmatizer

words = ['eats','eating','eaten','goes','going','gone','write','writing','fairly','sportingly']

lemmatizer = WordNetLemmatizer()

for word in words:
    print(f"{word} --> {lemmatizer.lemmatize(word,pos='v')} ")
