#############################################################################
# Stack class implemented with an array
class Stack:
    # Constructor
    def __init__(self):
        self.StackPointer = -1
        self.Max = 4
        self.Contents = ["" for Elements in range(self.Max)]

    # Add an item to the stack
    def Push(self, Item):
        if self.StackPointer >= 0:
            Action = MyStack.Push("Craig")
            self.StackPointer = self.StackPointer + 1
            return True
        else:
            return False
    
    

    # Remove an item from the stack
    def Pop(self):
        if self.StackPointer == self.StackPointer - 1:
            Item = MyStack.Pop("Craig")
            return Item
        else:
            return None


    # Look at the top item in the stack without removing it      
    def Peek(self):
        if self.Contents[self.StackPointer] == Item:
            Item = self.Contents[self.StackPointer]
            return Item


#############################################################################
# Main program starts here
MyStack = ("Craig")
# Subroutine to output the contents of a stack
def ClearStack(InputStack):
    Item = InputStack.Peek()
    while Item:
        Item = InputStack.Pop()
        if Item:
            print(Item)

# How to create a new stack
MyStack = Stack()

#How to push to the stack (returns True on success or False on stack overflow)
Action = MyStack.Push("Craig")
Action = MyStack.Push("Dave")

# How to pop from the stack (stack underflow returns None)
Item = MyStack.Pop()