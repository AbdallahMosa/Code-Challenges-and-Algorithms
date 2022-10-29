# Write here the code challenge solution
class Node:
    def __init__(self,vlaue):
        '''
        create new Node 
        '''
        self.next = None
        self.value = vlaue
class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        '''
        this method to push the value iside the stack 
        '''
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        ''''
        this method to remove the top value into the stack
        '''
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This stack is empty")
    
    def peek(self):
        '''
        this method to show the top without remove it 
        '''
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")




class MyQueue(): 
    def __init__(self) :
        self.stack_push = Stack()
        self.stack_pop= Stack()
    def push(self,value):
        '''
        push(int x) Pushes element x to the back of the queue
        '''
        if self.stack_pop.size != 0:
            for i in range(self.stack_pop.size):
                self.stack_push.push(self.stack_pop.pop())
        return self.stack_push.push(value)
    def pop(self):
        '''
        pop() Removes the element from the front of the queue and returns it
        '''
        if self.stack_push.size!=0 :
            for i in range(self.stack_push.size):
                self.stack_pop.push(self.stack_push.pop())
        return self.stack_pop.pop()
    def peek(self):
        '''
        peek() Returns the element at the front of the queue
        '''
        if self.stack_push.size==0 :
            return self.stack_pop.peek()
        else :
            for i in range(self.stack_push.size):
                self.stack_pop.push(self.stack_push.pop())
            return self.stack_pop.peek()
    def empty(self):
        '''
        empty() Returns true if the queue is empty, false otherwise
        '''
        return self.stack_push.size==0 and self.stack_pop.size==0

if __name__ =="__main__":
    
    q= MyQueue()
    q.push("A")
    q.push("B")
    q.push("C")
    q.push("D")
    print(q.peek())
    print(q.pop())
    print(q.peek())
    print(q.pop())
    print(q.peek())
    print(q.pop())
    print(q.peek())
    print(q.pop())
    print(q.pop())