""".....Program to demonstrate Tokenization ......
What is tokenization? Tokenization is the process of breaking up the given text into units called tokens.
The tokens may be words or number or punctuation mark.A token is the technical name for a sequence of characters
"""
import nltk
text = """At eight o'clock on Thursday morning Arthur didn't feel very good.
 He went to see the doctor at 20 new Street."""
sent_tokens = nltk.sent_tokenize(text)
word_tokens = nltk.word_tokenize(text)
print(sent_tokens)
print(word_tokens)