# Problem 1: LRU Cache

## Reason
In order to make all operations to O(1) time, here decide to use dictionary to store the (key, value) pairs. We also need to track the order of elements being inserted so that we can remove the least recently used when hitting the max_capacity, to achieve this we use deque in python collections module to reach O(1) when moving the oldest element. In other word, we track the order of elements being inserted in deque, and retrieve the key in order and get the value of that key from dictionary.

## Efficiency

- Time complexity
  - get: O(1), traverse and get values through dictionary takes constant time
  - set: O(1), access the value, move elements with deque both take constant time

- Space complexity
  - get: O(1) use constant memory when getting a value
  - set: O(n) where n is the capacity since we create that big dictionary to store the data
