
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
		
# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None
    
# Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next=NewNode

# Function to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

# Print the linked list
    def LListprint(self):
        printval = self.head
        print("------")
        while (printval):
            print(printval.data),
            printval = printval.next

        print("------")

    def removeDubs(self):
        val1 = self.head
        val2 = self.head
        while(val1):
            while(val2 and val2.next):
                if(val1.data == val2.next.data):
                    val2.next = val2.next.next
                else:
                    val2 = val2.next
            val1 = val1.next
            val2 = val1

    #first calculates the length, then finds the according node
    def kthToLast(self,k):
        lent = 0
        lhead = self.head
        while(lhead):
            lhead = lhead.next
            lent +=1
        
        lhead = self.head

        if(k >= lent or k<0):
            print("Invalid k value")
            return
        lent = lent - k - 1
        while(lent):
            lhead = lhead.next
            lent -= 1

        if(lhead):
            print("{} th to the last is {} \n".format(k,lhead.data))
        else:
            print("Invalid k value\n")


        # only one traverse to the end, with 2 pointers
    def kthToLastFaster(self,k):
        lnode = self.head
        t = k
        while(k):
            lnode = lnode.next
            k -=1
        goalNode = self.head
        while(lnode and lnode.next):
            goalNode  =goalNode.next
            lnode = lnode.next
            
        
        print("{} th to the last is {} \n".format(t,goalNode.data))


llist = SLinkedList()
llist.Atbegining("1")
llist.AtEnd("2")
llist.AtEnd("3")
llist.AtEnd("4")
llist.AtEnd("5")
llist.AtEnd("6")
llist.AtEnd("7")
llist.AtEnd("8")
llist.AtEnd("9")

llist.LListprint()
llist.kthToLast(0)
llist.kthToLast(2)
llist.kthToLast(9)
llist.kthToLast(5)

print("Faster to the last\n")

llist.kthToLastFaster(0)
llist.kthToLastFaster(2)
llist.kthToLastFaster(9)
llist.kthToLastFaster(3)
