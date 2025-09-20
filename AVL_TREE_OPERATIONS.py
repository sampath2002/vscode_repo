class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 
        self.height = 1
class AVL_TREE:
    def __init__(self):
        self.node = None
    
    def height(self,node):
        if node is None:
            return 0
        else:
            return node.height 
    def balance(self,node):
        if node is None:
            return 0
        else:
            return (self.height(node.left) - self.height(node.right))
    
    def left_rotation(self,z):
            y = z.right
            T2 = y.left
            y.left = z
            z.right = T2
            z.height = 1+max(self.height(z.left),self.height(z.right))
            y.height = 1+max(self.height(y.left),self.height(y.right))
            return y
    def right_rotation(self,z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y


    def insert(self,node,data):
        
        if node is None:
            
            return Node(data)
            
        
        elif data < node.data:
            node.left = self.insert(node.left,data)
        else:
                
            node.right = self.insert(node.right, data)

        #print(node.data,node.right.data)
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)
        if balance <-1 and data > node.right.data:
            #print(node.data,node.right.data, node.right.right.data)
            new_node = self.left_rotation(node)
            #print(new_node.data,new_node.left.data,new_node.right.data)
            return new_node
        
        elif balance > 1 and data < node.left.data:
            return self.right_rotation(node)
        
        elif balance > 1 and data < node.left.data:
            self.left_rotation(node.left)
            return self.right_rotation(node)
        
        
        elif balance > 1 and data < node.right.data:
            r_r= self.right_rotation(node.right)
            print('<><>',r_r.data)
            return self.left_rotation(node)
        return node
        # RIGHT - RIGHT SHIFT ROTATION
        #   BEFORE ROTATION 
        #   10 (HEIGHT : 2, BALANCE :-2 )
        #       20 (HEIGHT : 2, BALANCE :  -1, )
        #          30 (HEIGHT : 1 , BALANCE : 0 )
        #   AFTER ROTATION  -- BALANCED TREE 
        #       20                          (HEIGHT : 2, BALANCE : 1-1 : 0 )
        #  10                               (HEIGHT : 1, BALANCE :  0, )
        #                                   30 (HEIGHT : 1 , BALANCE : 0 )

        print('<><>',balance , node.right.data)
        if self.balance(node) < -1 and data > node.right.data:
            print("{}{}",node.right.data)
            return self.right_rotation(node)
    def traverse(self,node):
            if node is not  None:
                self.traverse(node.right)
                print(node.data)
                self.traverse(node.left)
                
            
t= AVL_TREE()
node =t.insert(None,10)
#print(node.data)
node =t.insert(node,20)
node =t.insert(node,15)
#print(node.data)
t.traverse(node)

