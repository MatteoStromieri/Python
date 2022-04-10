from distutils.log import error
from logging import exception

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, node):
        self.head = node

    def append(self, value):
        tail = Node(value)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = tail
    
    def insert(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
    
    def print(self):
        t = self.head
        while t != None:
            print(t.value)
            t = t.next
    
    def length(self):
        l = 0
        temp = self.head
        while temp != None:
            l += 1
            temp = temp.next
        return l
    
    #index starts at 0 and returns the object at index 'index'
    def search(self, index):
        temp = self.head
        i = 0
        while i != index :
            if temp == None:
                return ValueError
            temp = temp.next
            i += 1
        return temp

    def deleteHead(self):
        self.head = (self.head).next

    def delete(self, index):
        if index == 0:
            self.deleteHead()
        if index + 1 > self.length():
            print(ValueError)
            return ValueError
        temp = self.search(index-1)
        if temp != ValueError:
            temp.next = (temp.next).next
    
    def pop(self):
        self.delete(self.length()-1)
