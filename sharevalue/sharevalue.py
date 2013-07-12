#!/usr/bin/env python

import urllib2
import sys


def price(sym): #function to get the quoted price of the NASDAQ symbol entered as command line argument.

        quote= urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s='+sym+'&f=l1') #quote is an instance variable which is storing the quoted price at that instance, of that NASDAQ symbol

 #Here we print the quoted price of the NASDAQ symbol entered. 
        print "This is the  latest quote for the given NASDAQ symbol is "
        print quote.read() #we use read() as it is an instance variable

 #Here is the main function where the argument passed in the commandline is checked to see whether it is a valid input or not.
if __name__ == '__main__': 
        if len(sys.argv) < 2 or len(sys.argv) > 2:
                print "Incorrect entry. Enter a NASDAQ symbol"
                sys.exit(1)
        else:
#here we pass the NASDAQ symbol as an argument into the price function.
                price(sys.argv[1])
                sys.exit(0)

