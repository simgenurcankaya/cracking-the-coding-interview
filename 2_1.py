
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
		
# # Function to remove node
#     def RemoveNode(self, Removekey):

#         HeadVal = self.head

#         if (HeadVal is not None):
#             if (HeadVal.data == Removekey):
#                 self.head = HeadVal.next
#                 HeadVal = None
#                 return

#         while (HeadVal is not None):
#             if HeadVal.data == Removekey:
#                 break
#             prev = HeadVal
#             HeadVal = HeadVal.next

#         if (HeadVal == None):
#             return

#         prev.next = HeadVal.next

#         HeadVal = None
    
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




llist = SLinkedList()
llist.Atbegining("Mon")
llist.AtEnd("Tue")
llist.AtEnd("Wed")
llist.Atbegining("Sun")
llist.AtEnd("Thu")
llist.AtEnd("Thu")
llist.Atbegining("Sun")
llist.AtEnd("Thu")

llist.LListprint()

llist.removeDubs()
llist.LListprint()

#before remove dubs
# ------
# Sun
# Sun
# Mon
# Tue
# Wed
# Thu
# Thu
# Thu
# ------
# after remove dubs
# ------
# Sun
# Mon
# Tue
# Wed
# Thu
# ------