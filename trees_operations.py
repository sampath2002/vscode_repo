
class node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None

class tree:
    def __init__(self):
        

        self.root = None
        
    def append(self,data):
        #tail = node(data)
        if self.root is None:
            self.root = node(data)

            return 
        else:
            curr = self.root
            leaf = node(data)
            while curr:
                print(curr.data)
                if curr.data < leaf.data:
                    if curr.right is None:
                       curr.right = leaf 
                       leaf.right = leaf.left = None
                       #print(curr.left.data,self.root.data , self.root.right.data )
                       break 
                       
                    else: 
                        curr = curr.right 
                else:
                    if curr.left is None:
                       curr.left = leaf 
                       leaf.right = leaf.left = None
                       #print(curr.left.data,curr.data, curr.right  ) 
                       break
                    else: 
                        curr = curr.left



    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node.right:
            self.print_tree(node.right, level + 1)
        print('    ' * level + f'-> {node.data}')
        if node.left:
            self.print_tree(node.left, level + 1)


l = tree()
l.append(100)
l.append(10)
l.append(150)
l.append(177)
l.append(144)
l.print_tree()

                


            