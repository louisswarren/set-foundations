from pytrace.trace import *

from axioms import *
from definitions import *

@trace(show_counter=False, show_types=False)
def test_eq(left, right, expected=True):
    result = (left == right)
    assert(result == expected)
    return result


test_eq(UnorderedPair(1, 2), UnorderedPair(2, 1))
test_eq(OrderedPair(1, 2), OrderedPair(1, 2))
test_eq(OrderedPair(1, 2), OrderedPair(2, 1), False)

