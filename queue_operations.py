class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class circular_queue:
    def __init__(self):
        self.head = None
        self.tail= None
        self.prev = None 
    def enqueue(self,data):
        self.tail = node(data)
        if self.head is None:
            self.head = self.tail 
            self.head.next = self.head
        else:
            curr = self.head
            #print('<><><',curr.data,curr.next.data,curr.next.next.data)
            while curr.next != self.head:
                curr = curr.next 
            curr.next = self.tail 
            self.tail.next = self.head
            print('<><><',curr.data,curr.next.data,curr.next.next.data)
            print('??',self.tail.data,self.head.data)
    def dequeue(self):
        if self.head is None:
            print('empty')
        elif self.head.next == self.head:
            self.head = None 
        else:
            self.head = self.head.next 
            self.tail.next = self.head

    def display(self):
        curr = self.head
        #print(curr.data,end='-->')
        while curr.next !=self.head:
            print(curr.data,end='-->')
            curr = curr.next 
        print(curr.data, '-->',curr.next.data)


class queue:
    def __init__(self):
        self.head = None 
        self.tail = None
    def enqueue(self,data):
        tail = node(data)
        if self.head  is None:
            self.head = node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next 
            curr.next = tail
    def dequeue(self):
        if self.head is None:
            print("empty queue")
        elif self.head.next is None:
            self.head = None 
            print('removed the ONLY node from queue')
        else:
            self.head = self.head.next 
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end='-->')
            curr = curr.next


l = circular_queue()
l.enqueue(10)
l.enqueue(20)
l.enqueue(30)
l.enqueue(40)
l.dequeue()


l.display()
