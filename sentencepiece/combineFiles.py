import os
import re

all_input_filenames = os.listdir("../reddit/")

all_data = ""
for file in all_input_filenames:
    with open(os.path.join("../reddit/", file), encoding="utf-8") as fp: 
        data = fp.read()
        all_data += data
        all_data += "\n"

words = []
with open ('all_files.txt', 'w', encoding="utf-8") as fp:
    for line in all_data.split("\n"):
        for word in line.split():
            word = re.sub(r"^\W+", "", word)
            word = re.sub(r"\W+$", "", word)
            words.append(word)
    fp.write(all_data) 
    
uniq_words= set(words)
print(len(uniq_words))
print(sorted(uniq_words))