# # in the first time you should use these two line codes
# import nltk
# nltk.download('punkt')

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
import numpy as np

source_txt = 'text.txt'
frequence_name = 'Tokens_without_stops.txt'
glove_location = '/Users/zhanglingfeng/Downloads/glove/glove.6B.200d.txt'
# http://nlp.stanford.edu/data/glove.6B.zip

def tokenization_statistic(tokenization_all,Tokens_file_name):
    # dct = Dictionary([tokenization_all])  # initialize a Dictionary
    word_frequency = []
    for word in tokenization_all:
        word_frequency.append(tokenization_all.count(word))
    dct_pairs = sorted(list(set(list(zip(tokenization_all,word_frequency)))),key=lambda x: x[1],reverse=True)
    num = 0
    with open(Tokens_file_name,'w') as frequency_file:
        frequency_file.write("number" + " " + "word" + " " + "frequency" +"\n")
        for item in dct_pairs:
            frequency_file.write(str(num) + " " + item[0] + " " + str(item[1]) +"\n")
            num += 1
    
# encoding='utf-8-sig' is to remove \ufeff
# write the result into .txt file

def word_preprocessing(source_txt, frequence_name):
    lemmatizer = WordNetLemmatizer() 
    ps = PorterStemmer() 

    all_text =  open(source_txt, 'r', encoding='utf-8-sig')

    tokenization_all = []

    for text_line in all_text:

        text_line = text_line.lower()

        tokenization_results = word_tokenize(text_line)

        tokenization_all += tokenization_results

    stopwords_list = []
    with open('stopwords.txt','r') as f:
        for line in f:
            stopwords_list.append(line[:-1])
    # delete /n line break

    punctuations="!\"#$%&'’()*+,-./:;<=>?@[\]^_`{|}~"

    punctuation_list = []
    for punc in punctuations:
        punctuation_list.append(punc)

    stopwords_with_punctuations = stopwords_list + punctuation_list

    filtered_sentence = []
    for w in tokenization_all: 
        if w not in stopwords_with_punctuations:
            w = lemmatizer.lemmatize(w)
            w = ps.stem(w)
            filtered_sentence.append(w)

    tokenization_statistic(filtered_sentence, frequence_name)

def loadGloveModel(gloveFile):
    print("Loading Glove Model")
    f = open(gloveFile,'r')
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print("Done.",len(model)," words loaded!")
    return model

def get_embedding_vector(token_words):
    model = loadGloveModel(glove_location)
    return model[token_words]