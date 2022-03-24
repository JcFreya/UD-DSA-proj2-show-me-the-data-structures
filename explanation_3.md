# Problem 3: Huffman Coding

## Reason
Since we need to build the tree by order of character frequency, here will use priority queue(heapq) to implement Huffman coding, with base structure using binary tree where the node with the lowest frequency has the highest priority.

## Efficiency

- Time complexity  
  Encoding: O(nlog(n)), The priority queue takes O(log(n)) for each insertion(for sorting and finding the lowest probable nodes), the completely binary tree with n leaves has 2n-1 nodes.Since the Huffman is building completely binary tree, where n is the number of characters.

- Space complexity
  O(n) where n is the number of characters
