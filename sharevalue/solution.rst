Sharevalue
----------

Write a program in python to print the latest share value of a company whose NASDAQ symbol would be given as  command line argument.

Code Explanation
----------------

1. From the main function check whether the input provided is a valid input or not.
2. If its a valid input, pass the symbol as an argument in the function, else it will display an error message and exit.
3. This function will provide the quoted price of the share and will print it.

Code 
----
    ::

	import urllib2
	import sys

	"""Function is used to get the quoted price of the NASDAQ symbol,which is entered as command line argument."""

	def price(sym):
	    	quote= urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s='+sym+'&f=l1')
    		print "This is the  latest quote for the given NASDAQ symbol is "+quote.read()

	"""Here is the main function where the argument passed in the commandline is checked to see whether it is a valid input or not and then passed to the function price()."""
	if __name__ == '__main__':
        	if len(sys.argv) !=2:
                	print "Incorrect entry. Enter a NASDAQ symbol"
                	sys.exit(1)
        	else:
                	price(sys.argv[1])
                	sys.exit(1)

Link to the code is https://github.com/puspita23/puspita_utility/blob/master/sharevalue/sharevalue.py
