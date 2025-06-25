from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import TreebankWordTokenizer
corpus = """I am Sanjay's.
I am learning ML , NLP .
And I am excited !
"""

# corpus
# print(corpus)


documents = sent_tokenize(corpus)
# document / sentences
print(f"documents / sentences")

for doc in documents:
    print(doc)


#words 
words = word_tokenize(corpus)
print(f"words")
print(words)

#with punctutation
wordspunctutation = wordpunct_tokenize("corpus's")
print(f"wordspunctutation")
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

wordspunctutation
['I', 'am', 'Sanjay', "'", 's', '.', 'I', 'am', 'learning', 'ML', ',', 'NLP', '.', 'And', 'I', 'am', 'excited', '!']

'''
