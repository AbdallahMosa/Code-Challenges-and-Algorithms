# Write your test here
from challenge01 import Graph
g1 = Graph()
a = g1.add_node("A")
b = g1.add_node("B")
c = g1.add_node("C")
d = g1.add_node("D")
e = g1.add_node("E")
f = g1.add_node("F")
g = g1.add_node("G")
h = g1.add_node("H")
i = g1.add_node("I")
k = g1.add_node("K")
g1.add_edge( a,  b)
g1.add_edge( a,  c)
g1.add_edge( a,  e)
g1.add_edge( b,  d)
g1.add_edge( c,  f)
g1.add_edge( e,  d)
g1.add_edge( e,  f)
g1.add_edge( e,  g)
g1.add_edge( f,  h)
g1.add_edge( f,  i)
g1.add_edge( g, h)
g1.add_edge( h, k)
g1.add_edge( i, k)
def test_bft():
    actual=[]
    for value in g1.bft(a):
        actual.append(value.__str__())
    assert actual == ['A', 'B', 'C', 'E', 'D', 'F', 'G', 'H', 'I', 'K']