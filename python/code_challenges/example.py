#  Testing pulling the code challenge:
#  write here the code challenge instruction
def sum(a, b):
    return a+b


class Node:

	
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:


	def __init__(self):
		self.head = None


	def append(self, node):
		if  self.head is None:
			self.head=node
		else :
			current = self.head
			while current.next is not None :
				current = current.next
			current.next = node 

		
		

	def delete_a_node(self, key):
		
		temp = self.head
		if (temp.value == key):
			self.head = temp.next
			temp = None
			return
		while(temp is not None):
			if temp.value == key:
				prev.next = temp.next
				break
			prev = temp
			temp = temp.next

		if(temp == None):
			return
		temp = None



	def printList(self):
		list_of_node=[]
		if self.head is None :
			print("The linked list is empty")
		else :
			current = self.head
			while current is not None:
				list_of_node.append(current.value)
				print(current.value)

				current = current.next
		print(list_of_node)
		return list_of_node


linkedList1 = LinkedList()
node1 = Node(4)
node2 = Node(5)
node3 = Node(1)
node4 = Node(9)
if __name__=="__main__":
	linkedList1.append(node1)

	
	linkedList1.append(node2)

	
	linkedList1.append(node3)

	
	linkedList1.append(node4)

	print ("Created Linked List: ")
	linkedList1.printList()
	linkedList1.delete_a_node(5)
	print ("Linked List after Deletion of 5:")
	linkedList1.printList()
