from functools import singledispatch

class Greeting(object):
    @singledispatch
    def Greeter(name):
        if name == None:
            return "Hello, friend"
        elif name.isupper():
            return "HELLO, " + name
        else:
            return "Hello, " + name

    @Greeter.register(list)
    def _(name):
        if len(name) > 1:
            return "Hello, " + name[0] + " and " + name[1]