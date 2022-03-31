import pandas as pd
import numpy as np
#from IPython.display import display
import os
import json
import preprocessing

from gensim.models.doc2vec import Doc2Vec #, TaggedDocument

#import re
#import nltk
#import string
#from nltk.corpus import stopwords
from sklearn.decomposition import PCA

#nltk.download('stopwords')
#nltk.download('wordnet')
# Instantiate stopWords
#stopWords = stopwords.words("english")   
# Instantiate wordnet lemmatizer
#wn = nltk.WordNetLemmatizer()



"""
Desc: Standard preprocessing of query
Input: query (string) - text to be cleaned
Output: query (list of string) - cleaned text
"""

# Convert string to vec
def search(query):
    model = Doc2Vec.load(os.getcwd() + '/hazelnut_kingston') 
    df = pd.read_csv("/Users/braulioantonio/Documents/Python/Hazelnut/search_database.csv", 
                usecols=["url", "clean_text", "text_vec"] )
    #query = "Queen's university"
    query = preprocessing.preproc_query(query)
    query = model.infer_vector(query)

    # Convert to np array
    query = np.array(query)

    # nearest neighbors----------------------------------------------------------------
    df["cos_dist"] = df["text_vec"].apply(lambda x: np.dot(query, np.array(x)) / 
                                      (np.linalg.norm(query) * np.linalg.norm(np.array(x))))
    df = df.sort_values(by=["cos_dist"], ascending=False, ignore_index=True)
    # Take top N results
    N = 10
    df = df.head(N)

    # PCA-------------------------------------------------------------------------------
    pca = PCA(2)
    # Transform the data
    df_vec = pd.DataFrame(df["text_vec"].to_list())
    # Convert to dataframe
    df_vec = pd.DataFrame(pca.fit_transform(df_vec), columns=['pca_x', 'pca_y'])
    # Normalize pca dimensions to [0, 1]
    df_vec["pca_x"] = (df_vec["pca_x"] - df_vec["pca_x"].min()) / (df_vec["pca_x"].max() - df_vec["pca_x"].min()) 
    df_vec["pca_y"] = (df_vec["pca_y"] - df_vec["pca_y"].min()) / (df_vec["pca_y"].max() - df_vec["pca_y"].min())
    # Concatenate df_vec to df
    df = pd.concat([df, df_vec], axis=1)
    # Select columns
    df = df[["url", "pca_x", "pca_y", "cos_dist"]]

    result = df.to_json(orient="split")
    parsed = json.loads(result)
    return json.dumps(parsed)



    """ 
def preproc_query(query):
    # Lower case
    query = query.lower()
    # Remove unicode characters (emojis, etc.)
    query = query.encode('ascii', 'ignore').decode('utf-8')
    # Reduce repeated letters
    query= re.sub(re.compile(r"(.)\1{2,}"), r"\1\1", query)
    # Remove stop words
    pat = r'\b(?:{})\b'.format('|'.join(stopWords))
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
"""
