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

class Function(Extension):
    def __init__(self, domain, fmap):
        self.domain = domain
        self.fmap = fmap

    def __call__(self, arg):
        return self.fmap(arg)

    def __contains__(self, x):
        if not isinstance(x, OrderedPair):
            return False
        # Hacky check for simplicity
        if x.args[1] == self.fmap(x.args[0]):
            return True
        return False

class Sequence(Function):
    def __init__(self, fmap):
        self.fmap = fmap

    def __iter__(self):
        i = 0
        while True:
            yield self.fmap(i)
            i += 1
