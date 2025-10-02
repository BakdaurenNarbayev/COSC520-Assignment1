# LCP Hash Table Approach with Separate Chaining

class LCPHashTable(object):
    '''
    Class for Hash Table
    '''
    def __init__(self, size):
        # Size of the hash table
        self.size = size

        # Hash table of used items (e.g., logins)
        self.items = [[] for i in range(size)]

        # History of checks
        # True if checked item is already in the list, 
        # and False if it is not
        self.history = []

    def hash(self, item):
        '''
        Simple hash function using built-in hash funtion and size of the table
        '''
        return hash(item) % self.size

    def add(self, item):
        '''
        Add an item to the hash table using hash value
        '''
        self.items[self.hash(item)].append(item)

    def check(self, item):
        '''
        Check for existence of an item in the hash table
        by checking bucket associated with hash value, and update history
        '''
        bucket = self.items[self.hash(item)]

        for bucket_item in bucket:
            if bucket_item == item:
                self.history.append(True)
                return True
        
        self.history.append(False)
        return False
        
    def show_history(self):
        '''
        Show history of calls to funtion "check" and corresponding results
        '''
        return self.history