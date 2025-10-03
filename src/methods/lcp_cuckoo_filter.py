# LCP Cuckoo Filter Approach
# Based on: https://www.cs.cmu.edu/~dga/papers/cuckoo-conext2014.pdf

# Install mmh3 module first
# pip install mmh3

import math
import random
import mmh3

class LCPCuckooFilter(object):
    '''
    Class for Cuckoo Filter
    '''
    def __init__(self, items_count, bucket_size, fingerprint_bits, max_number_of_kicks):
        '''
        items_count : int
            Number of items expected to be stored in cuckoo filter
        bucket_size : int
            The size of a backet (max number of fingerprints)
        fingerprint_bits: int
            The number of bits used to store fingerprints
        max_number_of_kicks: int
            The maximum number of allowed kicks from the buckets
            when looking for a slot for a new item and 
            iteratively kicking previous items
        '''
        self.items_count = items_count
        self.table_size = math.ceil(items_count / bucket_size / 0.95) # Allow for extra room
        self.bucket_size = bucket_size
        self.fingerprint_bits = fingerprint_bits
        self.max_number_of_kicks = max_number_of_kicks

        # Used to calculate fingerprint
        self.fingerprint_mask = (1 << fingerprint_bits) - 1

        # Hash table of fingerprints (e.g., of logins)
        self.fingerprints = [[] for i in range(self.table_size)]

    def hash(self, val):
        '''
        Simple hash function using MurmurHash
        '''
        return mmh3.hash(val)

    def fingerprint(self, item):
        '''
        Determine fingerprint of an item using
        hash function and fingerprint mask
        '''
        return self.hash(item) & self.fingerprint_mask
    
    def find_indices(self, item):
        # Calculate fingerprint f, bucket indeces i1 and i2
        f = self.fingerprint(item)
        i1 = self.hash(item) % self.table_size
        # Convert integer to bytes (4 bytes, big-endian)
        fB = f.to_bytes(4, byteorder='big')
        i2 = (i1 ^ self.hash(fB)) % self.table_size
        return f, i1, i2

    def add(self, item):
        '''
        Add an item in the filter if it is new
        '''
        if not self.check(item):
            f, i1, i2 = self.find_indices(item)

            # If one of those buckets has an available slot, add/insert item there
            if len(self.fingerprints[i1]) < self.bucket_size:
                self.fingerprints[i1].append(f)
                return True
            
            if len(self.fingerprints[i2]) < self.bucket_size:
                self.fingerprints[i2].append(f)
                return True
            
            # If both buckets are full, choose one randomly and
            # swap a random item in that bucket with new item and
            # check second bucket for kicked item, and
            # if spot is available insert it there, otherwise
            # repeat this process until max number of kicks reached
            i = random.choice([i1, i2])
            for n in range(self.max_number_of_kicks):
                idx = random.randrange(len(self.fingerprints[i]))
                e = self.fingerprints[i][idx]
                self.fingerprints[i][idx] = f
                f = e
                # Convert integer to bytes (4 bytes, big-endian)
                fB = f.to_bytes(4, byteorder='big')
                i = (i ^ self.hash(fB)) % self.table_size
                if len(self.fingerprints[i]) < self.bucket_size:
                    self.fingerprints[i].append(f)
                    return True
                # If no spot found, consider the table as full, i.e. insertion failed
                return False
        # If item is already here
        return False

    def check(self, item):
        '''
        Check for existence of an item in the filter
        by checking buckets associated with it, and update history
        '''
        f, i1, i2 = self.find_indices(item)

        # Combine buckets and check for the fingerprint
        buckets = self.fingerprints[i1] + self.fingerprints[i2]
        for bucket_item in buckets:
            if bucket_item == f:
                return True
        return False