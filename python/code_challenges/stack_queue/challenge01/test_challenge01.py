# Write your test here
import pytest 
from challenge01 import * 


q= MyQueue()
q.push("A")
q.push("B")
q.push("C")
q.push("D")
def test_peek():
     assert q.peek()=="A"
def test_popA():
    q.pop()
    assert q.peek()=="B"
def test_popB():
    q.pop()
    assert q.peek()=="C"
def test_popC():
    q.pop()
    assert q.peek()=="D"
def test_popD():
    q.pop()
    assert q.peek()=="This stack is empty"
def test_empty():
    assert q.empty()