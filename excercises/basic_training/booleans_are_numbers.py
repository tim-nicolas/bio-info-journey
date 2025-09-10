# trying to understand the concept of booleans in python
import time
a = 8
b = 4
if (a > b) == (True):
    print("true")
if (a > b) == (not False):
    print("also true")
# it is possible to negate a boolean

if (True > 0):
    print("True")
else:
    print("False")
# booleans are numbers (True=1), (False=0)

c = -2
while (c < 2):
    c += 1
    print(bool(c))
    time.sleep(0.5)
# bool integer combination, is true for any number except 0
