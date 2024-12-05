#############################################################################
# Stack class implemented with an array
class Stack:
    # Constructor
    def __init__(self):
        self.StackPointer = -1  # Indicates the current position (empty stack at -1)
        self.Max = 4            # Maximum size of the stack
        self.Contents = [None for _ in range(self.Max)]  # Initialize stack with None

    # Add an item to the stack
    def Push(self, Item):
        # Check for stack overflow
        if self.StackPointer == self.Max - 1:
            print("Stack overflow: Cannot push item.")
            return False  # Stack is full, cannot push
        else:
            self.StackPointer += 1  # Move pointer to the next position
            self.Contents[self.StackPointer] = Item  # Place the item on the stack
            return True  # Successfully pushed the item

    # Remove an item from the stack
    def Pop(self):
        # Check for stack underflow
        if self.StackPointer == -1:
            print("Stack underflow: Cannot pop from an empty stack.")
            return None  # Stack is empty, cannot pop
        else:
            Item = self.Contents[self.StackPointer]  # Get the top item
            self.StackPointer -= 1  # Move pointer down to remove the item
            return Item  # Return the popped item

    # Look at the top item in the stack without removing it
    def Peek(self):
        # Check if the stack is empty
        if self.StackPointer == -1:
            print("Stack is empty.")
            return None  # No item to peek at
        else:
            return self.Contents[self.StackPointer]  # Return the top item

    # Return all items from the stack without modifying it
    def GetItems(self):
        if self.StackPointer == -1:
            print("Stack is empty.")
            return []  # Return an empty list if stack is empty
        else:
            return self.Contents[:self.StackPointer + 1]  # Return all items in the stack

#############################################################################
# Main program starts here

# Subroutine to output the contents of a stack
def ClearStack(InputStack):
    Item = InputStack.Pop()
    while Item is not None:
        print(Item)
        Item = InputStack.Pop()

# How to create a new stack
MyStack = Stack()

# How to push to the stack (returns True on success or False on stack overflow)
Action = MyStack.Push("Craig")
print(f"Push 'Craig': {Action}")
Action = MyStack.Push("Dave")
print(f"Push 'Dave': {Action}")
Action = MyStack.Push("Alice")
print(f"Push 'Alice': {Action}")
Action = MyStack.Push("Bob")
print(f"Push 'Bob': {Action}")
Action = MyStack.Push("Overflow")  # This should return False due to overflow

# How to pop from the stack (stack underflow returns None)
Item = MyStack.Pop()
print(f"Popped item: {Item}")

# How to peek at the top item without removing it
Item = MyStack.Peek()
print(f"Top item: {Item}")

# Getting all items currently in the stack
Items = MyStack.GetItems()
print(f"Current stack items: {Items}")

# How to clear the stack by popping all items
print("Clearing stack:")
ClearStack(MyStack)
