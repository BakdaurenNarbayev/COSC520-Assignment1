# LCP Binary Search Approach

class LCPBinarySearch(object):
    '''
    Class for Binary Search
    '''
    def __init__(self):
        # Sorted list of used items (e.g., logins)
        self.sorted_items = []

        # History of checks
        # True if checked item is already in the list, 
        # and False if it is not
        self.history = []

    def find_index(self, item):
        '''
        Find an index in the list (via binary search)
        where an item can be added 
        so that the list stays sorted
        '''
        # Left and right pointers to locate the index.
        # Aim to find left and right neighbor of the item to be inserted
        # Return left pointer as it is a potential index for the item
        left = 0
        right = len(self.sorted_items)
        while left < right:
            mid = (left + right) // 2
            mid_val = self.sorted_items[mid]
            # Return index immediately if match was found
            if item == mid_val:
                return mid
            elif item < mid_val:
                right = mid
            else:
                left = mid + 1
        return left

    def add(self, item):
        '''
        Add an item to the list at the appropriate index
        '''
        print(item)
        print(self.find_index(item))
        print(self.sorted_items)
        self.sorted_items.insert(self.find_index(item), item)
        print(self.sorted_items)

    def check(self, item):
        '''
        Check for existence of an item in the sorted list
        by finding its possible index using binary search, 
        and update history
        '''
        potential_index = self.find_index(item)
        # Check if potential index is within the list range 
        # and list item on that index is equal to item of interest
        if potential_index < len(self.sorted_items) and self.sorted_items[potential_index] == item:
            self.history.append(True)
            return True
        
        self.history.append(False)
        return False
        
    def show_history(self):
        '''
        Show history of calls to funtion "check" and corresponding results
        '''
        return self.history