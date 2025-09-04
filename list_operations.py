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

    1>2>3>4>5

    5>4>3>2>1


   
        
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
        self.tail = None
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
            self.head.next = self.head
        else:
            self.tail = node(data)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next 
            curr.next = self.tail

            self.tail.next = self.head 
            #print('<><><>',self.tail.next.data)


        return 
    
    def delete(self,val):
        
        if self.head is None:
            print('empty LIST to delete Node')

            return
        elif self.head.next == self.head and self.head.data == val:
            self.head = None
            return
        else:
            cnt =0
            curr = self.head
            while curr.data != val:
                prev = curr
                curr = curr.next
                
            if curr.next == self.head:
                prev.next = self.head
                self.tail.next = self.head 
            elif curr == self.head:
                self.head = self.head.next
                self.tail.next = self.head 
            elif curr.next !=self.head:
                prev.next = curr.next 







        
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
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
#l1.delete(22)
l1.display()


l1.display()
l = circular_list()
l.append(11)
l.append(22)
l.append(33)
l.append(44)
l.display()
l.delete(33)
l.display()

l3 = [22,33,44,55,66]
#l1.list_to_node(l3)
#print('list BEFORE rotation: ', l3, '\nlist AFTER rotation : ',l1.rotate(100,[22,33,44,55,66]))


