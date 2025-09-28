class min_heap:
    def __init__(self):
        self.heap = []
    


    def re_arrange(self,curr_index):
        parent = curr_index -1 //2
        while curr_index > 0  and self.heap[parent]  > self.heap [curr_index]:
            
            self.heap[parent], self.heap[curr_index] = self.heap[curr_index] , self.heap[parent]
            print(curr_index)
            curr_index = parent
            parent = curr_index -1 //2 



            


    def parent_index(self,index):
        return index // 2
    def re_min_heap_arrange(self,index):
        left = 2 * index + 1
        right = 2 * index + 2
        root_index = index
        #print('<><><><>',self.heap[self.parent_index(index)],left,right , self.heap[index])
        while True:
            if left < len(self.heap) and  self.heap[left] < self.heap[self.parent_index(index)]:
                root_index = left 
                #self.re_min_heap_arrange(root_index)
            if right < len(self.heap) and self.heap[right] < self.heap[self.parent_index(index)]:
                root_index = right 
                #self.re_min_heap_arrange(root_index)
            if self.heap[root_index] != self.heap[index]:
                self.heap[root_index] , self.heap[index] = self.heap[index] , self.heap[root_index]
                index = root_index 
            

    def insert(self,data):
        if self.heap is None:
            self.heap.append(data)
        else:
            self.heap.append(data)

            self.re_arrange(len(self.heap)-1)

    def delete(self):
        if len(self.heap) == 0:
            return 'empty heap to delete '
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            temp = self.heap[0]
            self.heap[0] = self.heap.pop()

            self.re_min_heap_arrange(0)
            return temp
    def display(self):
        print(self.heap)
        
