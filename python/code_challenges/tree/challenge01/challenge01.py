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
if __name__ == '__main__':
    tree=Tree()
    tree.root = Node(3)
    tree.root.left = Node(9)
    tree.root.right = Node(20)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(7)

    print("pre ",pre_order(tree.root))
    print("in ",in_order(tree.root))
    tree_root = find_tree(pre_order(tree.root),in_order(tree.root))
    print(tree_root.left.value)
    print(Level_Order_Traversal(tree_root))
