'''
Created on May 31, 2016

@author: fernandoapolinar
'''

try:
    fh = open('xlines.txt')
    for line in fh.read():
        print(line)
        
except IOError as e:
    print("something bad happened ({})". format(e))



print("After badness")

