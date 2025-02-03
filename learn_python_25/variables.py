# A variable is a container to hold data.
number = 10 
# number is a variable storing the value 10. We use the assignment operator = to assign a value to variable.

"""
Python is a type inferred language, so you dont have to explicitly define the variable type.
"""
#Assigned an integer
number = 20
print(type(number),number)

#Assigned a string
number = "twenty"
print(type(number),number)

# Assigning multiple values to multiple variables
a,b,c = 5,3.2,'Hello'
print(a)
print(b)
print(c)

# Assign same value to multpile variables at once
firstName = LastName = "Ravi Teja"
print("firstName",firstName)
print("LastName",LastName)

# Rules for naming Python variables
'''
1. Constant and variable names should have a combination of letters in lowercase,uppercase or digits or an underscore.
2. Variable name cannot start with a digit
3. You cant have any special characters except _
4. if you want to create a variable name having two words, use underscore to separate them
5. Python is a case - sensitive. So name and Name are different variables.
'''