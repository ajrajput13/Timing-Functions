'''
Author: Ansh Rajput
Date: Monday, April 4, 2022
Last modified: Monday, April 11, 2022
Purpose: Uses a linked list, nodes, stacks, and queues, to measure the time
         it takes to process unique actions and displays them in their own files
'''

import time

def nanosec_to_sec(ns):
    BILLION = 1000000000
    return ns/BILLION

class Node:
    def __init__(self,entry):
        self.entry = entry
        self.next = None
    def __repr__(self):
        return f"{self.entry}"

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self,entry):
        if self.is_empty():
            self.top = Node(entry)
        else:
            self.top = self.top.next
            self.top = Node(entry)

    def pop(self):
        if self.is_empty():
            raise RuntimeError("stack is empty")
        else:
            value = self.top
            self.top = self.top.next
            return value.entry

    def peek(self):
        if self.is_empty():
            raise RuntimeError("stack is empty")
        else:
            return self.top.entry
    def __str__(self):
        return f"{self.top}"
    def clear(self):
        self.top = None


class Queue:
    def __init__(self):
        self._front = None
        self._back = None
    def is_empty(self):
        return self._front == None

    def enqueue(self,entry):
        if self.is_empty():
            self._front = Node(entry)
            self._back = self._front
        else:
            self._back.next = Node(entry)
            self._back = self._back.next
    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("queue is empty")
        else:
            value = self._front
            self._front = self._front.next
            return value.entry
    def peek_front(self):
        if self.is_empty():
            raise RuntimeError('queue is empty')
        else:
            return self._front.entry
    def clear(self):
        self._front = None
        self._back = None


class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0
    def printlist(self):
        jumper = self._front
        print(f"printing list...")
        print(f"length: {self._length}")
        if jumper != None:
            while jumper != None:
                print(jumper.entry)
                if jumper.next != None:
                    print(f"my next is {jumper.next.entry}\n")
                else:
                    print("i have no next")
                jumper = jumper.next
        else:
            print("the list is empty")
    def reverse(self):
        b = None
        temp = self._front
        while temp != None:
            a = temp.next
            temp.next = b
            b = temp
            temp = a
        self._front = b

    def length(self):
        return self._length

    def insert(self,index,entry):
        if 0 <= index <= self._length:
            if index == 0:
                entry.next = self._front
                self._front = entry
            elif index < (self._length) and index > 0:
                temp = self._front
                for node in range(index-1):
                    temp = temp.next
                entry.next = temp.next
                temp.next = entry

            elif index == self._length:
                temp = self._front
                for web in range(index):
                    b = temp
                    temp = temp.next
                b.next = entry
                entry.next = temp
            self._length += 1
        else:
            raise RuntimeError("invaid index")

    def get_entry(self,index):
        temp = self._front
        if 0 <= index <= (self._length):
            for nodes in range(index):
                temp = temp.next
            return temp.entry
        else:
            raise RuntimeError('invaid index')

    def clear(self):
        self._front = None
        self._length = 0

    def remove(self,index):
        temp = self._front
        if index == 0:
            temp = self._front
            self._front = self._front.next
            self._length -= 1
            return temp.entry
        elif 0 < index <= (self._length - 1):
            for node in range(index-1):
                temp = temp.next
            temp2 = temp.next
            temp.next = temp.next.next
            self._length -= 1
            return temp2.entry
        elif self._length == 0:
            raise RuntimeError("list is empty")
        else:
            raise RuntimeError("invaid input")

    def set_entry(self,index,entry):
        temp = self._front
        if index == 0:
            self._front = entry
            self._length += 1
        elif 0 < index <= (self._length-1):
            for node in range(index):
                temp = temp.next
            temp.entry = entry
        else:
            raise RuntimeError("invaid index")

