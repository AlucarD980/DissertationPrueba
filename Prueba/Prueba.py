'''
Created on May 31, 2016

@author: fernandoapolinar
'''

print("Hello, World !!")

a, b = 5, 1

if a < b:
    print('a ({}) is less than b ({})'.format(a,b))
else:
    print('a ({}) is  not less than b ({})'.format(a,b))

print("foo" if a > b else "bar")

'''
loops
'''

print("fibbo")
a,b = 0,1
while b < 50:
    print(b)
    a,b = b, a + b
print("DONE")


