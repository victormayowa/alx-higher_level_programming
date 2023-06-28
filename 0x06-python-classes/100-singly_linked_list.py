#!/usr/bin/python3
"""
Singly Linked List Module
"""


class Node:
    """
    Defines a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a node instance.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node in the linked list (default is None).

        Raises:
            TypeError: If data is not an integer or next_node is not a Node object.

        Attributes:
            __data (int): The private instance attribute representing the data of the node.
            __next_node (Node): The private instance attribute representing the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Args:
            value (int): The data value to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            Node: The next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The next node to set.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.
    """
    def __init__(self):
        """
        Initializes an empty singly linked list.

        Attributes:
            __head: The private instance attribute representing the head of the linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (in increasing order).

        Args:
            value (int): The value of the new Node to insert.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)

