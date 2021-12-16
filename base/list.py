
from base.node import Node

class LinkedList:
	def __init__(self):
		self.head=None
	
	def display(self,val=None):
		if val is None:
			temp = self.head
		else:
			temp=val
		while (temp):
			print (temp.data, end=' -> ')
			temp = temp.next
		print('None')

	def insertElement(self,data):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
		else:
			temp = self.head
			while(temp.next):
				temp = temp.next
			temp.next=newNode