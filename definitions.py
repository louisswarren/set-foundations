from axioms import *

class Singleton(UnorderedPair):
    def __init__(self, x):
        self.internal = UnorderedPair(x, x)
        self.values = self.internal.values
        self.args = (x, )

    def __contains__(self, x):
        return x in self.internal

    def __repr__(self):
        return "Singleton({})".format(*self.args)

    def __str__(self):
        return "{{}}".format(*self.args)

class OrderedPair(UnorderedPair):
    def __init__(self, x, y):
        self.internal = UnorderedPair(Singleton(x), UnorderedPair(x, y))
        self.values = self.internal.values
        self.args = (x, y)

    def __contains__(self, x):
        return x in self.internal

    def __repr__(self):
        return "OrderedPair({}, {})".format(*self.args)

    def __str__(self):
        return "<{}, {}>".format(*self.args)

