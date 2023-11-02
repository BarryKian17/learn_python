# file = open('./text.txt')

# for line in file:
#     print(line)


# lineList = file.readlines()
# print(lineList)

# file.seek(50)

# para = str(file.read(150))

# print(para)

with open('./text.txt') as file:
    for line in file:
        print(line)

print('Test over')