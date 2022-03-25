# Problem 6: Union and Intersection

## Reason
- Union: Since we want all unique elements in two lists, here use set to traverse two lists and get all elements from two lists without duplicates, and create the linked list for output from the set.
- Intersection: For intersection, use same way to traverse two lists separately and store the unique element from two lists using set, and get the intersection of two sets. Then create the output LinkedList

## Efficiency

- Time complexity
  - Union: O(n), add and append take constant O(1) time, and need to do the same operation n times, where n is the total number of nodes
  - Intersection: O(n),  add and append take constant O(1) time, and need to do the same operation n times, where n is the total number of nodes

- Space complexity
- Union: O(n), where n is the total number of nodes
- Intersection: O(n), where n is the total number of nodes
