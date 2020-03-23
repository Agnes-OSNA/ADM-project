import os
from nltk.tokenize import word_tokenize
from collections import defaultdict

def tokenize(directory_input, input_file, tokens_occ, tokens_per_file):
    with open(os.path.join(directory_input, input_file), "rt") as f:
        tokens = word_tokenize(f.read())
        # Keep all tokens of all files
        tokens_per_file.append(tokens)
        # Count occurences per token
        for token in tokens:
            tokens_occ[token] += 1
    return tokens_occ, tokens_per_file

def writeVocabularyFiles(vocab_filename, wiki_filename, tokens_occ):
    vocab_file = open(vocab_filename, 'w')
    wiki_file = open(wiki_filename, 'w')
    for word in sorted(tokens_occ):
        vocab_file.write(str(word) + "\n")
        if word.startswith("Wiki_"):
            wiki_file.write(str(word) + "\n")

        
  
# PATHS
vocab_filename = "unique_words.txt"
wiki_filename = "wiki_words.txt"
directory_input = "./reddit/"
input_file = "2006-01-humanities-students-student-major-majoring-majors_0.txt"

tokens_occ = defaultdict(lambda: 0)
tokens_per_file = []

tokens_occ, tokens_per_file = tokenize(directory_input, input_file, tokens_occ, 
                                       tokens_per_file)
writeVocabularyFiles(vocab_filename, wiki_filename, tokens_occ)