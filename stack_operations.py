class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.head = None

    33>11
    def push(self,data):
        tail = node(data)
        if self.head is None:
            self.head = node(data)
            return 
        else:
            curr = self.head
            tail.next = curr
            self.head = tail
            #print('//',self.head.data,tail.next.data)
    def pop(self):
        if self.head is None:
            print('empty')
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next 
    def display(self):
        curr = self.head
        while curr:
            print(curr.data,end='-->')
            curr = curr.next

l = stack()
l.push(11)
l.push(22)
l.push(33)
l.push(44)
l.pop()

l.display()