#import os
#import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
import string

#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('omw-1.4')
#---------------------------- Preprocessing -------------------------------------------------

def stdtextpreprocessing(text):
    """ Desc: Text preprocessing of social media text using 
    typical text cleaning methods such as lowercasing, removal of mentions, etc.
    Input: text (string) - text to be cleaned
    Output: text (string) - cleaned text """
    
    # Instantiate stopWords
    stopWords = stopwords.words("english")
    # Instantiate wordnet lemmatizer
    wn = nltk.WordNetLemmatizer()
    # Lower case
    text = text.lower()
    # Remove all stop words
    text = ' '.join([word for word in text.split(' ') if word not in stopWords])
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