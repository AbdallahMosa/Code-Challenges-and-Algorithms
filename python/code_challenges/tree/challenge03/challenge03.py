# Write here the code challenge solution
class Node:
    '''
    this class to create new Node
    '''
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    '''
    this class to create new Tree 
    '''
    def __init__(self):
        self.root = None


def pre_order(root):
    '''
    this function accept the root of tree and return list of value by using pre order traversal  
    '''
    new_list =[]
    if root is not None:
        new_list.append(root.value)
        new_list+=pre_order(root.left)
        new_list+=pre_order(root.right)
    return new_list


def in_order(root):
    '''
    this function accept the root of tree and return list of value by using in order traversal  
    '''
    new_list =[]

    if root is not None:
        new_list+=in_order(root.left)
        new_list.append(root.value)
        new_list+=in_order(root.right)
    return new_list

def find_tree(pre_order, in_order):
    '''
    this function that accept to list by pre_order and in_order thin build the tree 
    from these two list  
    '''
    if len(pre_order) == 0 :
        return None 
    root = Node(pre_order[0])
    root_index = in_order.index(root.value)
    pre_order_left = pre_order[1:root_index+1]
    in_order_left = in_order[0:root_index]
    pre_order_right = pre_order[root_index+1:]
    in_order_right = in_order[root_index+1:]
    root.left = find_tree(pre_order_left,in_order_left)
    root.right = find_tree(pre_order_right,in_order_right)

    return root
def Level_Order_Traversal(root):
    '''
    this function accept the root of tree and return list of value by using in level_order traversal  
    '''
    # just for test my code 
    new_list = []
    if not root:
        new_list.append(None)
        return
    q = [root]
    while len(q) > 0:
        curr = q.pop(0)
        if curr.left  :
            q.append(curr.left)
        if curr.right :
            q.append(curr.right)
        new_list.append(curr.value)
    
    return new_list

def convert_to(list_of_num):
    if list_of_num ==[]:
        return None 
    list_of_num.sort()
    mid_value = len(list_of_num) // 2 
    root = Node(list_of_num[mid_value])
    root.left = convert_to(list_of_num[:mid_value])
    root.right = convert_to(list_of_num[mid_value+1:])
    return root
if __name__ == '__main__':
    test=[0,-3,-10,5,9]
    test1=[1,3]
    print(Level_Order_Traversal(convert_to(test)))
    print(Level_Order_Traversal(convert_to(test1)))