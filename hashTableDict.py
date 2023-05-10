# Creating hash table class
class Hashtable:
    def __init__(self):
        self.MAX = 100
        self.array = [None for i in range (self.MAX)]
            

    # Creating a hashinf function using ASCII
    def Hashfunc(self, key):
        sum = 0
        for char in key:
            ASCII_val = ord(char)
            sum += ASCII_val
        return sum % self.MAX
    
    # Adds value to the hash indexed array  
    def __setitem__(self, key, value):
        Index = self.Hashfunc(key)
        self.array[Index] = value
    
    # Getting value from the hashtable
    def __getitem__(self, key):
        Index = self.Hashfunc(key)
        return self.array[Index]
                 
element = Hashtable()
element["July 8"] = 130
print(element["July 8"])




