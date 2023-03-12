
# Node creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# linkedlist creation and various updating and printing methods


class Linkedlist:
    def __init__(self):
        self.head = None

#length  of the whole linked list
    def lenght(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length
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

# function to insert node at the begining
    def insertAtBegining(self, begnode):
        self.begnode = begnode
        begnode.next = self.head
        self.head = begnode


# function to insert in between two nodes

    def insertBetween(self, btwNode, firstNode, secondNode):
        stopNode = self.head
        while True:
            if stopNode == secondNode:
                break
            elif stopNode == firstNode:
                stopNode.next = btwNode
                btwNode.next = secondNode
            stopNode = stopNode.next
        
#Delete the last node

    def deleteNode(self):
        lastNode = self.head
        while lastNode.next is not None:
            referenceNode = lastNode
            lastNode = lastNode.next
        referenceNode.next = None

#Delete a node between two nodes
    def deleteInBetween(self,position):
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

  
  
           


    def Print(self):
        if self.head is None:
            print("The lnList is empty!!")
            return
        currentData = self.head
        print(f"{currentData.data}--->", end="")
        while True:
            if currentData.next is None:
                break
            print(f"{currentData.next.data}--->", end="")
            currentData = currentData.next
        


firstNode = Node("jassim")
linkedList = Linkedlist()
linkedList.insertData(firstNode)
thirdNode = Node("parvathy")
begData = Node("Somebody") 
fourthNode = Node("you")
btwNode = Node("Between")
linkedList.insertData(thirdNode)
linkedList.insertAtBegining(begData)
linkedList.insertData(fourthNode) 
linkedList.insertBetween(btwNode, thirdNode, fourthNode)
linkedList.deleteInBetween(3)
linkedList.Print()


