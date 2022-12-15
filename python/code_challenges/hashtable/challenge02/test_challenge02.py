# Write your test here
import pytest 
from challenge02 import repeated

ex1 ='ASAC is a department at LTUC. ASAC teaches programming in LTUC'
ex2 ="I am learning programming at ASAC"
def test_repeated():
    actual= repeated(ex1)
    extcepted="ASAC"
    assert actual == extcepted
def test_repeated2():
    actual= repeated(ex2)
    extcepted="No Repetition"
    assert actual == extcepted