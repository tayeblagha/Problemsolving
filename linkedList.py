class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class linkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode
    
    def printLinkedList(self):
        output = ""
        if self.head is None:
            print("Empty List")
            return
        else:
            currentNode = self.head
            while True:
                output += f"{currentNode.value}-->"
                if currentNode.nextNode is None:
                    output += "None"
                    break
                currentNode = currentNode.nextNode
            print(output)

    def delete(self, value):
        if self.head is None:
            print("Empty List. Cannot delete.")
            return
        
        if self.head.value == value:
            self.head = self.head.nextNode
            return
        
        currentNode = self.head
        while currentNode.nextNode:
            if currentNode.nextNode.value == value:
                currentNode.nextNode = currentNode.nextNode.nextNode
                return
            currentNode = currentNode.nextNode
        
        print(f"Value {value} not found in the list. Cannot delete.")

    def update(self, old_value, new_value):
        currentNode = self.head
        while currentNode:
            if currentNode.value == old_value:
                currentNode.value = new_value
                return
            currentNode = currentNode.nextNode
        print(f"Value {old_value} not found in the list. Cannot update.")

# Example
linkedList1 = linkedList() 
linkedList1.insert(1)
linkedList1.insert(3)
linkedList1.insert(5)
linkedList1.insert(7)
linkedList1.insert(9)
linkedList1.insert(11)




print("Original Linked List:")
linkedList1.printLinkedList()

# Example of delete
linkedList1.delete(3)
print("\nLinked List after deleting 3:")
linkedList1.printLinkedList()

# Example of update
linkedList1.update(1, 2)
print("\nLinked List after updating 1 to 10:")
linkedList1.printLinkedList()
