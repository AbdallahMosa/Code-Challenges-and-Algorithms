# Write here the code challenge solution
class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        '''
        this function to add new node 
        '''
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    # def delete_a_node(self, val ):
    #     '''
    #     this function just to delete node from the LinkedList 
    #     '''
        
    #     current = self.head
    #     if (current.value == val):
    #         self.head = current.next
            
    #         return
    #     while(current is not None):
    #         if current.value == val:
    #             previous.next = current.next
    #             break
    #         previous = current
    #         current = current.next
    #     ''''
    #     if the current == None which mean the val not in to the linklist 
    #     '''
    #     if(current == None): 
    #         return
      
    def get_node(self,value):
        current=self.head
        while current.value != value:
            current=current.next
        return current
    def printAll(self):
        '''
        this function for print and return new list 
        '''
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



def delete_node(node):
    nextNode = node.next
    node.value = nextNode.value
    node.next = nextNode.next

linkedList1 = LinkedList()

if __name__=="__main__":
    linkedList1.append(4)
    linkedList1.append(5)
    linkedList1.append(1)
    linkedList1.append(9)
    print ("Linked List: ")
    linkedList1.printAll()
    delete_node(linkedList1.get_node(5))
    print (" after Delete 5:")
    linkedList1.printAll()