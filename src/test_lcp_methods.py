# Unit tests for LCP Methodes
# Install pytest module to run
# pip install pytest
# use command "pytest" to run the unit tests

from methods.lcp_linear_search import LCPLinearSearch
from methods.lcp_binary_search import LCPBinarySearch
from methods.lcp_hash_table import LCPHashTable
from methods.lcp_bloom_filter import LCPBloomFilter
from methods.lcp_cuckoo_filter import LCPCuckooFilter

from utils.string_generation import generate_strings

import pytest

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
answers.append( [False for _ in range(26)] )

# Testing Linear Search Method
def test_lcp_linear_search():
    for i in range(len(tests)): 
        current_test = tests[i]
        linear_search = LCPLinearSearch()

        for j in range(len(current_test)):
            item = current_test[j]
            assert linear_search.check(item) == answers[i][j]
            if not linear_search.check(item):
                linear_search.add(item)
        assert len(linear_search.items) == answers[i].count(False)

# Testing Binary Search Method
def test_lcp_binary_search():
    for i in range(len(tests)): 
        current_test = tests[i]
        binary_search = LCPBinarySearch()

        for j in range(len(current_test)):
            item = current_test[j]
            assert binary_search.check(item) == answers[i][j]
            if not binary_search.check(item):
                binary_search.add(item)
        assert len(binary_search.items) == answers[i].count(False)

# Testing Hash Table Method
def test_lcp_hash_table():
    for i in range(len(tests)): 
        current_test = tests[i]
        hash_table = LCPHashTable(11)

        for j in range(len(current_test)):
            item = current_test[j]
            assert hash_table.check(item) == answers[i][j]
            if not hash_table.check(item):
                hash_table.add(item)
        assert len(hash_table.items) == answers[i].count(False)

# Testing Bloom Filter Method
def test_lcp_bloom_filter():
    n = 26 # number of items to add
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

    # Test on more words to see false positive probability
    n = 1000000
    bloom_filter = LCPBloomFilter(n, p)

    current_test = generate_strings(n, 6)
    inserted_set = set()
    
    for item in current_test:
        if not bloom_filter.check(item):
            bloom_filter.add(item)
            inserted_set.add(item)

    # Measure false positive rate with new random strings
    false_positive_count = 0

    new_random_strings = generate_strings(10000, 6)

    for item in new_random_strings:
        if item not in inserted_set and bloom_filter.check(item):
            false_positive_count += 1

    assert false_positive_count / len(new_random_strings) <= p
    
# Testing Cuckoo Filter Method
def test_lcp_cuckoo_filter():
    n = 40 # number of items to add
    b = 4 # bucket size
    fb = 8 # fingerprint size
    k = 500 # max number of kicks
    p = 0.05 # false positive probability
    
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

    # Test on more words to see false positive probability
    n = 1000000
    fb = 12 # fingerprint size
    cuckoo_filter = LCPCuckooFilter(n, b, fb, k)

    current_test = generate_strings(n, 6)
    inserted_set = set()
    
    for item in current_test:
        if not cuckoo_filter.check(item):
            if cuckoo_filter.add(item): # if insertion succeded
                inserted_set.add(item)

    # Measure false positive rate with new random strings
    false_positive_count = 0

    new_random_strings = generate_strings(10000, 6)

    for item in new_random_strings:
        if item not in inserted_set and cuckoo_filter.check(item):
            false_positive_count += 1

    assert false_positive_count / len(new_random_strings) <= p