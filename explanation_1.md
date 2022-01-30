# Problem 1: LRU Cache

## Reason
In order to make all operations to O(1) time, here decide to use dictionary. We also need to track the first and last element, to achieve this we use deque in python collections module so that we can reach O(1) when moving the element. In other word, we keep the order of elements in deque, and retrieve the key in order and get the value of that key from dictionary.

## Efficiency

- Time complexity
  - get: O(1)
  - set: O(1)


accessing and setting the values through a dictionary takes constant time.
accessing the first and last element is constant time as well using the head and tail of the deque.
rearranging the elements when we want to move something to the top or drop an element is also constant time because we are using a doubly linked list


- Space complexity
  - set: O(n) where n is the capacity since we create that big dictionary to store the data
  - get: O(1) use constant memory when getting a value
