# Use Program 1 as a function to create list of 10 nodes with random integer 
# values assigned at each node along with node pointer. Write a Quick Sort 
# Program using recursion to sort in descending order. 

from base.list import LinkedList
from one import createLinkedList


def paritionLast(start, end):
    if (start == end or start == None or end == None):
        return start

    pivot_prev = start
    curr = start
    pivot = end.data

    while (start != end):
        if (start.data > pivot):
            pivot_prev = curr
            temp = curr.data
            curr.data = start.data
            start.data = temp
            curr = curr.next
        start = start.next

    temp = curr.data
    curr.data = pivot
    end.data = temp

    return pivot_prev

def sort(start, end):
    if(start == None or start == end or start == end.next):
        return

    pivot_prev = paritionLast(start, end)
    sort(start, pivot_prev)

    if(pivot_prev != None and pivot_prev == start):
        sort(pivot_prev.next, end)

    elif (pivot_prev != None and pivot_prev.next != None):
        sort(pivot_prev.next.next, end)
 
if __name__ == "__main__":
    print('Linked List Before Sorting: ')
    my_list = LinkedList()
    createLinkedList(8,my_list)
 
    start = my_list.head
    end=start
    while (end.next != None):
        end = end.next

    sort(start, end)
 
    print("\nAfter Quick Sort: ");
    
    my_list.display()