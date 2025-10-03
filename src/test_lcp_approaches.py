# Unit tests for algorithms
# Install pytest module to run
# pip install pytest
# use command "pytest" to run the unit tests

from lcp_linear_search import LCPLinearSearch
from lcp_binary_search import LCPBinarySearch
from lcp_hash_table import LCPHashTable
from lcp_bloom_filter import LCPBloomFilter
from lcp_cuckoo_filter import LCPCuckooFilter
import pytest

# TODO: More/better tests with edge cases

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

# Testing Bloom Filter Approach
def test_lcp_bloom_filter():
    n = 20 # number of items to add
    p = 0.05 # false positive probability
    
    bloom_filter = LCPBloomFilter(n, p)

    # No item has been added
    current_test = tests[2] # ["a", "b", "c", ..., "x", "y", "z"]
    for item in current_test:
        assert not bloom_filter.check(item)

    # Add items and check in the filter (no false negatives)
    current_test = tests[2] # ["a", "b", "c", ..., "x", "y", "z"]
    for item in current_test:
        if not bloom_filter.check(item):
            bloom_filter.add(item)
        assert bloom_filter.check(item)

    # TODO: test on more words to see false positive probability
    '''
    for item in current_test:
        if not bloom_filter.check(item):
            bloom_filter.add(item)
    number_of_positives = bloom_filter.show_history().count(True)
    number_of_false_positives = number_of_positives - answers[i].count(True)
    assert number_of_false_positives / number_of_positives <= p
    '''
    
# Testing Cuckoo Filter Approach
def test_lcp_cuckoo_filter():
    n = 40 # number of items to add
    b = 4 # bucket size
    fb = 8 # fingerprint size
    k = 500 # max number of kicks
    
    cuckoo_filter = LCPCuckooFilter(n, b, fb, k)

    # No item has been added
    current_test = tests[2] # ["a", "b", "c", ..., "x", "y", "z"]
    for item in current_test:
        assert not cuckoo_filter.check(item)

    # Add items and check in the filter (no false negatives)
    current_test = tests[2] # ["a", "b", "c", ..., "x", "y", "z"]
    for item in current_test:
        if not cuckoo_filter.check(item):
            cuckoo_filter.add(item)
        assert cuckoo_filter.check(item)

    # TODO: test on more words to see false positive probability
    '''
    for item in current_test:
        if not cuckoo_filter.check(item):
            cuckoo_filter.add(item)
    number_of_positives = cuckoo_filter.show_history().count(True)
    number_of_false_positives = number_of_positives - answers[i].count(True)
    assert number_of_false_positives / number_of_positives <= p
    '''