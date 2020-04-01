import sentencepiece as spm
import os

directory_input = "../reddit/"
all_input_filenames = os.listdir(directory_input)
input_file = all_input_filenames[0]
path = "../reddit/" + input_file
#test/botchan.txt

#spm.SentencePieceTrainer.Train('--input=../reddit/2006-01-humanities-students-student-major-majoring-majors_0.txt --model_prefix=m --vocab_size=190')
spm.SentencePieceTrainer.Train('--input=all_files.txt --model_prefix=m --vocab_size=3000 hard_vocab_limit=false')

sp = spm.SentencePieceProcessor()
sp.Load("m.model")
print(sp)

print(sp.EncodeAsPieces("I saw a girl with a telescope".encode('utf-8')))
print("\n", sp.EncodeAsPieces("I saw a girl with a telescope"))
print(sp.EncodeAsIds("I saw a girl with a telescope"))
print("\n", sp.EncodeAsPieces("I saw a girl with a telescope Wiki__Ivy_League__ifqls"))
print(sp.EncodeAsIds("I saw a girl with a telescope Wiki__Ivy_League__ifqls"))
print("\nFrom ID: ", sp.IdToPiece(10))

for n in range(5):
    print(sp.SampleEncodeAsPieces('Wiki__Ivy_League__ifqls', -1, 0.1))