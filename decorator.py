def greet(fun):

    def warpper(name):
        print('Hello')
        fun(name)
        print('nice to meet you')

    return warpper

name = input('Your name : ')

@greet
def myName(name):
    print(name)

myName(name)