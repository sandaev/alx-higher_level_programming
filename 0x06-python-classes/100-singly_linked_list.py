#!/usr/bin/python3
'''This module defines a singly linked list

Attributes:
------------
data (int) - Value of node
next_node (int) - Points to the next node

Poperties:
-----------
data() - Retrieves value of node
data(value) - Sets the value of node
next_node() - Retrieves next node
next_node(value) - Sets next_node

Classes:
----------
Node - Defines a node
LinkedList - Defines the linked list

Methods:
---------
sorted_insert(value) - Inserts a new Node into the correct sorted
position in the list
'''


class Node:
    '''Defines the node of linked list'''
    def __init__(self, data, next_node=None):
        '''Constructor for the Node objects'''
        if not isinstance(data, int):
            raise TypeError("data nust be an integer")
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        ''''Gets the value of Node object'''
        return self.__data

    @data.setter
    def dat(self, value):
        '''Sets the value of Node Object'''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
            self.__data = value

    @property
    def next_node(self):
        '''Retrieves the next_node object'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''Defines a singly linked list object'''
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        '''Creates node in sorted order'''
        node = Node(value)
        if not self.__head:
            self.__head = node

        elif not self.__head.next_node:
            if self.__head.data < value:
                self.__head.next_node = node
            else:
                node.next_node = self.__head
                self.__head = node
        else:
            temp = self.__head
            while self.__head:
                prev = self.__head
                nxt = self.__head.next_node

                if prev.data < value:
                    if nxt and nxt.data > value:
                        prev.next_node = node
                        node.next_node = nxt
                        self.__head = temp
                        break
                    elif nxt is None:
                        prev.next_node = node
                        self.__head = temp
                        break
                elif value < prev.data and nxt.data > value:
                    node.next_node = self.__head
                    self.__head = node
                    break
                elif value == prev.data and nxt is not None:
                    prev.next_node = node
                    node.next_node = nxt
                    self.__head = temp
                    break
                self.__head = self.__head.next_node

    def __str__(self):
        '''Gets printed when object is printed'''
        while self.__head:
            print(self.__head.data)
            if self.__head.next_node is None:
                return ""
            self.__head = self.__head.next_node
        return ""
