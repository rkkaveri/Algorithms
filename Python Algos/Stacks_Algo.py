class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(int(item))
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items-1)]
    def size(self):
        return len(self.items)
    def isOne(self):
        if len(self.items) == 1:
            return True
        else:
            return False
    def display(self):
        return self.items

if __name__ == '__main__':
    s = Stack()
    s.push(5)
    print(s.isOne())
    count = 0
    while count != 5:
        z = int(input("Enter the value:"))
        s.push(z)
        count += 1
    print(s.display())
    print("Length of stack :",s.size())
    print("Popping two elements from stack")
    s.pop()
    s.pop()
    print(s.display())
    print("Length of stack :",s.size())
    
