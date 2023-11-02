# with open('./about.txt','w') as file:
#     file.write('hello')
#     file.write('\nhow are you')
#     file.write("\nI'm under the water")

# with open('./about.txt','a') as file:
#     file.write('hello')
#     file.write('\nhow are you')
#     file.write("\nI'm under the water")


lists = ['Hello Brofdrt','\n You must be joking']

with open('./about.txt','a') as file:
    file.writelines(lists)