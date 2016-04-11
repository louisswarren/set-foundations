class mzf:
    def __contains__(self, x):
        raise NotImplementedError

class Indeterminate(Exception):
    pass

class UnorderedPair(mzf):
    def __init__(self, x, y):
        self.values = (x, y)
        self.args = (x, y)

    def __contains__(self, x):
        return x in self.values

    def __eq__(self, other):
        if isinstance(other, UnorderedPair):
            return (all(x in other.values for x in self.values) and
                    all(y in self.values for y in other.values))
        raise Indeterminate

    def __repr__(self):
        return "UnorderedPair({}, {})".format(*self.args)

    def __str__(self):
        return "{{{}, {}}}".format(*self.args)

class Extension(mzf):
    def __init__(self, domain, concept):
        self.domain = domain
        self.concept = concept

    def __contains__(self, x):
        return x in self.domain and self.concept(x)

class _NaturalSet(mzf):
    def __contains__(self, x):
        try:
            return int(x) and x >= 0
        except ValueError:
            return False

Naturals = _NaturalSet()

