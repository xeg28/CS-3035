class Stack:
    #initializing the list and size in the __init__ function
    def __init__(self):
        self.items = []
        self.__size = 0
    
    #pushing the items using append and incrementing the size
    def push(self, item):
        self.items.append(item)
        self.__size += 1
    
    #pops the items from the list using the pop method and decrements the size
    def pop(self):
        if(self.__size > 0):
            self.__size -= 1
        return self.items.pop()
        
    #returns true if the list is empty    
    def isEmpty(self):
        return self.__size == 0
        
    #peeks at the item at the top of the stack
    def peek(self):
        return self.items[self.__size - 1]
        
    #returns the size of the stack
    def size(self):
        return self.__size
  
#initializing the stack and pushing 5 elements       
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)

#test cases showcasing that pop, size, isEmpty, and peek are working properly
print("Pop 1:", stack1.pop())
print("Size:", stack1.size())
print("Is empty:", stack1.isEmpty())
print("Peek:", stack1.peek())
print()

print("Pop 2:", stack1.pop())
print("Size:", stack1.size())
print("Is empty:", stack1.isEmpty())
print("Peek:", stack1.peek())

