"""
I need:
- a dictionary of elements
--every dict element is like ( element(key), set(value) )
- an array of linked lists
-- every element of the array is  ( size, linked list ), every list cointains the elements of a certain set

Space complexity: O(n)

Time complexity:
    __init__ -> O(len(values))
    union -> O(min(size(A),size(B)))
    find -> O(1)
"""

import LinkedList as ll

class UnionFind:

    def __init__(self, values):
        self.elements = {}
        self.sets = []
        for i in range(0,len(values)):
            temp = ll.LinkedList(ll.Node(values[i]))
            self.elements[values[i]] = i
            self.sets.append([1,temp])
    
        
    def union(self, A, B):
        if self.sets[A][0] == 0 or self.sets[A][0] == 0:
            return 
        if self.sets[A][0] < self.sets[B][0]: 
            A,B = B,A
        self.sets[A][0] += self.sets[B][0]
        temp = self.sets[B][1].head
        while temp != None:
            (self.sets[A][1]).insert(temp.value)
            self.elements[temp.value] = A
            temp = temp.next
        self.sets[B][0] = 0
        self.sets[B][1] = None

    
    def find(self, i):
        return self.elements.get(i)


        