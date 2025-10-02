from lcp_algorithms import linear_search, binary_search, hashing, bloom_filter, cuckoo_filter
import pytest

# TODO: More tests

tests = []
answers = []

tests.append( [chr(ord("a") + i) for i in range(26)] ) # i.e., ["a", "b", "c", ..., "x", "y", "z"]
answers.append( [0 for i in range(26)] )

tests.append( ["a", "a", "b", "b"] )

def test_lcp_algorithms():
    for i in range(len(tests)): 
        assert linear_search(tests[i]) == answers[i]
        # assert binary_search(tests[i]) == answers[i]
        # assert hashing(tests[i]) == answers[i]
        # assert bloom_filter(tests[i]) == answers[i]
        # assert cuckoo_filter(tests[i]) == answers[i]