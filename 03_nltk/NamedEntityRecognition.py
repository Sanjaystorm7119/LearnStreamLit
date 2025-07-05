import nltk
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
sentence="The Eiffel Tower was built from 1887 to 1889 by French engineer Gustave Eiffel, whose company specialized in building metal frameworks and structures."
"""
Person Eg: Krish C Naik
Place Or Location Eg: India
Date Eg: September,24-09-1989
Time  Eg: 4:30pm
Money Eg: 1 million dollar
Organization Eg: iNeuron Private Limited
Percent Eg: 20%, twenty percent
"""


sentence2 = "My name is Sanjay"


# words = nltk.word_tokenize(sentence)
# print(words)



words = nltk.word_tokenize(sentence2)
print(f"words--> {words}")
pos_tag = nltk.pos_tag(words)
print(f"pos_tag-->{pos_tag}")
chunk = nltk.ne_chunk(pos_tag)
print(f"chunk-->{chunk}").draw()
