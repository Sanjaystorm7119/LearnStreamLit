from nltk.tokenize import sent_tokenize  #Para to sentences
from nltk.tokenize import word_tokenize  #sentences to words
from nltk.tokenize import wordpunct_tokenize #sentences to words with punctuations treated separately
from nltk.tokenize import TreebankWordTokenizer #sentences to words with punctuations along with attached word

corpus = """I am Sanjay's.
I am learning ML , NLP .
And I am excited !
"""

# corpus
# print(corpus)


documents = sent_tokenize(corpus)
# document / sentences
print(f" sent_tokenize -->documents / sentences ")

for doc in documents:
    print(doc)


#words 
words = word_tokenize(corpus)
print(f"words {words}")
# print(words)

#with punctutation
wordspunctutation = wordpunct_tokenize("corpus's")
print(f"wordpunct_tokenize --> wordspunctutation")
print(wordspunctutation)


#TreeBankWordTokeizer
print("TreeBankWordTokeizer")
# tokenizer = TreebankWordTokenizer()
# print(tokenizer.tokenize(corpus))

print(TreebankWordTokenizer().tokenize(corpus))

''' Output

documents / sentences
I am Sanjay's.
I am learning ML , NLP .
And I am excited !

words
['I', 'am', 'Sanjay', "'s", '.', 'I', 'am', 'learning', 'ML', ',', 'NLP', '.', 'And', 'I', 'am', 'excited', '!']

wordspunctutation / TreeBankWordTokeizer
['I', 'am', 'Sanjay', "'", 's', '.', 'I', 'am', 'learning', 'ML', ',', 'NLP', '.', 'And', 'I', 'am', 'excited', '!']

'''
