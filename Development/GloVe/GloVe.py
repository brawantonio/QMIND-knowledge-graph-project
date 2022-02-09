import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pandas as pd

"""GloVe class

    - Needs to be instantiated with a file type of pretrained vectors
        i.e.,
            - glove.6B.50d.txt
            - glove.6B.100d.txt
            - glove.6B.200d.txt
            - glove.6B.300d.txt
    In this in main,
    
    glove = GloVePrebuild("glove.6B.50d.txt")
    
    OR:
        Also takes in a pandas dataframe or a list object, 
        as seen in the constructor switch statement
    
    etc.,

"""
class GloVe:
    def __init__(self, Vectors):
        super().__init__()
        self.embeddings_dict = {}
        
        if isinstance(Vectors, str): 
            # Vectors is a filepath
            with open(Vectors, 'r', encoding="utf-8") as f:
                for line in f:
                    values = line.split()
                    word = values[0]
                    vect = np.asarray(values[1:], "float32")
                    self.embeddings_dict[word] = vect
        
        elif isinstance(Vectors, pd.DataFrame):
            # Vectors is a dataframe
            self.embeddings_dict = Vectors.to_dict()
            
        elif isinstance(Vectors, list):
            # Vectors is a list
            for line in Vectors:
                word = line[0]
                vect = np.asarray(line[1:], "float32")
                self.embeddings_dict[word] = vect
        
    def find_closest_embeddings(self, index):
        return sorted(self.embeddings_dict.keys(), key=lambda word: self.compute_word_distance(word, index))

    def plot_all(self, amount = 1000):
        tsne = TSNE(n_components=2, random_state=0)
        words =  list(self.embeddings_dict.keys())
        vectors = [self.embeddings_dict[word] for word in words]
        Y = tsne.fit_transform(vectors[:amount])

        plt.scatter(Y[:, 0], Y[:, 1])

        for label, x, y in zip(words, Y[:, 0], Y[:, 1]):
            plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords="offset points")
        plt.show()
    
    def plot_word_neighbors(self, word, amount = 250):
        tsne = TSNE(n_components=2, random_state=0)
        words = self.find_closest_embeddings(word)[0:amount]
        vectors = [self.embeddings_dict[word] for word in words]
        Y = tsne.fit_transform(vectors[:amount+1])

        plt.scatter(Y[:, 0], Y[:, 1])

        for label, x, y in zip(words, Y[:, 0], Y[:, 1]):
            plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords="offset points")
        plt.show()
    
    def compute_word_distance(self, word1, word2):
        return spatial.distance.euclidean(self.embeddings_dict[word1], self.embeddings_dict[word2])


