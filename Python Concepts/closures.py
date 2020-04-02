def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction

myFunction = outerFunction('Test')
myFunction()