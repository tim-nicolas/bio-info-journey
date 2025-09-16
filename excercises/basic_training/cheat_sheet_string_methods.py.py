# cheatsheet for me with all string methods and more


# Statements do not return something, whereas expressions can. An argument is an expression passed to a function.
# A statement says "Do that" to python. There are different kinds of statements.
string = (" Fingerboarding is easy")  # string = ... is an assignment statement

# all uppercases
print(string.upper())  # =>' FINGERBOARDING IS EASY'

# all lowecases
print(string.lower())  # =>' fingerboarding is easy'

# every first letter of a word in upper case
print(string.title())  # =>' Fingerboarding Is Easy'

# removes blank spaces at front and end of string
print(string.strip())  # =>'Fingerboarding is easy'

# removes only left blank spaces
print(string.lstrip())  # =>'Fingerboarding is easy'

# replaces every e with an i
print(string.replace("e", "i"))  # =>'Fingirboarding is iasy'

# gives the index of argument in parentheses: 4. If argument is not in variable. -1
print(string.find("ge"))  # =>4


# Extras (no methods):

# one example for an operator with a string. Returns a boolean.
print("ge" in string)  # =>True

# gives number of elements in object
print(len(string))  # =>23

# formatted strings can include variables or expressions inside.
name = ("Tim")
formatted_string = f"{name} is {len(name)} characters long"
print(formatted_string) # =>'Tim is 3 characters long'

