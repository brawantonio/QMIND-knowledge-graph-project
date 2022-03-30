#preprocessing.py

#import os
#import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
import string

#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('omw-1.4')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')

    
# Instantiate stopWords
stop = stopwords.words("english")

#---------------------------- Preprocessing -------------------------------------------------

def stdtextpreprocessing(text):
    """ Desc: Text preprocessing of social media text using 
    typical text cleaning methods such as lowercasing, removal of mentions, etc.
    Input: text (string) - text to be cleaned
    Output: text (string) - cleaned text """

    # Instantiate wordnet lemmatizer
    wn = nltk.WordNetLemmatizer()
    # Lower case
    text = text.lower()
    # Remove all stop words
    text = ' '.join([word for word in text.split(' ') if word not in stop])
    # Remove unicode characters (emojis, etc.)
    text = text.encode('ascii', 'ignore').decode()
    # Remove urls
    text = re.sub(r'http*\S+', ' ', text)
    # Remove multi-character symbols (\n, \t, \r)
    text = re.sub(r'[\n\r\t]', ' ', text)
    # Remove numeric values
    text = re.sub(r'[0-9]', ' ', text)
    # Remove punctuation
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    # Remove extra blank spaces
    text = re.sub(r'\s{2,}', ' ', text)
    # Lemmatize the text
    text = ' '.join([wn.lemmatize(word) for word in text.split(' ')])
    return text

def preproc_query(query):
    wn = nltk.WordNetLemmatizer()
    # Lower case
    query = query.lower()
    # Remove unicode characters (emojis, etc.)
    query = query.encode('ascii', 'ignore').decode('utf-8')
    # Reduce repeated letters
    query= re.sub(re.compile(r"(.)\1{2,}"), r"\1\1", query)
    # Remove stop words
    pat = r'\b(?:{})\b'.format('|'.join(stop))
    query = re.sub(pat, '', query)
    # Remove punctuation
    query = re.sub('[%s]' % re.escape(string.punctuation), ' ', query)
    # Remove stop words again (in case stop word was next to punctuation)
    query = re.sub(pat, '', query)
    # Remove extra blank spaces
    query = re.sub(r'\s{2,}', ' ', query)
    # Lemmatize and tokenize
    query = [wn.lemmatize(word) for word in query.split()]
    
    return query
#import re
#import nltk
#from nltk.corpus import stopwords
#stop = stopwords.words('english')

example_string = """
Hey,
This week has been crazy. Attached is my report on IBM. Can you give it a quick read and provide some feedback.
Also, make sure you reach out to Claire (claire@xyz.com).
You're the best.
Cheers,
George W.
212-555-1234
"""

def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

def ie_preprocess(document):
    document = ' '.join([i for i in document.split() if i not in stop])
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def extract_names(document):
    names = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names

if __name__ == '__main__':
    numbers = extract_phone_numbers(string)
    emails = extract_email_addresses(string)
    names = extract_names(string)