class Executive:
    def __init__(self):
        self.stack = Stack()
        self.queue = Queue()
        self.linklist = LinkedList()
    def main(self):
        self.pop_item()
        self.pop_all()
        self.enqueueing()
        self.get_index_one()
        self.get_last_index()
        self.print_list()

    def pop_item(self):
        num = 0
        print("Beginning the timing code...")
        results = open("pop_one_results.txt", "w")
        for _ in range(100):
            num += 1000
            self.stack.clear()
            for _ in range(num):
                self.stack.push(_)
            start_time = time.process_time_ns()
            self.stack.pop()
            end_time = time.process_time_ns()
            ns = end_time - start_time
            sec = nanosec_to_sec(end_time - start_time)
            results.write(f"{ns} {sec} {start_time} {end_time}\n")
            print("Total time in ns: ", f"{end_time} - {start_time}")
            print("Total time in sec: ", sec)
        results.close()
        
    def pop_all(self):
        results = open("pop_results.txt","w")
        num = 0
        print("Beginning the timing code...")
        for _ in range(100):
            num += 1000
            self.stack.clear()
            for _ in range(num):
                self.stack.push(_)

            start_time = time.process_time_ns()
            while self.stack.top != None:
                self.stack.pop()
            end_time = time.process_time_ns()
            ns = end_time - start_time
            sec = nanosec_to_sec(end_time - start_time)
            results.write(f"{ns} {sec} {start_time} {end_time} \n")
            print("Total time in ns: ", f"{end_time} - {start_time}")
            print("Total time in sec: ", sec)
        results.close()
        
    def enqueueing(self):
        print("Beginning the timing code...")
        num = 0
        results = open("enqueue_results.txt", "w")
        for _ in range(100):
            num += 1000
            self.queue.clear()
            start_time = time.process_time_ns()
            for _ in range(num):
                self.queue.enqueue(_)
            end_time = time.process_time_ns()
            ns = end_time - start_time
            sec = nanosec_to_sec(end_time - start_time)
            results.write(f"{ns} {sec} {start_time} {end_time} \n")
            print("Total time in ns: ", f"{end_time} - {start_time}")
            print("Total time in sec: ", sec)
        results.close()
        
    def get_index_one(self):
        print("Beginning the timing code...")
        num = 0
        results = open("get_index_one.txt", "w")
        for _ in range(100):
            num += 1000
            self.linklist.clear()
            start_time = time.process_time_ns()
            for i in range(num):
                self.linklist.insert(0,Node(i))
            self.linklist.get_entry(0)
            end_time = time.process_time_ns()
            ns = end_time - start_time
            sec = nanosec_to_sec(end_time - start_time)
            results.write(f"{ns} {sec} {start_time} {end_time} \n")
            print("Total time in ns: ", f"{end_time} - {start_time}")
            print("Total time in sec: ", sec)
        results.close()
        
    def get_last_index(self):
        print("Beginning the timing code...")
        num = 0
        results = open("get_last_index.txt", "w")
        for _ in range(100):
            num += 1000
            self.linklist.clear()
            start_time = time.process_time_ns()
            for i in range(num):
                self.linklist.insert(0,Node(i))
            self.linklist.get_entry(self.linklist._length-1)
            end_time = time.process_time_ns()
            ns = end_time - start_time
            sec = nanosec_to_sec(end_time - start_time)
            results.write(f"{ns} {sec} {start_time} {end_time} \n")
            print("Total time in ns: ", f"{end_time} - {start_time}")
            print("Total time in sec: ", sec)
        results.close()
        
    def print_list(self):
        print("Beginning the timing code...")
        num = 0
        results = open("full_list_result.txt", "w")
        for _ in range(100):
            num += 1000
            self.linklist.clear()
            start_time = time.process_time_ns()
            for i in range(num):
                self.linklist.insert(0, Node(i))
            for node in range(self.linklist._length):
                print(self.linklist.get_entry(node))
            end_time = time.process_time_ns()
            ns = end_time - start_time
            sec = nanosec_to_sec(end_time - start_time)
            results.write(f"{ns} {sec} {start_time} {end_time} \n")
            print("Total time in ns: ", f"{end_time} - {start_time}")
            print("Total time in sec: ", sec)
        results.close()
Executive().main()
