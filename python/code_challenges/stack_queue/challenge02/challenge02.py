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
    def is_empty(self):
        return self.size == 0



def is_valid(val):
    '''
    this function to check the string is has a valid Parentheses or invalid 
    '''
    stack=Stack()

    for i in val :
        if i =="(" or i == "{" or i == "[":
            stack.push(i)
        elif i ==")" or i == "}" or i == "]":
            if stack.is_empty() or  not is_same(stack.peek(),i):
                return False 
            else :    
                stack.pop()
    if stack.is_empty():
        return True 
    else :
        return False 

def is_same(open, close):
    '''
    This function to check if the opening tag is the same as closing tag
    '''
    if open =="(" and close==")":
        return True 
    elif open =="{" and close=="}":
        return True 
    elif open =="[" and close=="]":
        return True 
    else :
        return False 

if __name__=="__main__":
    x="(2+5){123}[0]"
    print(is_valid(x))
    y="("
    print(is_valid(y))