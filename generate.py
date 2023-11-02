words = ['apple','orange','mango','lime']

from random import randint;

def sentenceMix(word):
    random_index = randint(0,len(words)-1)
    return f'{words[random_index]} {word} '

with open('./text.txt') as file:
    para = file.read()
    wordList = para.split()
    mix_para = list(map(sentenceMix,wordList))
    paraCount = int(input('Count : '))

    for count in range(paraCount):
        with open('./generate.txt','a') as write_file:
            write_file.write(','.join(mix_para) +'\n\n')