# 1. Write a python/C program to create a linked list of 'n' nodes. Each node contains an
# integer value  and pointer to next node.

from base.list import LinkedList
import random

def createLinkedList(n,my_list):
    for i in range(n):
        my_list.insertElement(random.randint(0, 100))
    my_list.display()

if __name__ == "__main__":
    num= int(input("Enter no.of nodes : "))
    my_list = LinkedList()
    createLinkedList(num,my_list)
