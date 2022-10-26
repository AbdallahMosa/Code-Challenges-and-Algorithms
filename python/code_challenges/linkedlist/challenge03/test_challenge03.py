# Write your test here
from challenge03 import *
import pytest

@pytest.fixture
def linkedList1():
    linkedList1 = LinkedList()
    linkedList1.append(1)
    linkedList1.append(2)
    linkedList1.append(3)
    linkedList1.append(4)
    linkedList1.append(5)
    mid_node=remove_node_n(linkedList1.get_node(1),2)
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
    mid_node=remove_node_n(linkedList2.get_node(1),1)
    node_value = []
    while mid_node is not None :
        node_value.append(mid_node.value)

        
        mid_node=mid_node.next

    return node_value


@pytest.fixture
def linkedList3():
    linkedList3 = LinkedList()
    linkedList3.append(1)

    mid_node=remove_node_n(linkedList3.get_node(1),1)
    node_value = []
    while mid_node is not None :
        node_value.append(mid_node.value)

        
        mid_node=mid_node.next
    return node_value


def test_remove_n(linkedList1):
    actual = linkedList1
    expected = [1,2,3,5]
    assert actual == expected
def test_remove_last(linkedList2):
    actual = linkedList2
    expected = [1,2,3,4]
    assert actual == expected
def test_empty(linkedList3):
    actual = linkedList3
    expected = []
    assert actual == expected
