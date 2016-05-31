'''
Created on May 31, 2016

@author: fernandoapolinar
'''

#Fibonacci class

class Fibonacci():
    
    def __init__(self, a ,b):
        self.a = a
        self.b = b
    
    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci(0,1)

for r in f.series():
    if r > 1000:break
    print(r)
    
    