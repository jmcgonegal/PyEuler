#-------------------------------------------------------------------------------
# Name:        Problem 51
# Purpose: Find the smallest prime which, by replacing part of the number
# (not necessarily adjacent digits) with the same digit, is part of an eight
# prime value family.
#
# Author:      John McGonegal
#
# Created:     04/03/2012
# Copyright:   (c) John McGonegal 2012
# Licence:     None
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import math
import time
start_time = time.time()
def getPrimes(val):
  values = [True] * val
  primes = []
  for n in range(2,val):

    if(values[n]):
      primes.append(n)
      for mult in range(n+n,val,n):
        values[mult] = False


  return primes
def isPrime(number):
  return number in primes

def findPrimes(min,max):
  result = []
  for prime in primes:
    if(prime > min and prime < max):
      result.append(prime)
  return result

def findSimilar(prime_range,number,min_digit, max_digit):
  for digits in range(min_digit,max_digit):


    found = []
    for digit in range(digits-1):
      #for digit2 in range(digits-1):

      test = []
      for prime in prime_range:
        p = str(prime)
        if(p[digit]== str(number)):
          test.append(prime)
      if(len(test) == 4):
        found = test
        return found

def findNumberWithDigit(numbers, digit):
  result = []
  for number in numbers:
    if(str(digit) in str(number)):
      result.append(number)
  return result

# get primes
min = 100000
max = 1000000
primes = getPrimes(max)
elapsed_time = time.time() - start_time
print "found", len(primes), "primes in", elapsed_time, "seconds"

single_digit_primes = findPrimes(1,10)

#print findPrimes(100,1000)

prime_range = findPrimes(min,max)
results = {}
for n in range(len(prime_range)):

  for i in range(len(str(min))-2):
    for j in range(i+1,len(str(min))-1):
      for k in range(j+1,len(str(min))):
        test = []
        test.append(prime_range[n])
        t = str(prime_range[n])
        prime = str(prime_range[n])

        if(prime[j] == prime[k] == prime[i]):
          strtest = prime
          strtest = strtest[:i] + str('.') +  strtest[i+1:]
          strtest = strtest[:j] + str('.') +  strtest[j+1:]
          strtest = strtest[:k] + str('.') +  strtest[k+1:]
          for m in range(n+1,len(prime_range)):
            prime_test = str(prime_range[m])
            if prime_test[j] == prime_test[k] == prime_test[i]:

              strtest2 = prime_test
              strtest2 = strtest2[:i] + str('.') +  strtest2[i+1:]
              strtest2 = strtest2[:j] + str('.') +  strtest2[j+1:]
              strtest2 = strtest2[:k] + str('.') +  strtest2[k+1:]
              if(strtest == strtest2):
                test.append(prime_range[m])
        if(len(test) == 8):
          print test[0], '=', len(test)
          elapsed_time = time.time() - start_time
          print "found in", elapsed_time, "seconds"

          exit
