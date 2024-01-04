
class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None
class LinkedList:
    def __init(self):
        self.head=None
    def insert(self, newNode):
        if self.head is None:
            self.head=newNode
        else:
            self.head.next= newNode


firstNode=Node("John")
linkedList= LinkedList()
linkedList.insert(firstNode)