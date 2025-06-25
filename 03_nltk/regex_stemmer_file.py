from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer


words = ['eats','eating','eaten','goes','going','gone','write','writing','fairly','sportingly']

reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)

print(reg_stemmer.stem("eating"))

snowball_stemming = SnowballStemmer('english')

for word in words:
    print(f"{word} --> {snowball_stemming.stem(word)}")
