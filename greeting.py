from functools import singledispatch

class Greeting():
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
        nameAtTheEnd = names[-1]
        shouted = ""

        for name in names:
            if name.isupper():
                shouted = ". AND " + name
                names.remove(name)

        del names[-1]
        joinNamesByCommas = ", ".join(names) 

        return "Hello, " + joinNamesByCommas + " and " + nameAtTheEnd + shouted