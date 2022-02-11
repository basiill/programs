def add(a,b):
	c=a+b
	return c
def sub(a,b):
	c=a-b
	return c
def multi(a,b):
	c=a*b
	return c
def divi(a,b):	
	c=a/b
	return c
def exp(a,b):
	c=a**b
	return c

a=int(input("enter the 1st number: "))
b=int(input("enter the 2nd number: "))
print("enter the operation")
choice=input("Add,Substract,Multiply,Divide,Exponent: ")
if (choice=="Add"):
	print ("Result = ",add(a,b))
elif (choice=="Substract"):
	print ("Result = ",sub(a,b))
elif (choice=="Multiply"):
	print ("Result = ",multi(a,b))
elif (choice=="Divide"):
	print ("Result = ",divi(a,b))
elif (choice=="Exponent"):
	print ("Result = ",exp(a,b))
else:
	print("invalid input")

