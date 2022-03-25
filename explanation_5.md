# Problem 5: Blockchain

## Reason
This blockchain implementation uses linked list and hashing to connect the blocks. Within each block, it stores information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.

## Efficiency

- Time complexity
  O(n), to add block with hashing process takes constant time O(1). But since we combine the information(data, timestamp, previous_hash) of block before hashing which takes O(n), and to traverse over the block chain also takes O(n) time

- Space complexity
  O(n), n is number of blocks in blockchain
