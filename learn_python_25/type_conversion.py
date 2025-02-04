# Type conversion is the process of converting data of one type to another.

'''
There are two types of type conversion in Python
 1. Implicit Conversion : automatic type conversion
 2. Explicit Conversion : manual type conversion
'''

# Implicit type conversion

# Example where python promotes the conversion of the lower data type (integer) to higher data type (float) to avoid data loss

integer_number = 96
float_number = 9.6

new_num = integer_number + float_number

print("Data Type: ",type(new_num))
print(new_num)

# Python always converts smaller data type to larger datatypes to avoid the loss of data

num1 = "9"
num2 = 12
# print(num1+num2) Throws a TypeError : can only concatenate str (not "int") to str. Python cannot implement implicit conversion in these cases

# Explicit Type Conversion

# User converts the data type to required data type
# Let's consider the above example itself. Where we convert str to int explicitly
str_num = int(num1)
print(str_num + num2)

# In type casting loss of data may occur as we enforce the object to a specific data type.