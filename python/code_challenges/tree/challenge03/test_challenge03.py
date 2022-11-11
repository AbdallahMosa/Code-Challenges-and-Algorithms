# Write your test here
import pytest 
from challenge03 import * 



def test_tree1():
    test=[0,-3,-10,5,9]
    
    assert Level_Order_Traversal(convert_to(test)) == [0, -3, 9, -10, 5] 
    
def test_tree2():
    test2=[1,3]
    assert Level_Order_Traversal(convert_to(test2)) == [3, 1]

