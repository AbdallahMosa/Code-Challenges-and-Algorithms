# Write your test here
import pytest 
from challenge01 import * 

tree=Tree()
tree.root = Node(3)
tree.root.left = Node(9)
tree.root.right = Node(20)
tree.root.right.left = Node(15)
tree.root.right.right = Node(7)

def test_tree1():
    tree_root= find_tree(pre_order(tree.root),in_order(tree.root))
    assert tree_root.value == 3 
    
def test_tree2_None():
    tree_root= find_tree(pre_order(tree.root),in_order(tree.root))
    assert tree_root.left.left == None
def test_tree3_9():
    tree_root= find_tree(pre_order(tree.root),in_order(tree.root))
    assert tree_root.left.value == 9
def test_tree4():
    tree1=Tree()
    tree1.root = Node(-1)
    tree_root= find_tree(pre_order(tree1.root),in_order(tree1.root))
    assert tree_root.value == -1