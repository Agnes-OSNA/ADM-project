def readWrite(filepath1, filepath2, filepath3):
    sw=[]
    bertList=[]
    # count1 = 0
    # count2 = 0
    # count3 = 0

    with open(filepath1) as singleFile:
        for line in singleFile:
            line = line.strip()
            sw.append(line)
            # count1 = count1 + 1
            # print(line)

    with open(filepath2) as multipleFile:
        for line in multipleFile:
            line = line.strip()
            sw.append(line)
            # count2 = count2 + 1
            # print(line)

    with open(filepath3, encoding="utf8") as bertFile:
        for line in bertFile:
            line = line.strip()
            word = line
            if line.startswith("[un") and len(sw) != 0:
                word =sw.pop(0)
            bertList.append(word)
    # print(count1, count2, count3)
    file1 = open('C:\KANYAAAAAA\Spring_2020\COURSES\AdvancedDM\PROJECT\BERT\BERT_MODEL_VOCABULARY\Result.txt', 'w', encoding="utf8")
    for x in bertList:
        x = x +"\n"
        file1.write(x)


if __name__ == '__main__':
    f1 = input("Enter the filepath 1")
    f2 = input("Enter the filepath 2")
    f3 = input("Enter the filepath 3")

    # f1 = "C:\KANYAAAAAA\Spring_2020\COURSES\AdvancedDM\PROJECT\BERT\BERT_MODEL_VOCABULARY\OneUncommonWord.txt"
    # f2 = "C:\KANYAAAAAA\Spring_2020\COURSES\AdvancedDM\PROJECT\BERT\BERT_MODEL_VOCABULARY\MultipleUncommonWords.txt"
    # f3 = "C:\KANYAAAAAA\Spring_2020\COURSES\AdvancedDM\PROJECT\BERT\BERT_MODEL_VOCABULARY\bert-base-uncased-vocab.txt"

    readWrite(f1, f2, f3)
