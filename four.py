#Implement a hash table of 10 elements with modulo as hash function.
#Implement chaining when collision occurs using parts of Program 1 as a function

import random
from base.list import LinkedList
from base.node import Node

class MyHash:
	def __init__(self, size):
		self.links = [None] * size
		self.size = size

	def insertElement(self, key):
		head = self.links[self.hash(key)]
		if head == None:
			head = LinkedList()
			node = Node(key)
			head.insertElement(node.data)
			self.links[self.hash(key)] = head
		else:
			node = Node(key)
			head.insertElement(node.data)
			
	def hash(self, key):
		hash_code = key % self.size
		return hash_code
	
	def display(self):
		print('\nIndex\tKey')
		for obj in range(self.size):
			print(f'  {obj}  \t{self.links[obj]}')


if __name__ == "__main__": 
	num=10
	hash = MyHash(num)
	for i in range(num):
		hash.insertElement(random.randint(1, 99))
	
	hash.display()