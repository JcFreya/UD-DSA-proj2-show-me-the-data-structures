'''
# Problem 5: Blockchain
Use linked lists and hashing to create a blockchain implementation.

A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
This blockchain implementation will be using a SHA-256 hash, the Greenwich Mean Time when the block was
created, and text strings as the data.

'''

import hashlib
import datetime as dt

class Block:
    def __init__(self, timestamp, data, previous_hash):
        # check empty Input
        if data is None:
            print("Error: Data input couldn't be None\n")
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)


    def calc_hash(self, hash_str):
        """
        Hash the information to store in the block chain such as transaction time,
        data, and information like the previous chain.
        """
        sha = hashlib.sha256()
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        return "timestamp: {}\ndata: {}\nhash: {}\nprevious hash: {}\n"\
            .format(self.timestamp, self.data, self.hash, self.previous_hash, )

class Blockchain():
    def __init__(self):
        self.head = None
        self.last = None
        self.link = dict()

    def add_block(self, data):
        # check None input
        if data is None:
            print("Error: Input data couldn't be None\n")
            return

        if not self.head:
            self.head = Block(self.get_utc_time(), data, 0)
            self.last = self.head
            self.link[self.last.hash] = self.last
        else:
            new_block = Block(self.get_utc_time(), data, self.last.hash)
            self.link[new_block.hash] = new_block
            self.last = new_block


    def get_utc_time(self):
        return dt.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")


    def print_blockchain(self):
        curr = self.last
        while True:
            print(curr)
            if curr.previous_hash == 0:
                break

            curr = self.link[curr.previous_hash]


print('----------Test1----------')
# test add creat blockchain and add block
block_chain = Blockchain()
block_chain.add_block("block1")
block_chain.add_block("block2")
block_chain.print_blockchain()
print('\n')

print('----------Test2----------')
# test add block with None value
block_chain = Blockchain()
block_chain.add_block("block1")
block_chain.add_block(None)
block_chain.print_blockchain()
print('\n')

print('----------Test3----------')
# test add block with empty value
block_chain = Blockchain()
block_chain.add_block("block1")
block_chain.add_block("")
block_chain.print_blockchain()
print('\n')
