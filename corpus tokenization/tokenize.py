import os
from nltk.tokenize import word_tokenize
from collections import defaultdict
import operator

def tokenize(directory_input, input_file, tokens_occ, tokens_per_file):
   with open(os.path.join(directory_input, input_file), "rt", encoding="utf-8") as f:
       tokens = word_tokenize(f.read())
       # Keep all tokens of all files
#       tokens_per_file.append(tokens)
       # Count occurences per token
       for token in tokens:
           if token.startswith("Wiki_"):
               tokens_occ[token] += 1
   return tokens_occ, tokens_per_file

def writeVocabularyFiles(vocab_filename, wiki_filename, sorted_d):
    # Write all unique words and unique wiki words in two files in alphabetic order
#    vocab_file = open(vocab_filename, 'w', encoding="utf-8")
    wiki_file = open(wiki_filename, 'w', encoding="utf-8")
    for word in sorted_d:
#    for word in sorted(tokens_occ):
#        vocab_file.write(str(word) + "\n")
#        if word.startswith("Wiki_"):
        wiki_file.write(str(word) + "\n")

def tokenizeAllFiles(all_input_filenames, tokens_occ, tokens_per_file):
    i=0
    for input_filename in all_input_filenames:
        tokens_occ, tokens_per_file = tokenize(directory_input, input_filename, 
                                               tokens_occ, tokens_per_file)
        # To check on progress
        print(i)
        i += 1
    return tokens_occ, tokens_per_file
        
  
# PATHS
vocab_filename = "unique_words.txt"
wiki_filename = "test_all_wiki_words_sorted_per_occ.txt"
directory_input = "../reddit/"
#input_file = "2006-01-humanities-students-student-major-majoring-majors_0.txt"

tokens_occ = defaultdict(lambda: 0)
tokens_per_file = []

all_input_filenames = os.listdir(directory_input)

#tokens_occ, tokens_per_file = tokenize("../sentencepiece/", "all_files.txt", tokens_occ, tokens_per_file)
#tokens_occ, tokens_per_file = tokenize(directory_input, input_file, tokens_occ, tokens_per_file)

tokens_occ, tokens_per_file = tokenizeAllFiles(all_input_filenames, tokens_occ, tokens_per_file)
sorted_d = dict(sorted(tokens_occ.items(), key=operator.itemgetter(1),reverse=True))
writeVocabularyFiles(vocab_filename, wiki_filename, sorted_d)

#for k, v in sorted_d.items():
#    print(k, v)
print("Number of wiki words:", len(tokens_occ))


