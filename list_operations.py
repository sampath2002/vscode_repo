import numpy as np

import matplotlib.pyplot as plt
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
    def delete(self,val):
        curr = self.head 
        if curr.data == val and curr.next is None:
            self.head = None
            return
        elif curr.data == val and  curr.next is not None:
            self.head = self.head.next

            print(self.head.data)
            return
        else:
            while curr.next:
                #print(curr.data)
                if curr.data == val:
                    #print(curr.data)
                    curr.prev = curr.next

                temp = curr
                curr = curr.next
                

            return 
    1>2>1
    1>2>3>4>1>2>3

    def display(self):
        curr = self.head
        print(self.head.data)
        while curr.next:
            print(curr.data, end='-->')
            curr = curr.next
        print(curr.data, '-->','None')     

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
            print('<><><>',tail.next.data)


        return 
    
    def delete(self,val):
        curr = self.head 
        if curr.data == val and curr.next is None:
            self.head = None
            return
        elif curr.data == val and  curr.next is not None:
            self.head = self.head.next

            #print(self.head.data)
            return
        else:
            while curr.next != self.head:
                #print(curr.data)
                if curr.data == val:
                    print(curr.data)
                    temp.next = curr.next 

                temp = curr
                curr = curr.next
            if curr.data == val:
                print(curr.data)
                temp.next = curr.next 

            return 
        
    def display(self):
        curr = self.head
        print(self.head.data)
        while curr.next != self.head:
            print(curr.data, end='-->')
            curr = curr.next
        print(curr.data, '-->',curr.next.data)            


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

l1 = double_linked_list()
l1.append(22)
l1.append(33)
l1.append(44)
l1.append(55)
l1.delete(22)
#l1.display()
l = circular_list()
l.append(22)
l.append(33)
l.append(44)
l.display()
l.delete(22)
l.display()
l.append(45)
l.display()

l3 = [22,33,44,55,66]
#l1.list_to_node(l3)
#print('list BEFORE rotation: ', l3, '\nlist AFTER rotation : ',l1.rotate(100,[22,33,44,55,66]))


