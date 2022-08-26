#!/usr/bin/env python3 

'''
execution time to find primes upto n. n is given in command line argument.
python3 calc_execute_time.py 10000

'''

import primes
from primes import is_divisible, all_primes, sieve_gen_primes
import sys
import time


# sys.argv[0]
print("Looking for Primes up to ", sys.argv[1])

print("Using Sieve of Eratosthenes")
st = time.time()

count=0
for i in sieve_gen_primes():
    if i > int(sys.argv[1]):
        break    
    count+=1        
    
            

et = time.time()


elapsed_time = et - st
print('Execution time (Sieve of Eratosthenes):', elapsed_time, 'seconds')
print("Found " + str(count) + " primes")

st = time.time()

a = len(all_primes(int(sys.argv[1])))

et = time.time()


elapsed_time = et - st
print('Execution time (my method):', elapsed_time, 'seconds')
print("Found " + str(a) + " primes")




