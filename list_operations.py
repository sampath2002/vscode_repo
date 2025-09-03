import numpy as np

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append(self,data):
        if  self.head is None:
            self.head = node(data)
        else:
            tail = node(data)
            curr =self.head
            while curr.next:
                curr = curr.next 
            curr.next = tail
            tail.prev = curr 
        return 
    1>2>1
    1>2>3>4>1>2>3

class circular_list:
    def __init__(self):
        self.head = None
    def list_to_node(self,list):
        for i in list:
            self.append(i)
        return 
    def rotate(self,pos,list):
        curr = self.head
        cnt = 0
        count =0
        while cnt < len(list) :
            if count > pos:

                list[cnt] = curr.data
                 
                cnt +=1

            curr = curr.next
            
            count = count +1 
            
        return list 

    def append(self,data):
        if self.head is None:
            self.head= node(data)
        else:
            tail = node(data)
            curr = self.head
            while curr.next != self.head and curr.next is not None:
                curr = curr.next 
            curr.next = tail
            tail.next = self.head 
        return 
    
            


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append(self,data):
        tail = node(data)
        if self.head is None:
            
            self.head = tail
            #print(self.head.data)
        else:
            curr = self.head
            while curr.next:
                print(curr.data,end='-->')
                curr = curr.next 
            curr.next = tail
            print(curr.data,'-->',curr.next.data)

l = double_linked_list()
l.append(22)
l.append(33)
l.append(44)
l.append(55)
l1 = circular_list()
l3 = [22,33,44,55,66]
l1.list_to_node(l3)
print('list BEFORE rotation: ', l3, '\nlist AFTER rotation : ',l1.rotate(100,[22,33,44,55,66]))


