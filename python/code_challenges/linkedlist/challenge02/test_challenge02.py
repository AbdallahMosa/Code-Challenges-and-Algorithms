# Write your test here
from challenge02 import *
import pytest

@pytest.fixture
def linkedList1():
    linkedList1 = LinkedList()
    linkedList1.append(1)
    linkedList1.append(2)
    linkedList1.append(3)
    linkedList1.append(4)
    linkedList1.append(5)
    mid_node=find_mid_node(linkedList1.get_node(1))
    node_value = []
    while mid_node is not None :
        node_value.append(mid_node.value)

        
        mid_node=mid_node.next

    return node_value


@pytest.fixture
def linkedList2():
    linkedList2 = LinkedList()
    linkedList2.append(1)
    linkedList2.append(2)
    linkedList2.append(3)
    linkedList2.append(4)
    linkedList2.append(5)
    linkedList2.append(6)
    mid_node=find_mid_node(linkedList2.get_node(1))
    node_value = []
    while mid_node is not None :
        node_value.append(mid_node.value)

        
        mid_node=mid_node.next

    return node_value


@pytest.fixture
def linkedList3():
    linkedList3 = LinkedList()
    linkedList3.append(1)
    linkedList3.append(2)
    linkedList3.append(3)
    linkedList3.append(4)
    linkedList3.append(5)
    linkedList3.append(6)
    linkedList3.append(6)
    mid_node=find_mid_node(linkedList3.get_node(1))
    node_value = []
    while mid_node is not None :
        node_value.append(mid_node.value)

        
        mid_node=mid_node.next
    return node_value


def test_mid_odd(linkedList1):
    actual = linkedList1
    expected = [3, 4, 5]
    assert actual == expected
def test_mid_even(linkedList2):
    actual = linkedList2
    expected = [4, 5, 6]
    assert actual == expected
def test_mid_3(linkedList3):
    actual = linkedList3
    expected = [4, 5, 6 ,6]
    assert actual == expected



