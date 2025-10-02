# Unit tests for algorithms
# Install pytest module to run
# pip install pytest
# use command "pytest" to run the unit tests

from lcp_linear_search import LCPLinearSearch
from lcp_binary_search import LCPBinarySearch
import pytest

# TODO: More tests

tests = []
answers = []

# Test #1
tests.append( ["a", "a", "b", "b"] )
answers.append( [False, True, False, True] )

# Test #2
tests.append( ["a", "b", "a", "c", "b", "c"] )
answers.append( [False, False, True, False, True, True] )

# Test #3
# ["a", "b", "c", ..., "x", "y", "z"]
tests.append( [chr(ord("a") + i) for i in range(26)] ) 
answers.append( [False for i in range(26)] )

def test_lcp_linear_search():
    for i in range(len(tests)): 
        current_test = tests[i]
        linear_search = LCPLinearSearch()

        for item in current_test:
            if not linear_search.check(item):
                linear_search.add(item)
        assert linear_search.show_history() == answers[i]

def test_lcp_binary_search():
    for i in range(len(tests)): 
        current_test = tests[i]
        binary_search = LCPBinarySearch()

        for item in current_test:
            if not binary_search.check(item):
                binary_search.add(item)
        assert binary_search.show_history() == answers[i]