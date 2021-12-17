from base.node import Node


class LinkedList:

	def __init__(self):
		self.head = None

	def add(self, data):
		temp = self.head
		self.head = Node(data)
		self.head.next = temp

	def __str__(self):
		str_list = []
		current = self.head
		while current:
			str_list.append(str(current.data))
			current = current.next
		return "[" + "->".join(str_list) + "]"

# Implement the missing functions in the ChainedHashTable ADT    
class ChainedHashTable:
	def __init__(self, size):
		self.links = [None] * size
		self.size = size

	def __repr__(self):
		final_list = []
		for i in range(len(self.links)):
			if self.links[i] == None:
				final_list.append('None')
			else:
				link_list = self.links[i]
				string = link_list.__str__()
				final_list.append(string)
		return ', '.join(final_list)



	def insert(self, key):
		#Make 'lst' equal to LL/None at given key in hash table
		lst = self.links[self.hash(key)]

		#Check to see if spot at hash table is None. If so, make new LL.
		if lst == None:
			lst = LinkedList()
			node = Node(key)
			lst.add(node.data)
			self.links[self.hash(key)] = lst
			return

		#Else append key to already existing linked list.
		node = Node(key)
		lst.add(node.data)
		return

	def hash(self, key):
		hash_code = key % self.size
		return hash_code


if __name__ == "__main__": 
	my_list = LinkedList()
cht = ChainedHashTable(7)
cht.insert(15)
cht.insert(11)
cht.insert(27)
cht.insert(8)

print(cht)