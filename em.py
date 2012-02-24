#!/usr/bin/env python
import operator
def likelihood(theta, vector):
   return vector[theta] / float(sum(vector))

def mle(vector):
   maxtheta, maxvalue = max([(theta[1], likelihood(theta[0], vector)) for theta in enumerate(vector)], key=operator.itemgetter(1))
   return maxtheta

def main():
   vector = [.5, .25, .125, .125]
   print "mle : ", mle(vector)
   for theta in enumerate(vector):
      print "likelihood(%r) : %r" % (theta[1], likelihood(theta[0], vector))

if __name__ == '__main__':
   main()
