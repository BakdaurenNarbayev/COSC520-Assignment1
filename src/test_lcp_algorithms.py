# Unit tests for algorithms
# Install pytest module to run
# pip install pytest
# use command "pytest" to run the unit tests

from lcp_algorithms import binary_search, hashing, bloom_filter, cuckoo_filter
from lcp_linear_search import LCPLinearSearch
import pytest

# TODO: More tests

tests = []
answers = []

# ["a", "b", "c", ..., "x", "y", "z"]
tests.append( [chr(ord("a") + i) for i in range(26)] ) 
answers.append( [False for i in range(26)] )

tests.append( ["a", "a", "b", "b"] )
answers.append( [False, True, False, True] )

def test_lcp_algorithms():
    for i in range(len(tests)): 
        current_test = tests[i]

        linear_search = LCPLinearSearch()
        for item in current_test:
            if not linear_search.check(item):
                linear_search.add(item)
        assert linear_search.show_history() == answers[i]
        # assert binary_search(tests[i]) == answers[i]
        # assert hashing(tests[i]) == answers[i]
        # assert bloom_filter(tests[i]) == answers[i]
        # assert cuckoo_filter(tests[i]) == answers[i]