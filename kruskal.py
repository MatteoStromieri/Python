""""
input:=[v1,v2,...vn],[(u1,v1,weight1),(u2,v2,weight2)....(un,vn,weightn)]

Time complexity(Amortized analysis): O(nlogn)
Space complexity: O(m)  (Space complexity could be O(1) if we sort the original graph's edges instead of creating a sorted copy)

where n = |vertexes| and m = |edges|
"""
import UnionFind as uf

def kruskal(vertexes,edges):
    #sort edges by weight O(nlogn)
    sorted_graph = sorted(edges, key = weight)
    #this will be the output MST
    mst = []
    #let's make our partition O(n)
    partition = uf.UnionFind(vertexes)
    #cycle over edges O(nlogn)(amortized cost)
    for i in sorted_graph:
        A = partition.find(i[0])
        B = partition.find(i[1])
        if(A != B ):
            mst.append(i)
            partition.union(A,B)
    return [vertexes,mst]



def weight(edge):
    return edge[2]

"""
SAMPLE INPUT 

out = kruskal(['a','b','c','d'],[('a','b',2),('a','c',1),('d','b',3),('c','d',4)])
print(out)

output -> [['a', 'b', 'c', 'd'], [('a', 'c', 1), ('a', 'b', 2), ('d', 'b', 3)]]
"""