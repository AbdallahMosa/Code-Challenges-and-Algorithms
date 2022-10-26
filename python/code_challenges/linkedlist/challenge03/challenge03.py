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
        this method to add new node 
        '''
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def get_node(self,value):
        current=self.head
        while current.value != value:
            current=current.next
        return current
    def printAll(self):
        '''
        this method for print and return new list 
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
    def __str__(self):
        output=""
        if self.head is None : 
          output = "Empty linked list"
        else :
         current=self.head
        while current : 
            output+=f'{current.value}-->'
            current=current.next
        output+= "None"
        return output





def remove_node_n(head, number_r):
    '''
    this function to remove node by using number From the end of the list
    '''
    slow = head 
    fast = head 
    for i in range(number_r): 
        fast = fast.next
    if not fast:
        return slow.next
    while fast.next is not None:
        fast = fast.next
        slow = slow.next   
    slow.next = slow.next.next
    return head
        
def find_mid_node(head):
    '''
    this function to find and return  the middle node and 
    '''
    node=[]
    while head is not None:
        node.append(head) 
        head=head.next
    return node[len(node)//2]

def delete_node(node):
    '''
    this function to delete the node from the linkd list 
    '''
    nextNode = node.next
    node.value = nextNode.value
    node.next = nextNode.next

linkedList1 = LinkedList()

if __name__=="__main__":
    # -------------- just for my test ------------- 
    linkedList1.append(1)
    linkedList1.append(2)
    linkedList1.append(3)
    linkedList1.append(4)
    linkedList1.append(5)
    linkedList1.append(6)
    # linkedList1.append(6)

    # print ("Linked List: ")
    # linkedList1.printAll()
    # delete_node(linkedList1.get_node(5))
    # print (" after Delete 5:")
    # linkedList1.printAll()
    linkedList1.printAll()
    print("after ==================================")
    x=remove_node_n(linkedList1.get_node(1),2)
    while x is not None :

        print(x.value)
        x=x.next
    # linkedList1.printAll()