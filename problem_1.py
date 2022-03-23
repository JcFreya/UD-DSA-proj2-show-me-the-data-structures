'''
Design a data structure known as a Least Recently Used (LRU) cache.

- All operations must take O(1) time.
- When cache hit, get() operation returns the appropriate value.
- When cache miss, get() returns -1.
- While putting an element in the cache, put() / set() operation must insert the
element. If the cache is full, removes the least recently used entry first and
then insert the new element.
For the current problem, consider the size of cache = 5.
'''

from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity=None):
        # Initialize class variables
        self.max_capacity = capacity # set max capacity
        self.cache_data = {} # store key,value pairs
        self.cache_order = deque() # track the order of key,value insert

    def get(self, key):
        """
        Retrieve item from provided key. Return -1 if nonexistent.
        Input:
            self, key value
        Output:
            value: value of input key (-1 if input key not exists)
        """
        if key is None:
            return -1
        return self.cache_data.get(key, -1) # return -1 if key not exists

    def set(self, key, value):
        """
        Set the value if the key is not present in the cache.
        If the cache is at capacity remove the oldest item.
        Input:
            self, key, value
        """
        # check none max_capacity
        if self.max_capacity is None:
            print("Error: Cache capacity couldn't be None")
            return

        # check empty capacity
        if self.max_capacity <= 0:
            print("Error: Cache capacity need to be greater than 0")
            return

        # check the key
        if key is None:
            print("Error: Key couldn't be None")
            return

        # check max_capacity and insert values
        if len(self.cache_order) == self.max_capacity:
            print("\nHit the max capacity")

            # remove the least recently used entry
            rm_lru = self.cache_data[self.cache_order.popleft()] # pop the oldest
            print('(', rm_lru, ', ', self.cache_data[rm_lru],') deleted\n')
            del self.cache_data[rm_lru]

        self.cache_order.append(key) # track the order of key,value insert
        self.cache_data[key] = value
        print('(', key, ', ', value, ') inserted')


print('----------Test1----------')
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print('Get value of 1: ', our_cache.get(1))       # returns 1
print('Get value of 2: ', our_cache.get(2))       # returns 2
print('Get value of 9: ', our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)     # Hit the max capacity. 1 ,  1  deleted
our_cache.set(7, 7)     # Hit the max capacity. 2 ,  2  deleted

print('Get value of 1: ', our_cache.get(1))      # returns -1 because (1,1) has been removed when the cache reached it's capacity
print('Get value of 2: ', our_cache.get(2))      # returns -1 because (2,2) has been removed when the cache reached it's capacity
print('\n')

print('----------Test2----------')
our_cache = LRU_Cache(3)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)

our_cache.set(1, 4) # Hit the max capacity. 1 ,  1  deleted
our_cache.set(2, 5) # Hit the max capacity. 2 ,  2  deleted
our_cache.set(3, 6) # Hit the max capacity. 3 ,  3  deleted

print('Get value of 1: ', our_cache.get(1))     # returns 4
print('Get value of 2: ', our_cache.get(2))     # returns 5
print('Get value of 3: ', our_cache.get(3))     # returns 6

print('Get value of 6: ', our_cache.get(6))      # returns -1 because 6 is not present in the cache
print('\n')

print('----------Test3----------')
# test None max_capacity
our_cache = LRU_Cache()     # Error: Cache capacity couldn't be None
our_cache.set(1, 1)

# test 0 max_capacity
our_cache = LRU_Cache(0)    # Error: Cache capacity need to be greater than 0
our_cache.set(1, 1)

# test none key
our_cache = LRU_Cache(2)
our_cache.set(None, 2)      # Error: Key couldn't be None

print(our_cache.get(1))     # returns -1
print('\n')
