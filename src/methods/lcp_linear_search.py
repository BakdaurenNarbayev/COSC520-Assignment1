# LCP Linear Search Approach

class LCPLinearSearch(object):
    '''
    Class for Linear Search
    '''
    def __init__(self):
        # List of used items (e.g., logins)
        self.items = []

    def add(self, item):
        '''
        Add an item to the list if it is new
        '''
        if not self.check(item):
            self.items.append(item)

    def check(self, item):
        '''
        Check for existence of an item in the list
        by going through all items
        '''
        for _item in self.items:
            if _item == item:
                return True
        return False