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
    
def find_sum_BST(root, k):
    '''
    this function that accept the Binary Search tree  and number as an intger and return True if tree has two 
    that their summation is the given integer 
    
    '''
    new_val = {}
    def is_sum(root):
        if not root:
            return False
        if root.value in new_val:
            return True
        new_val[k - root.value] = True
        return is_sum(root.left) or is_sum(root.right)
    return is_sum(root)
if __name__=="__main__":
    # tree1=Tree()
    tree1 = Node(7)
    tree1.left=Node(2)
    tree1.right=Node(9)
    tree1.left.right=Node(5)
    tree1.left.left=Node(1)
    tree1.right.right=Node(14)
    print(find_sum_BST(tree1,3))