# this is a comment

# below this line is the way you to import any package to your script
import os

# below this line is the way to declare the variables
number = 1 # the common variable name
n_number = 1 # variable name with _
# above variable has data type of integer

string = "Hi"
object = object
# end of variable section

# below lines is the way you can make loop
# for loop:
for i in range(1, 10): # this line will make increase i value from 0 to 10
	print(i) # printing the value of i

# while loop
n = 0
while n < 10: # make loop while n is less than 10
	print(n) # printing the value of n
	n += 1 # increase the n value by 1

# below lines are the way to declare and use class
class YourClass: # declaring you class or also called object
	def YourEmptyFunction(this):
		pass

	def YourPrintFunction(this, str:string):
		print(str)

# this is how you use the above class
yourclass = YourClass()
yourclass.YourPrintFunction("Hello World");

# below lines are the way to make a childred from any available class
class YourChildClass(YourClass):
	def YourChildEmptyClass(this):
		pass

	def YourChildPrintFunction(this, text:string):
		print(str.upper(text))

# this is how you use it
your_child_class = YourChildClass()
your_child_class.YourChildPrintFunction("Hello World")
