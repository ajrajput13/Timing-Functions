'''
Author: Ansh Rajput
Date: Feburary, 28, 2021
Last modified: March, 6, 2021 
Purpose: The purpose of this lab is to create a program that takes a file containing all
         of "Moby Dick" and creates 2 other files. One of which counts
         and prints how many times each word is written while the other file prints each
         unique word that only appears once. This is done using dictionaries and file I/O.
'''

import time
from linked_list import LinkedList


def nanosec_to_sec(ns):
    BILLION = 1000000000
    return ns/BILLION

def print_menu():
    print("Time one of the following: ")
    print("1) Popping a single item from a stack")
    print("2) Popping all items from a stack")
    print("3) Queue's enqueue")
    print("4) Linked List get_entry at specifically index 0")
    print("5) Linked List get_entry at specifically the last index")
    print("6) Printing all elements in a LinkedList using get_entry\n")

def pop_single():
    start_time = time.process_time_ns()
    my_stack = []
    size = 0
    i = 0
    while i < 10:
        while size < 1000:
            my_stack.append('element')
            size += 1
        my_stack.pop()
        i += 1
        end_time = time.process_time_ns()

    print("Total time in ns: ", end_time-start_time)
    print("Total time in sec: ", nanosec_to_sec(end_time-start_time))
    

def pop_all():
    start_time = time.process_time_ns()
    my_stack = []
    size = 0
    i = 0
    while i < 10:
        while size < 1000:
            my_stack.append('element')
            size += 1
            my_stack.pop()
        i += 1
        end_time = time.process_time_ns()

    print("Total time in ns: ", end_time-start_time)
    print("Total time in sec: ", nanosec_to_sec(end_time-start_time))

def queue_enqueue():
    pass
    #Didn't know what it was asking

def entry_at_0():
    my_list = LinkedList()
    current = 0
    my_list.insert(current, 1000)
    my_list.print_list
    print(my_list)

def entry_at_last():
    pass

def print_all_entry():
    pass

def main():
    
    print_menu()
    user_input = int(input("Enter the number of the operation you want to time: "))

    if user_input == 1:
        pop_single()

    if user_input == 2:
        pop_all()

    if user_input == 3:
        queue_enqueue()

    if user_input == 4:
        entry_at_0()

    if user_input == 5:
        entry_at_last()

    if user_input == 6:
        print_all_entry()

    print()
    main()

main()





    
