#!/usr/bin/env python
from sys import argv, exit, stderr
from os import EX_OK, EX_USAGE, EX_NOINPUT
from math import floor

def sieve(n):
   numbers = range(n)
   zeros = [0] * n
   for i in range(2, int(n**.5) + 1):
      if numbers[i]:
         numbers[i*2::i] = zeros[i*2::i]
   return filter(None, numbers)

def main():
   try:
      print "prime numbers : %r" % sieve(int(argv[1]))
   except IndexError:
      stderr.write("ERROR: %s needs an integer as input\n" % (argv[0]))
      return EX_NOINPUT
   except ValueError:
      stderr.write("ERROR: %s is not a valid integer\n" % (argv[1])) 
      return EX_USAGE
   return EX_OK

if __name__ == '__main__':
   exit(main())
