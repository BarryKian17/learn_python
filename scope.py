# global scope
name = "Barry"

def myName() :
    global name;
    name = "kian"
    print(name)

myName()
print(name)