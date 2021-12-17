# Use Program 1 as a function to create list of 10 nodes with random integer 
# values assigned at each node along with node pointer. Write a Quick Sort 
# Program using recursion to sort in descending order. 

from base.list import LinkedList
from one import createLinkedList	

def parition(start, end) :
	pivot = start
	front = start
	while front != None and front != end :
		if (front.data > end.data) :
			pivot = start
			# Swap node value
			temp = start.data
			start.data = front.data
			front.data = temp
			# Visit to next node
			start = start.next
		
		# Visit to next node
		front = front.next
	
	temp = start.data
	start.data = end.data
	end.data = temp
	return pivot

def quickSort(start, end) :
	if start == end :
		return
	pivot = parition(start, end)

	if pivot != start != None :
		quickSort(start, pivot)
	if pivot != None and pivot.next != None :
		quickSort(pivot.next, end)

if __name__ == "__main__": 
	my_list = LinkedList()
	createLinkedList(10,my_list)
	start= my_list.head
	end=my_list.head
	while (end.next):
		end=end.next
	val=quickSort(start,end)
	print("\n After Sort \n")
	my_list.display(val=val)