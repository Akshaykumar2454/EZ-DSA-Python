class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def inOrder(root):
    current=root
    stack=[]
    done=0
    while True:         #Reach the left most Node of the current
        if current is not None:
            stack.append(current)    #place pointer to a tree nodeon the stack
            current = current.left  #Before traversing the node's left subtree
                
                        #Backtracing from empty subtree & visit node
                        # At the top of the satck
                        # However if the stack is empty you are done
        elif(stack):
            current=stack.pop()
            print(current.data, end=" ")
#we have visitefd the node and its left
#subtree,Now,it's right subtree's turn
            current=current.right
        else:
            break
    print()

#input



root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

inOrder(root)
