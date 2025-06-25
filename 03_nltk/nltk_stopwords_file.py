from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
# nltk.download('stopwords')

# print(stopwords.words('english'))

corpus ="""
He took a sip of the drink. He wasn't sure whether he liked it or not, but at this moment it didn't matter. She had made it especially for him so he would have forced it down even if he had absolutely hated it. That's simply the way things worked. She made him a new-fangled drink each day and he took a sip of it and smiled, saying it was excellent.
There was only half a worm in the apple. At first, Judy didn't quite comprehend what this meant. "Why would only half a worm be living in an apple?" she wondered. And then it dawned on her. Judy quickly spit out the bite she had just taken expecting to see the other half of the worm. It ended up being much worse than that.
"""
stemmer = PorterStemmer()
sentences = sent_tokenize(corpus)
# print(sentences)
for sentence in sentences:
    print(sentence)

