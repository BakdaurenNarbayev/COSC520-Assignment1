# Unit tests for algorithms
# Install pytest module to run
# pip install pytest
# use command "pytest" to run the unit tests

from lcp_linear_search import LCPLinearSearch
from lcp_binary_search import LCPBinarySearch
from lcp_hash_table import LCPHashTable
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

# Testing Linear Search Approach
def test_lcp_linear_search():
    for i in range(len(tests)): 
        current_test = tests[i]
        linear_search = LCPLinearSearch()

        for item in current_test:
            if not linear_search.check(item):
                linear_search.add(item)
        assert linear_search.show_history() == answers[i]

# Testing Binary Search Approach
def test_lcp_binary_search():
    for i in range(len(tests)): 
        current_test = tests[i]
        binary_search = LCPBinarySearch()

        for item in current_test:
            if not binary_search.check(item):
                binary_search.add(item)
        assert binary_search.show_history() == answers[i]

# Testing Hash Table Approach
def test_lcp_hash_table():
    for i in range(len(tests)): 
        current_test = tests[i]
        hash_table = LCPHashTable(11)

        for item in current_test:
            if not hash_table.check(item):
                hash_table.add(item)
        assert hash_table.show_history() == answers[i]