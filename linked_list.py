'''
Author: Ansh Rajput
Date: Feburary, 28, 2021
Last modified: March, 6, 2021
'''

from nodeClass import Node

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0

    def print_list(self):
      printval = self._front
      while printval is not None:
         print (printval.element)
         printval = printval.next

    def length(self): #Returns length of linked list
        return self._length

    def insert(self, index, entry): #Inserts new url with node into linked list
        node = Node(entry)
        if self._front == None:
            self._front = node
        else:
            repeat = 1
            currentNode = self._front
            while repeat < index:
                if currentNode.next != None:
                    currentNode = currentNode.next
                    repeat += 1
            currentNode.next = node
        self._length+=1

    def remove(self, index): #Removes entry at index
        repeat = 1
        currentNode = self._front
        while repeat < index:
            currentNode = currentNode.next
            repeat += 1
        currentNode.next = currentNode.next.next
        self._length -= 1

    def get_entry(self, index): #Returns entry at index
        if index <= self._length and index >= 1:
            repeat = 1
            currentNode = self._front
            while repeat < index:
                currentNode = currentNode.next
                repeat += 1
            return currentNode
        else:
            raise RuntimeError("Index out of range.")

    def set_entry(self, index, entry): #Sets entry at index
        repeat = 1
        currentNode = self._front
        while repeat < index:
            currentNode = currentNode.next
            repeat += 1
        currentNode.url = entry

    def clear(self): #Clears the linked list
        self._front = None
        self._length = 0
