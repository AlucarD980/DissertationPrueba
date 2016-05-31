'''
Created on May 31, 2016

@author: fernandoapolinar
'''

def isprime(n):
    if n == 1:
        return False
    
    for x in range (2, n):
        if n % x == 0:
            return False
        
        else:
            return True


'''
Generator
'''
        
def primes(n = 1):
    while(True):
        if isprime(n): yield n
        n += 1

'''
End Generator
'''

for n in primes():
    if n > 100: break
    print(n)
    