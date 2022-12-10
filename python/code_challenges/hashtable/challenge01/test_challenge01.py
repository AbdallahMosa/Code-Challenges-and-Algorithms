# Write your test here
import pytest 
from challenge01 import * 

tree1 = Node(7)
tree1.left=Node(2)
tree1.right=Node(9)
tree1.left.right=Node(5)
tree1.left.left=Node(1)
tree1.right.right=Node(14)
print(find_sum_BST(tree1,3))

def test_is_sum1():
    actual= find_sum_BST(tree1,3)
    extcepted=True
    assert actual == extcepted
def test_is_sum2():
    actual= find_sum_BST(tree1,4)
    extcepted=False
    assert actual == extcepted