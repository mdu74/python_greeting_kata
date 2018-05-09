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
    def _(names):
        if len(names) > 1:
            nameAtTheEnd = names[-1]
            del names[-1]
            joinNamesByCommas = ", ".join(names)
            return "Hello, " + joinNamesByCommas + " and " + nameAtTheEnd