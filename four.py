#Implement a hash table of 10 elements with modulo as hash function.
#Implement chaining when collision occurs using parts of Program 1 as a function


import random
from base.list import LinkedList
from base.node import Node

class ChainedHashTable:
	def __init__(self, size):
		self.links = [None] * size
		self.size = size

	def insert(self, key):
		#Make 'head' equal to LL/None at given key in hash table
		head = self.links[self.hash(key)]

		#Check to see if spot at hash table is None. If so, make new LL.
		if head == None:
			head = LinkedList()
			node = Node(key)
			head.insertElement(node.data)
			self.links[self.hash(key)] = head
			return

		#Else append key to already existing linked list.
		node = Node(key)
		head.insertElement(node.data)
		return

	def hash(self, key):
		hash_code = key % self.size
		return hash_code


if __name__ == "__main__": 
	my_list = LinkedList()
	num=10
	cht = ChainedHashTable(num)

	for i in range(num):
		cht.insert(random.randint(1, 99))
	print('\nIndex\tKey')
	for obj in range(cht.size):
		print(f'  {obj}  \t{cht.links[obj]}')