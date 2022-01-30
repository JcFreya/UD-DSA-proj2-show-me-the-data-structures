'''
design a data structure known as a Least Recently Used (LRU) cache
All operations must take O(1) time.
    In case of a cache hit, your get() operation should return the appropriate value.
    In case of a cache miss, your get() should return -1.
While putting an element in the cache, put() / set() operation will insert the element if the key is not present.
If the cache is full, removes the least recently used entry first and then insert the element.
'''

from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.max_capacity = capacity
        self.cache_data = {}
        self.cache_order = deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key is None:
            return -1
        return self.cache_data.get(key, -1)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        # check empty capacity
        if self.max_capacity == 0:
            print("Error: Cache capacity need to be greater than 0")
            return

        # print('cache size ', len(self.cache_order))
        if len(self.cache_order) == self.max_capacity:
            rm_elem = self.cache_data[self.cache_order.popleft()]
            # print(rm_elem,'deleted')
            del self.cache_data[rm_elem]
        self.cache_order.append(key)
        self.cache_data[key] = value

print('----------Test1----------')
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache.set(7, 7)

print(our_cache.get(1))      # returns -1 because the cache reached it's capacity and 1 was the least recently used entry
print(our_cache.get(2))      # returns -1 because the cache reached it's capacity and 2 was the least recently used entry


print('----------Test2----------')
our_cache = LRU_Cache(3)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)

our_cache.set(1, 4) # because the cache reached it's capacity and 1 will be removes since it was the least recently used entry
our_cache.set(2, 5) # because the cache reached it's capacity and 2 will be removes since it was the least recently used entry
our_cache.set(3, 6) # because the cache reached it's capacity and 3 will be removes since it was the least recently used entry

print(our_cache.get(1))       # returns 4
print(our_cache.get(2))       # returns 5
print(our_cache.get(3))      # returns 6

print(our_cache.get(6))      # returns -1 because 6 is not present in the cache


print('----------Test3----------')
our_cache = LRU_Cache(0) # pop error when setting value on 0 capcacity

our_cache.set(1, 1)    # Error: Cache capacity need to be greater than 0

print(our_cache.get(1))     # returns -1 because 1 is not present in the cache
