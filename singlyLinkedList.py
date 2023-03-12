import llInBetween
# Creating a linkedlist
# create a node class
# creating a linkedlist()
# creating a insert() method for linked list  

# Node creation 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
# linkedlist creation and various updating and printing methods
class Linkedlist:
    def __init__(self):
        self.head = None
# inserts new node to the linkedlist
    def insertData(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    def Print(self):
        if self.head is None:
            print("The lnList is empty!!")
            return
        currentData = self.head
        print(f"{currentData.data}--->", end = "")
        while True:
            if currentData.next is None:
                break
            print(f"{currentData.next.data}--->",end = "")
            currentData = currentData.next
           
           
            


            




firstNode = Node("jassim")
linkedList = Linkedlist()
linkedList.insertData(firstNode)
thirdNode = Node("parvathy")
linkedList.insertData(thirdNode)
linkedList.Print()

        





