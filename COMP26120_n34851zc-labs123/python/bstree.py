import config

class bstree:
    def __init__(self):
        self.verbose = config.verbose
        # we ceate the left node and right node
        self.left = None
        self.right = None

    def size(self):
        if (self.tree()):
            # the size is the current number of node in the tree
            return 1 + self.left.size() + self.right.size()
        return 0
        
    
    def tree(self):
        # This counts as a tree if it has a field self.value
        # it should also have sub-trees self.left and self.right
        return hasattr(self, 'value')
        
    def insert(self, value):
        if (self.tree()):
            # TODO if tree is not NULL then insert into the correct sub-tree
            binarytree = self
            # put the vallue inside the binary tree
            while True:
                if value <= binarytree.value:
                # in the if statement we need to go left side of the tree
                    if binarytree.left == None:
                        binarytree.left = bstree()
                        binarytree.left.value = value
                        # jump outside of the loop
                        break
                    else:
                        binarytree = binarytree.left

                else:
                # In the else statement, It will go to the right side of the tree
                    if binarytree.right == None:
                        binarytree.right = bstree()
                        binarytree.right.value = value
                        # jump outside of the loop
                        break
                    else:
                        binarytree = binarytree.right
        else:
        # TODO otherwise create a new node containing the value
            # print
            self.value = value
        
    def find(self, value):
        if self.tree():
            # TODO complete the find function

            # print("Placeholder - remove this print statement")
            # TODO complete the find function
            binarytree = self
            if binarytree.value == value:
                return True  

            while True: 
                if value <= binarytree.value:  
                    if binarytree.left == None:  
                        return False 
                    elif binarytree.left.value == value:  
                        return True

                    # in the else statements, It will go to the next height 
                    else:
                        binarytree = binarytree.left 
                else:  
                    if binarytree.right == None:  
                        return False
                    elif binarytree.right.value == value:    
                        return True
                    # in the else statements, It will go to the next height     
                    else:  
                        binarytree = binarytree.right  
        return False 
         
    # You can update this if you want
    def print_set_recursive(self, depth):
        if (self.tree()):
            for i in range(depth):
                print(" ", end='')
            print("%s" % self.value)
            self.left.print_set_recursive(depth + 1)
            self.right.print_set_recursive(depth + 1)
            
    # You can update this if you want
    def print_set(self):
        print("Tree:\n")
        self.print_set_recursive(0)
        
    def print_stats(self):
        # TODO update code to record and print statistic
         print("Placeholder - remove this print statement")
            
            
