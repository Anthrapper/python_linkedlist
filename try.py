# import random


# class MyHash:
# 	def __init__(self, key=-1, val=-1, next=None):
# 		self.key = key
# 		self.val = val
# 		self.next = next

# class MyHashMap:
# 	def __init__(self):
# 		self.data = [MyHash() for x in range(7)]
		
# 	def getHead(self, key):
# 		return self.data[key % 7]

# 	def put(self, key):
# 		val=key % 5
# 		head = self.getHead(key)

# 		while head.next:
# 			if head.next.key == key:
# 				head.next.val = val
# 				return
# 			head = head.next
# 		# head.next =self.data.repl(val, MyHash(key, val))
# 		head.next=MyHash(key,val)
		
# 	def get(self, key):
# 		head = self.getHead(key)
# 		while head.next:
# 			if head.next.key == key:
# 				return head.next.val
# 			head = head.next
# 		return -1

# 	def display(self,keys):

# 		my_list=self.data
# 		print(keys)
# 		print('Index\t\tKey')

		
# 		for x in range(len(my_list)):
# 			print(f"  {x} \t\t")
			
# 			# for i in range(len(keys)):
# 			# 	print(f"{self.get(keys[i] % 7)} ")
# 			# print()
# 			# print(my_list[x].key)
# 			# print(f"{x} : {self.get(my_list[x].key)}")

# 			# print(x)
# 			# print(my_list[x].key)
# 			# print(f"  {x} \t\t {self.data[x].val}")
# 		print(self.get(15))


# if __name__ == "__main__":
# 	obj = MyHashMap()
# 	# for i in range(4):
# 	keys=[int(input()) for x in range(7)]
# 	# obj.put(15)
# 	# obj.put(11)
# 	# obj.put(27)
# 	# obj.put(8)
# 	# obj.display(keys)
# 	print(obj.get(15))

class ListNode:
	def __init__(self, key=None, value=None, nxt=None):
		self.k = key
		self.val = value
		self.next = nxt
	
class MyHashMap:

	def __init__(self):
		self.size = 10
		self.lst = [None] * self.size
		
	def hash(self, key):
		return key % self.size

	def put(self, key: int, value: int) -> None:
		pos = self.hash(key)
		if self.lst[pos] is None: self.lst[pos] = ListNode(key, value); return
		h = head = self.lst[pos]
		while h:
			if h.k == key: h.val = value; return
			h = h.next
		self.lst[pos] = ListNode(key, value, head)
		
	def get(self, key: int) -> int:
		pos = self.hash(key)
		if self.lst[pos] is None: return -1
		head = self.lst[pos]
		while head:
			if head.k == key: return head.val
			head = head.next
		return -1


obj = MyHashMap()
obj.put( 10, 'ALH')
obj.put( 25, 'Mumbai')
obj.put( 20, 'Mathura')
obj.put( 9, 'Delhi')
obj.put( 21, 'Punjab')
obj.put( 21, 'Noida')
print(obj.get(21))
