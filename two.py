# Use Program 1 as a function to create list of 10 nodes with random integer values 
# assigned at each node along with node pointer. Write a Merge Sort Program using 
# recursion to sort in ascending order. 

from one import createLinkedList
from base.list import LinkedList

def mergeList(left, right):
	temp = None
	if left is None:
		return right
	if right is None:
		return left

	if left.data <= right.data:
		temp = left
		temp.next = mergeList(left.next, right)
	else:
		temp = right
		temp.next = mergeList(left, right.next)

	return temp
	
def mergeSort(head):
	if head is None or head.next is None:
		return head

	mid =midElement(head)
	newHead = mid.next
	mid.next = None
	left = mergeSort(head)
	right = mergeSort(newHead)
	sortedlist = mergeList(left, right)
	return sortedlist

def midElement(head):
	i = j = head
	while (j.next and j.next.next):
		i = i.next
		j = j.next.next
	return i

if __name__ == "__main__":
	print('\nLinked List Before Sorting: \n')
	my_list = LinkedList()
	createLinkedList(10,my_list)
	res = mergeSort(my_list.head)
	print("\nAfter Merge Sort: \n")
	my_list.display(val=res)