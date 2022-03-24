'''
# Problem 3: Huffman Coding
Implement the logic for both encoding and decoding of Huffman Coding compression algorithm.

A data compression algorithm reduces the amount of memory (bits) required to represent a message (data).
The compressed data, in turn, helps to reduce the transmission time from a sender to receiver.
The sender encodes the data, and the receiver decodes the encoded data.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data,
there is a loss (lossy) or no loss (lossless) of information.
The Huffman Coding is a lossless data compression algorithm.

references:
https://favtutor.com/blogs/huffman-coding
https://github.com/heineman/python-data-structures/blob/master/5.%20Heap-based%20Structures/huffman.py
https://www.techiedelight.com/huffman-coding/
https://towardsdatascience.com/introduction-to-python-heapq-module-53534feda625
'''

import sys
from collections import Counter
import heapq

class Node:

    def __init__(self, value, freq, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        self.freq = freq

    def __lt__(self, other):
        # use freq to compare the nodes in priority queue later
        return self.freq < other.freq

    def __str__(self):
        return self.left, self.right


def calculate_frequenct(data):
    # calculate the frequency for each character
    freq = dict(Counter(data))
    # sort the nodes by frequency ascending
    # sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return freq


def is_leaf(root):
    return root.left is None and root.right is None


def build_tree(freq):
    """
    Build the binary tree using the sorted character frequency queue
    Args:
        freq: sorted characted frequency queue
    Return:
        Root of the tree
    """
    # convert frequency list to nodes
    freq_queue = [Node(k, v) for k,v in freq.items()]
    heapq.heapify(freq_queue)

    # until the queue only has one element left
    while len(freq_queue) > 1:
        # remove two nodes with the highest priority(lowest frequency)
        left = heapq.heappop(freq_queue)
        right = heapq.heappop(freq_queue)
        # get the sum of two nodes' value
        sum_value = left.freq + right.freq
        # add in the new node
        heapq.heappush(freq_queue, Node(None, sum_value, left, right))

    root = freq_queue[0]

    return freq_queue, root


def encode_tree(node, bistring=''):
    """
    Traverse the tree and encode the tree with 0 and 1, return the mapping
    """
    # check None root
    if node is None:
        return

    # base case for Recursion
    if is_leaf(node):
        return {node.value: bistring}

    left = node.left
    right = node.right

    encoded_dict = dict() # store the code for each character
    encoded_dict.update(encode_tree(left, bistring + '0'))
    encoded_dict.update(encode_tree(right, bistring + '1'))
    return encoded_dict


def decode_data(node, idx, encoded_data):
    decoded_data = ''
    # check None node
    if node is None:
        return idx, decoded_data

    # when hit the leaf node
    if is_leaf(node):
        # print(node.value, end='')
        decoded_data += node.value
        return idx,  decoded_data

    idx += 1
    if encoded_data[idx] == '0':
        node = node.left
    else:
        node = node.right

    return decode_data(node, idx, encoded_data)


def huffman_encoding(data):

    # check input
    if data is None:
        print("Error: Input couldn't be None\n")
        return None, None

    # check empty input
    if len(str(data)) == 0:
        print("Error: Input is empty\n")
        return None, None

    # calculate the frequency for each character
    freq = calculate_frequenct(str(data))
    print('Frequency list: ', freq)

    # build the tree with sorted frequency, and get the root of tree
    tree, root = build_tree(freq)

    # encode the tree
    encoded_dict = encode_tree(root)

    print('Encode dictionary:')
    for i in encoded_dict:
        print(f'{i} : {encoded_dict[i]}')

    # mapping back to the code from tree to generate the encoded_data
    encoded_data = ''
    for char in str(data):
        encoded_data += encoded_dict[char]

    return encoded_data, tree


def huffman_decoding(data, tree):

    if data is None or len(tree)==0:
        print("Error: Input is empty\n")
        return
    decoded_data = ''
    curr = tree[0]
    if is_leaf(curr):
        # handle repetitive case
        while curr.freq > 0:
            decoded_data += curr.value
            curr.freq -= 1
    else:
        idx = -1
        while idx < len(data) - 1:
            idx,  decoded_cha = decode_data(curr, idx, data)
            decoded_data += decoded_cha
    return decoded_data



# TESTING
def test_huffman_coding(data):
    # Function for testing
    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))

    encoded_data, tree = huffman_encoding(data)

    if encoded_data is not None:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

if __name__ == "__main__":
    codes = {}

    print('----------Test1----------')
    # test normal strings
    strings = "The bird is the word"
    test_huffman_coding(strings)
    # The content of the encoded data is: 1110111111101010001100110000101100101101101011111101010000111001100001
    # The content of the encoded data is: The bird is the word

    print('----------Test2----------')
    #  test repetitive string
    strings = "AAABBBAACCDDD"
    test_huffman_coding(strings)
    # The content of the encoded data is: 11111110101011110000010101
    # The content of the encoded data is: AAABBBAACCDDD

    print('----------Test3----------')
    # test empty Input
    strings = ""
    test_huffman_coding(strings)
    # Error: Input is empty

    print('----------Test4----------')
    # test None input
    strings = None
    test_huffman_coding(strings)
    # Error: Input couldn't be None

    print('----------Test4----------')
    # test invalue input
    strings = 123
    test_huffman_coding(strings)
    # The content of the encoded data is: 01110
    # The content of the encoded data is: 123
