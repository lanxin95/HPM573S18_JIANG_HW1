#Problem 1: Object Types. Consider the number 17. Construct multiple variables (y1, y2, y3, and y4) in Python that represent the number 17 in the various forms of objects (integer, float, string, and Boolean, respectively). Hint: For creation of the Boolean, set a value for 17 to be compared against another number.
#1. Print the value of y1, y2, y3, and y4 and their types (Hint: you can use function type() to get a type of an object or variable).
y1=int(18)
print(y1,type(y1))
y2=float(18)
print(y2,type(y2))
y3=str(18)
print(y3,type(y3))
y4=(17>16)
print(y4,type(y4))
#2. Use y1, y2, or y3 to create a variable named text such that print(text) prints 'The value of x is 17.'
text = "The value of y1, y2, or y3 is %d, %f, or %s." % (y1,y2,y3)
print(text)
text = "The value of y3 is %s." % (y3)
print(text)

