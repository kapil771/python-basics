def decoratorkapil(myFunc):
    def insideDecorator(*args):
        print('insideDecorator Function executed before {}'.format(myFunc.__name__))
        return myFunc(*args)
    return insideDecorator

@decoratorkapil      # Decorator function that takes below function as an argument
def display(*args):
    '''  This function is passed as an argument to the decorator function specified above after @ sign '''
    print('In display function')
    print(*args)

display('Hello','Hi',123)

display('Hello2','Hi2',1232)