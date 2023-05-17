def findElement(str1, index):
    return str1[index] # returns the character at the variable index

def concatStrings(str1, str2):
    return str1 + str2 # concats str1 and str2 and returns that string
    
def divideStrings(str1):
    mid = len(str1)//2 #finds the midpoint, if the length is odd, it favors the floor
    return str1[0:mid] # returns the strings from the beginning up to the midpoint

def findSubstring(str1, str2):
    if(str1.find(str2) >= 0): # checks if the str2 is in str1 
        return True
    else: 
        return False
# tests all the functions
inputString1 = "This is a test string" 
inputString2 = "...it tests your functions" 
inputString3 = "functions" 
print(findElement(inputString1, 0)) 
print(concatStrings(inputString1, inputString2)) 
print(divideStrings(inputString1)) 
print(findSubstring(inputString2, inputString3)) 
print(findSubstring(inputString1, inputString3))

