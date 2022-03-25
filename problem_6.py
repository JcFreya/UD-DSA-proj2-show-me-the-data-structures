'''
# Problem 6: Union and Intersection
Implement the union and intersection functions.
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B.
The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that
are members of both the sets A and B.

Here will take in two linked lists and return a linked list that is composed of either
the union or intersection, respectively.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):

    # check empty Input
    if llist_1 is None or llist_2 is None:
        print("Error: Input lists couldn't be None\n")
        return

    # set to store all elements from two lists
    all_elements = set()

    # traverse list1
    curr = llist_1.head
    while curr:
        all_elements.add(curr.value)
        curr = curr.next

    # traver the list2
    curr = llist_2.head
    while curr:
        all_elements.add(curr.value)
        curr = curr.next

    # generate the output list
    union_list = LinkedList()
    for element in all_elements:
        union_list.append(element)

    return union_list

def intersection(llist_1, llist_2):
    # check empty Input
    if llist_1 is None or llist_2 is None:
        print("Error: Input lists couldn't be None\n")
        return

    # set to store all elements from llist_1
    l1 = set()

    # traver the llist_1 to get all elments
    curr = llist_1.head
    while curr:
        l1.add(curr.value)
        curr = curr.next

    # set to store all elements from llist_2
    l2 = set()
    while curr:
        l2.add(curr.value)
        curr = curr.next

    intersection = l1.intersection(l2)

    # create the output LinkedList
    intersection_list = LinkedList()
    for element in intersection:
        intersection_list.append(element)

    return intersection_list


# Test case 1
print('----------Test1----------')

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
print('\n')
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->

# Test case 2
print('----------Test2----------')

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
print('\n')
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->


# Test case 3
print('----------Test3----------')
# test invalid input
linked_list_5 = None
linked_list_6 = LinkedList()

element_2 = [1,7,8,9,11,21,1]

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
print('\n')
# Error: Input lists couldn't be None
# Error: Input lists couldn't be None
