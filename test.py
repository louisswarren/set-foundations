from pytrace.trace import trace

from axioms import *
from definitions import *

import itertools

@trace()
def trace_eq(left, right, expected=True):
    result = (left == right)
    return result

def test_eq(left, right, expected=True):
    result = trace_eq(left, right, expected)
    assert(result == expected)

test_eq(UnorderedPair(1, 2), UnorderedPair(2, 1))
test_eq(OrderedPair(1, 2), OrderedPair(1, 2))
test_eq(OrderedPair(1, 2), OrderedPair(2, 1), False)

evens = Sequence(lambda x: x * 2)
test_eq(list(itertools.islice(evens, 5)), [0, 2, 4, 6, 8])
