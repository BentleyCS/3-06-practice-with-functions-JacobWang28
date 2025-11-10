#Herons Formula
import math
def heronsformula(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return(area)
print(heronsformula(3,4,5))

#returns the square root of the number n
import math
def root(n):
    return math.sqrt(n)
print (root(9))

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(a,b,c):
    s=(a+b+c)/2
    return s
print(semiPerimeter(3,4,5))

#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
def multiplyDifferences(a,b,c,d):
    result=a*(a-b)*(a-c)*(a-d)
    return result
print(multiplyDifferences(5,2,3,1))

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(a,b,c):
    s=(a+b+c)/2
    area=area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
print(herons(3,4,5))


#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(number):
    return number*2
print (denominator(3))
#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(a,b):
    a=a*-1
    return(a+b,a-b)
print(plusMinus(3,4))
#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a,b,c):
    result=(b**2)-((a*c)*4)
    return(result)
print(mainCalc(3,4,5))

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a,b,c):
    discriminant=b**2-(4*a*c)
    if discriminant<0:
        return None
    x1=(-b+math.sqrt(discriminant))/(2*a)
    x2=(-b-math.sqrt(discriminant))/(2*a)
    return(x1,x2)
print(quadratic(3,4,5))



