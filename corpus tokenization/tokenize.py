import os
from nltk.tokenize import word_tokenize
from collections import defaultdict
import operator

def tokenize(directory_input, input_file, tokens_occ, tokens_per_file):
   with open(os.path.join(directory_input, input_file), "rt", encoding="utf-8") as f:
       tokens = word_tokenize(f.read())
       # Count occurences per token
       for token in tokens:
           if token.startswith("Wiki_"):
               tokens_occ[token] += 1
   return tokens_occ, tokens_per_file

def writeVocabularyFiles(wiki_filename, sorted_d):
    nb_sup_10 = 0
    # Write unique wiki words in a file
    wiki_file = open(wiki_filename, 'w', encoding="utf-8")
    for word, occ in sorted_d.items():
        #wiki_file.write(str(word) + " " + str(occ) + "\n")
        if occ > 10:
            nb_sup_10 += 1
    return nb_sup_10

def tokenizeAllFiles(all_input_filenames, tokens_occ, tokens_per_file):
    i = 0
    for input_filename in all_input_filenames:
        tokens_occ, tokens_per_file = tokenize(directory_input, input_filename, 
                                               tokens_occ, tokens_per_file)
        # Check on progress
        print(i)
        i += 1
    return tokens_occ, tokens_per_file
 
def showResults(sorted_d, nb_sup_10):
    # Show the most occuring word and number of wiki words   
    print(list(sorted_d.keys())[0], list(sorted_d.values())[0])
    print("\nNumber of wiki words:", len(tokens_occ))       
    print(nb_sup_10)
    print("Portion:", nb_sup_10/len(tokens_occ))


  
# PATHS
wiki_filename = "all_wiki_words_sorted_per_occ.txt"
directory_input = "../reddit/"
#input_file = "2006-01-humanities-students-student-major-majoring-majors_0.txt"

tokens_occ = defaultdict(lambda: 0)
tokens_per_file = []

all_input_filenames = os.listdir(directory_input)

tokens_occ, tokens_per_file = tokenizeAllFiles(all_input_filenames, tokens_occ, tokens_per_file)
sorted_d = dict(sorted(tokens_occ.items(), key=operator.itemgetter(1),reverse=True))
nb_sup_10 = writeVocabularyFiles(wiki_filename, sorted_d)

showResults(sorted_d, nb_sup_10)

