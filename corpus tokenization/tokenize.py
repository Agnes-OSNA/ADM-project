import os
from nltk.tokenize import word_tokenize
from collections import defaultdict

def tokenize(directory_input, input_file, tokens_occ, tokens_per_file):
   with open(os.path.join(directory_input, input_file), "rt", encoding="utf-8") as f:
       tokens = word_tokenize(f.read())
       # Keep all tokens of all files
       tokens_per_file.append(tokens)
       # Count occurences per token
       for token in tokens:
           tokens_occ[token] += 1
   return tokens_occ, tokens_per_file

def writeVocabularyFiles(vocab_filename, wiki_filename, tokens_occ):
    vocab_file = open(vocab_filename, 'w', encoding="utf-8")
    wiki_file = open(wiki_filename, 'w', encoding="utf-8")
    for word in sorted(tokens_occ):
        vocab_file.write(str(word) + "\n")
        if word.startswith("Wiki_"):
            wiki_file.write(str(word) + "\n")

def tokenizeAllFiles(all_input_filenames, tokens_occ, tokens_per_file):
    for input_filename in all_input_filenames:
        tokens_occ, tokens_per_file = tokenize(directory_input, input_filename, 
                                               tokens_occ, tokens_per_file)
        print(tokens_occ)
    return tokens_occ, tokens_per_file
        
  
# PATHS
vocab_filename = "unique_words.txt"
wiki_filename = "wiki_words.txt"
directory_input = "../reddit/"
input_file = "2006-01-humanities-students-student-major-majoring-majors_0.txt"

tokens_occ = defaultdict(lambda: 0)
tokens_per_file = []

all_input_filenames = os.listdir(directory_input)
tokens_occ, tokens_per_file = tokenize("../sentencepiece/", "all_files.txt", tokens_occ, tokens_per_file)
writeVocabularyFiles(vocab_filename, wiki_filename, tokens_occ)
print(sorted(tokens_occ))
print(len(tokens_occ))
