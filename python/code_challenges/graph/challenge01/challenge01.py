# Write here the code challenge solution
class Node:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self,value):
        '''
        this method to add new node inside the garph 
        '''
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self,node1,node2,weight=0):
        '''
        method to add edge (conencting between to nodein graph )
        '''
        
        if not node1 in self.adj_list.keys():
            return("this node does not exist")

        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2,weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1,weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        '''
        to print the  graph 
        '''
        output = ''
        for vertex in self.adj_list.keys():
            output+= f'{vertex} ->'
            for edge in self.adj_list[vertex]:
                output+= f'{edge.vertex} ---> '
            output+= '\n'
        return output

    def bft(self, value):
        '''
        this method that take a value as a parameter, then traverse through the graph using Breadth First way starting 
        from the inputted value, and appending all the visited nodes values in a returned array
        
        '''
        visited_node = []
        queue = [value]
        while queue:
            current_node = queue.pop(0)
            if current_node not in visited_node:
                visited_node.append(current_node)
                for edge in self.adj_list[current_node]:
                    queue.append(edge.vertex)
        return visited_node





