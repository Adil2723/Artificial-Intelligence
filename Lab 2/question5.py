class MyList:
    def __init__(self):
        self.data = []

    def insert(self, val):
        self.data.append(val)

    def delete(self, val):
        if val in self.data:
            self.data.remove(val)
        else:
            print("Value not found")

    def search(self, val):
        for i in range(len(self.data)):
            if self.data[i] == val:
                print("Value found at index", i)
                return
        print("Value not found")

    def display(self):
        print("List:", self.data)


class MyStack:
    def __init__(self):
        self.data = []

    def insert(self, val):
        self.data.append(val)

    def delete(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            print("Stack is empty")

    def search(self, val):
        for i in range(len(self.data)-1, -1, -1):
            if self.data[i] == val:
                print("Value found at position", len(self.data)-1-i)
                return
        print("Value not found")

    def display(self):
        print("Stack:", self.data)


class MyQueue:
    def __init__(self):
        self.data = []

    def insert(self, val):
        self.data.append(val)

    def delete(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        else:
            print("Queue is empty")

    def search(self, val):
        for i in range(len(self.data)):
            if self.data[i] == val:
                print("Value found at position", i)
                return
        print("Value not found")

    def display(self):
        print("Queue:", self.data)


lst = MyList()
lst.insert(10)
lst.insert(20)
lst.insert(30)
lst.display()
lst.search(20)
lst.delete(20)
lst.display()

stk = MyStack()
stk.insert(5)
stk.insert(15)
stk.insert(25)
stk.display()
stk.search(15)
stk.delete()
stk.display()

que = MyQueue()
que.insert(100)
que.insert(200)
que.insert(300)
que.display()
que.search(200)
que.delete()
que.display()
