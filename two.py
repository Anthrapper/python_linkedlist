# Use Program 1 as a function to create list of 10 nodes with random integer values 
# assigned at each node along with node pointer. Write a Merge Sort Program using 
# recursion to sort in ascending order. 

from base.list import LinkedList
from one import createLinkedList

 
def mergeList(left, right):

	if left == None:
		return right
	if right == None:
		return left

	result = None

	if left.data <= right.data:
		result = left
		result.next = mergeList(left.next, right)
	else:
		result = right
		result.next = mergeList(left, right.next)

	return result
	

def mergeSort(head):

	if head == None or head.next == None:
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