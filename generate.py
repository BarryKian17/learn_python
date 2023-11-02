with open('./text.txt') as file:
    para = file.read()

    paraCount = int(input('Count : '))

    for count in range(paraCount):
        with open('./generate.txt','a') as write_file:
            write_file.write(para+'\n\n')