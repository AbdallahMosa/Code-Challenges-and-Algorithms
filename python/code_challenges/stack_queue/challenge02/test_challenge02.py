# Write your test here
import pytest 
from challenge02 import * 

def test_one():
    test="()"
    assert is_valid(test)
def test_two():
    test="()[12]{}"
    assert is_valid(test)
def test_three():
    test="({)}"
    assert is_valid(test) == False
def test_four():
    test="[{(())}]"
    assert is_valid(test) 
def test_five():
    test="[(hello)()]"
    assert is_valid(test) 