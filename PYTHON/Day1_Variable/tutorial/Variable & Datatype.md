# Day 1 - Variables and Data Types

What is a variable?
Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

a = 1
b = True
c = "Harry"
d = None
These are four variables of different data types.

What is a Data Type?
Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
In python, we can print the type of any operator using type function:

a = 1
print(type(a))
b = "1"
print(type(b))
By default, python provides the following built-in data types:

1. Numeric data: int, float, complex
int: 3, -8, 0
float: 7.349, -9.0, 0.0000001
complex: 6 + 2i


2. Text data: str
str: "Hello World!!!", "Python Programming"


3. Boolean data:
Boolean data consists of values True or False.


4. Sequenced data: list, tuple
list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

Example:

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
Output:

[8, 2.3, [-4, 5], ['apple', 'banana']]
Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

Example:

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
Output:

(('parrot', 'sparrow'), ('Lion', 'Tiger'))


5. Mapped data: dict
dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

Example:

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
Output:

{'name': 'Sakshi', 'age': 20, 'canVote': True}


# Typecasting in python
The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

Two Types of Typecasting:
Explicit Conversion (Explicit type casting in python)
Implicit Conversion (Implicit type casting in python).
Explicit typecasting:
The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.

It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .

Example of explicit typecasting:
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)
Output:
The Sum of both the numbers is 22
Implicit type casting:
Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

Python converts a smaller data type to a higher data type to prevent data loss.

Example of implicit type casting:
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
Ouput:
<class 'int'>
<class 'float'>
10.0
<class 'float'>