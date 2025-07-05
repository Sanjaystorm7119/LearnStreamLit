import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

corpus = """
He took a sip of the drink of history. He wasn't sure whether he liked it or not, but at this moment it didn't matter. She had made it especially for him so he would have forced it down even if he had absolutely hated it. That's simply the way things worked. She made him a new-fangled drink each day and he took a sip of it and smiled, saying it was excellent.
There was only half a worm in the apple. At first, Judy didn't quite comprehend what this meant. "Why would only half a worm be living in an apple?" she wondered. And then it dawned on her. Judy quickly spit out the bite she had just taken expecting to see the other half of the worm. It ended up being much worse than that.
"""

stemmer = PorterStemmer()
snowBall_stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

sentences = sent_tokenize(corpus)

for i in range(len(sentences)):
    words = word_tokenize(sentences[i].lower())
    print(f"Original sentence: {sentences[i]}")

    # filtered_stemmed = [stemmer.stem(word) for word in words if word.lower() not in stop_words and word.isalpha()]
    # print(f"Stemmed and filtered words: {filtered_stemmed} \n")
    
    # snowBallfiltered_stemmed = [snowBall_stemmer.stem(word) for word in words if word.lower() not in stop_words and word.isalpha()]
    # print(f"Stemmed and snowballfiltered words: {snowBallfiltered_stemmed} \n")
    
    
    filtered_lematised = [lemmatizer.lemmatize(word,pos='v') for word in words if word.lower() not in stop_words and word.isalpha()]
    sentences[i] = ' '.join(filtered_lematised)
    
    # print(f"lemmatised and filtered words: {filtered_lematised} \n")

print(f"lemmatised and filtered words: {sentences} \n")


