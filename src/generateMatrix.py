import numpy as np
import os
from gensim.models.keyedvectors import KeyedVectors

#convert binary gene2vec to matrix txt

def load_embeddings(file_name):
    model = KeyedVectors.load(file_name)
    wordVector = model.wv
    vocabulary, wv = zip(*[[word, wordVector[word]] for word, vocab_obj in wordVector.vocab.items()])
    return np.asarray(wv), vocabulary

def outputTxt (embeddings_file):
    embeddings_file = embeddings_file  # gene2vec file address
    wv, vocabulary = load_embeddings(embeddings_file)
    index = 0
    save_path = 'outputDir/'
    matrix_txt_file = os.path.join(save_path, embeddings_file+".txt" ) # gene2vec matrix txt file address
    with open(matrix_txt_file, 'w') as out:
        for ele in wv[:]:
            out.write(str(vocabulary[index]) + "\t")
            index = index + 1
            for elee in ele:
                out.write(str(elee) + " ")
            out.write("\n")
    out.close()


