''' here I will try to get a general understanding of all operators'''


# arithmetic operators (I left out +,-,*,/)
# returns an int as long as both operands are ints
# else float is returned
# / always returns a float

# Modulus = Rest
print(14 % 4)  # =>2

# Exponentiation
print(4**3)  # =>64

# Floor division; how often dies b fit in a with no decimals
print(14//4)  # =>3


'''Python assignment operators, used to assign a new expression
to an existing variable in a shorter way.
arithmetic assignment operators += as an example.
works for arithemtic and bitwise'''

x = 14

print(x += 3)  # =>17
# same as x = x + 3


# Bitwise operators
# Compares two integers (float not possible)

# AND sets each bit to 1 of both bits are 1
x = 14  # 00001110
x &= 9  # 00001110 & 00001001 = 00001000
print(x)  # => 8

# OR sets each bit to 1 if at least one of two bits is 1
x = 14  # 00001110
x |= 3  # 00001110 | 00000011 = 00001111
print(x)  # =>15

# XOR sets each bit to 1 if one but not two bits are 1
x = 14  # 00001110
x ^= 15  # 00001110 ^ 00001111 = 00000001
print(x)  # =>1

# NOT inverts all bits
x = 12  # 00001100
print(~x)  # =>-13  # x = -x -1

# << left shift shifts the int x digits to the left by adding zeros
x = 12
x <<= 1  # 00001100 << 00000001 = 00011000
print(x)  # =>24

# >> right shift shifts int to the right by removing x bits from the right and adding 0 to the left
x = 13  # 00001101
x >>= 2  # 00001101 >> 00000010 = 00000011
print(x)  # =>3


# comparison operators
# returns a boolean
# checks if values are the same

x = 3
y = 3

# == to check if its the same
print(x == y)  # =>True

# != to check if values are not equal
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

