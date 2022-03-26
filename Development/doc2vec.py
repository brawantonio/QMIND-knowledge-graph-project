import os
import pandas as pd
import preprocessing
import file2doc

#----------------------------------------------------
def corpus_dataframe(dirpath,files_dictionary):
    corpus_data = []

    for key in files_dictionary.keys():
        for file in files_dictionary[key]:
            file_metadata = file2doc.metadata(dirpath + file)
            corpus_data.append(file2doc.extract_text(dirpath+file, key) + file_metadata.all())

    # Extract title of project
    titles = [text.partition("\n")[0] for text in corpus_data]
    # Delete title from each element in data
    for i in range(len(corpus_data)):
        corpus_data[i] = corpus_data[i].replace(titles[i], "")
    # Create df
    df = pd.DataFrame(list(zip(titles, corpus_data)),columns =['title', 'desc'])
    # Create text column
    df["text"] = df["title"] + " " + df["desc"]
    # Display
    #df
    df["clean_text"] = df["text"].apply(preprocessing.stdtextpreprocessing)
    df = df[["title", "clean_text"]]
    return df 


if __name__ == "__main__":
    dirpath = file2doc.get_dirpath()
# ----------------------------- get files --------------------------------
    files_dictionary = file2doc.get_files(dirpath) 
    df = corpus_dataframe(dirpath, files_dictionary)
    #building bag of words and tokens This will go in doc2vec
    from gensim.models.doc2vec import Doc2Vec, TaggedDocument
    text_docs = [TaggedDocument(doc.split(' '), [i]) 
    for i, doc in enumerate(df["clean_text"])]
    #Source for Hyperparameter tuning
    # https://medium.com/betacom/hyperparameters-tuning-tf-idf-and-doc2vec-models-73dd418b4d
    # Instantiate model
    model = Doc2Vec(vector_size=64, window=5, min_count=1, workers=8, epochs=40)
    # Build vocab
    model.build_vocab(text_docs)
    # Train model
    model.train(text_docs, total_examples=model.corpus_count, epochs=model.epochs)
    # Generate vectors
    #from gensim.test.utils import get_tmpfile
    #hazelnut_model = get_tmpfile("my_doc2vec_model")
    model.save(os.getcwd() + '/hazelnut_model')
    #files_dictionary

# --------------------------------- Create data dataframe -----------------
# this needs to be functionalized!!!!! 
