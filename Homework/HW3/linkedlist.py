#The node class contains the value and the reference to the 
#Next node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
#the linked list class contains the head node, tail node, and size       
class LinkedList:
    #initializes the instance variables
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    #checks if the list is empty
    def isEmpty(self):
        return self.size == 0
    
    #inserts a value at the beginning of the list
    def insertHead(self, value):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
        self.size += 1
    
    #removes the item at the beginning of the list
    def removeHead(self):
        if self.isEmpty():
            raise Exception("You cannot remove an item from an empty list")
            return
        if self.size == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.size -= 1
            return value
        else:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value
        
    #inserts an item at the end of the list
    def insertTail(self, value):
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
    
    #removes the item at the end of the list
    def removeTail(self):
        if self.isEmpty():
            raise Exception("You cannot remove an item from an empty list")
            return
        if self.size == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.size -= 1
            return value
        #the loop in this block iterates to the second last element
        #in the list so the tail reference can be deleted and
        #re-referenced to the element before it
        else:
            curr = self.head
            while curr.next.next != None: 
                curr = curr.next
            value = self.tail.value
            curr.next = None
            self.tail = curr
            self.size -= 1
            return value
    
    #inserts a value at the specified index
    def insertAtPos(self, value, index):
        if index > self.size or index < 0:
            raise Exception("index", index, "is out of bounds for length", self.size)
            return
        if index == 0:
            self.insertHead(value)
        elif index == self.size:
            self.insertTail(value)
        #The loop in this block will go to the element right before 
        #index so the new node can be connected to the one before it.
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            temp = curr.next
            curr.next = Node(value)
            curr.next.next = temp
            self.size += 1
    
    #Prints out the list
    def traverse(self):
        curr = self.head
        print('[', end="")
        while curr.next != None:
            print(curr.value, end=', ')
            curr = curr.next
        print(self.tail.value, end="]")
        print()

#Test Cases        
linkedList = LinkedList()
linkedList.insertHead(4)
linkedList.insertHead(2)
linkedList.insertHead(1)
linkedList.insertHead(0)

linkedList.insertTail(5)
linkedList.insertTail(6)

linkedList.removeHead()
linkedList.removeTail()
linkedList.insertAtPos(3,2)

linkedList.traverse()

# ----- Ouput -----
#[1, 2, 3, 4, 5]
