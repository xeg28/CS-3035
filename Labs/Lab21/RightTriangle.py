from math import sqrt

class RightTriangle:
    #creates a right trianlge in two cases. Case 1, only side1 and side2 is provided.
    #Case 2: side 1, side2, and hyp is provided.
    #Exception handling is in place and exceptions are raised for any bad input
    def __init__(self, side1, side2, hyp=None):
        
        try:
            self.side1 = float(side1)
            self.side2 = float(side2)
        except ValueError:
            raise Exception("side 1 and side 2 must be numeric.")    
        
        if float(side1) < 0 or float(side2) < 0 or (hyp != None and float(hyp) < 0):
            raise Exception("All values must be positive.")
        
        if hyp != None and abs(pow(float(side1),2) + pow(float(side2),2) - pow(float(hyp),2)) > 0.0001:
            raise Exception("The values given are not a pythagorean triplet.")
        
        if hyp == None:
            self.hyp = sqrt(pow(self.side1,2) + pow(self.side2,2))
        else:
            self.hyp = float(hyp)
    
    #returns whether the two triangles are equal to one another 
    def __eq__(self,rightTriangle):
        if abs(self.hyp - rightTriangle.hyp) > 0.0001:
            return False
        elif abs(self.side1 - rightTriangle.side1) <= 0.0001 and abs(self.side2 -rightTriangle.side2) <= 0.0001:
            return True
        else:
            return False

#A recursive function that checks whether the input is correct, if an exception is 
#caught, the function will call itself until the user provides the proper input. 
#There is also two cases to this function which are the same as the __init__ function
def validateInput(input1, input2, input3 = None):
    triangle = None
    if(input3 == None):
        try:
            triangle = RightTriangle(input1,input2)
        except Exception as e:
            print(str(e), "Try again")
            return validateInput(input("Enter side 1 of triangle 1. "),input("Enter side 2 of triangle 1. "))
        return triangle
    else:
        try:
            triangle = RightTriangle(input1,input2,input3)
        except Exception as e:
            print(str(e), "Try again")
            return validateInput(input("Enter side 1 of triangle 2. "),input("Enter side 2 of triangle 2. "),input("Enter the hypotenuse of triangle 2. "))
        return triangle

#Two triangles are created for both cases
triangle1 = validateInput(input("Enter side 1 of triangle 1. "),input("Enter side 2 of triangle 1. "))

triangle2 = validateInput(input("Enter side 1 of triangle 2. "),input("Enter side 2 of triangle 2. "), input("Enter the hypotenuse of triangle 2. "))

#The triangles are compared to seet if they are equal to one another
print("Triangle 1 == Triangle 2:",triangle1 == triangle2)




