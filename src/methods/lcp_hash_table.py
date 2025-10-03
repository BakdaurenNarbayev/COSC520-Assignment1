# LCP Hash Table Approach with Separate Chaining

# Install mmh3 module first
# pip install mmh3

import mmh3

class LCPHashTable(object):
    '''
    Class for Hash Table
    '''
    def __init__(self, size):
        '''
        size : int
            Number of buckets in the hash table
        '''
        # Size of the hash table
        self.size = size

        # Hash table of used items (e.g., logins)
        self.items = [[] for _ in range(size)]

    def hash(self, item):
        '''
        Simple hash function using MurmurHash and size of the table
        '''
        return mmh3.hash(item) % self.size

    def add(self, item):
        '''
        Add an item to the hash table if it is new
        '''
        if not self.check(item):
            self.items[self.hash(item)].append(item)

    def check(self, item):
        '''
        Check for existence of an item in the hash table
        by checking bucket associated with hash value
        '''
        bucket = self.items[self.hash(item)]
        for bucket_item in bucket:
            if bucket_item == item:
                return True
        return False