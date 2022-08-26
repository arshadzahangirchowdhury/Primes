#!/usr/bin/env python3 

'''
Functions for operations with primes
author : azc
'''
def is_divisible(x):
    ''' returns true if x is divisible by any one number starting from 2 upto the half of the number + 1'''
    out = []
    for i in range(2,x//2 +1):
        if i==2:
            out.append(x%i)
        if i>2 and i%2 !=0:
            out.append(x%i)

    return 0 in out

def all_primes(x):
    if isinstance(x,int):
        if x<3:
            raise ValueError('x must be greater than 3')
        else:
            primes = [2,3]
            count=2
            for i in range(0,x):
                if i > 3 :
                    if not is_divisible(i):
                        count=count+1
                        primes.append(i)

    
    else: 
        raise TypeError("x must be integer")

    return primes


def sieve_gen_primes():
    """ 
    Generate an infinite sequence of prime numbers.
    Sieve of Eratosthenes    
    Code by David Eppstein, UC Irvine, 28 Feb 2002
    http://code.activestate.com/recipes/117119/
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    i = 2
    
    while True:
        if i not in D:
            # i is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield i
            D[i * i] = [i]
        else:
            # i is composite. D[i] is the list of primes that
            # divide it. Since we've reached i, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[i]:
                D.setdefault(p + i, []).append(p)
            del D[i]
        
        i += 1



if __name__ == '__main__':
    print("Just some functions for having fun with primes")
        