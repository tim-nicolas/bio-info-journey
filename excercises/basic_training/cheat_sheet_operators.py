'''adding this to my existing cheatsheet in the future'''
# comparison operators
# returns a boolean
# checks if values are the same

x = 3
y = 3

# == to check if its the same
print(x == y)  # =>True

# != to chek if values are not equal
print(x != y)  # =>False

# > or < check if value is greater or less
print(x > y)  # =>False

# >= to check if values are greater than or equal to OR <= for less than or equal to
print(x >= y)  # =>True


# logical operators
# also return booleans
# now two seperate statements are compared in their output

# its possible to set the variable to the boolean itself or another statement
x = True
y = (2 < 1)

# and returns true if both statements are true
print(x and y)  # =>False

# or returns true if atleast one of them is true
print(x or y)  # =>True

# not returns the opposite boolean
print(not x)  # =>True


# identity operators
# compares two variables in their identity / checks if two variables refer to same object in memory
# not to be confused with "==" which compares only the value
# there is only one operator "is"
# a "not" can be added

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is z)  # =>False
print(x == z)  # =>here True is returned as the values in these lists are the same
print(x is y)  # =>True
print(x is not y)  # =>False


# membership operators
# checks if a certain value is in a given container (lists, tuples, string, etc.)
# there is also only one operator "in"
# a "not" can also be added here

print(2 in x)  # =>True
print(2 not in x)  # =>False
