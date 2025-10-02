# LCP Linear Search Algorithm

class LCPLinearSearch(object):
    '''
    Class for Linear Search
    '''
    def __init__(self):
        # List of used items (e.g., logins)
        self.items = []

        # History of checks
        # True if checked item is already in the list, 
        # and False if it is not
        self.history = []

    def add(self, item):
        '''
        Add an item to the list
        '''
        self.items.append(item)

    def check(self, item):
        '''
        Check for existence of an item in the list
        by going through all items, and update history
        '''
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.history.append(True)
                return True
        
        self.history.append(False)
        return False
        
    def show_history(self):
        '''
        Show history of calls to funtion "check" and corresponding results
        '''
        return self.history