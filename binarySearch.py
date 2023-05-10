# Binary Search Coding in python
import math

def Getinput():
    numberOfElements = int(input("Enter the number of elements: "))
    elements = input("Enter the elements: ")
    listOfElements = list (map (int, elements.split()))[:numberOfElements]
    print(f"Your list is {listOfElements} ")
    return listOfElements

start = 0
def Binarysearch(listGiven, start, end, targetElement):
    print(listGiven[start:])
    midIndex = math.floor(((start + end)/2))
    if start > end:
        return False
    if listGiven[midIndex] == targetElement:
        return True
    if listGiven[midIndex] < targetElement:
       return Binarysearch(listGiven, midIndex+1, end, targetElement)
    else:
       return Binarysearch(listGiven, start, midIndex-1, targetElement)
       
    


inputList = Getinput()
end =len(inputList) - 1 
target = 19
result = Binarysearch(inputList, start, end, target)
print(result)


    


    



