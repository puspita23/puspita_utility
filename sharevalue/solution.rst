SHAREVALUE
----------
Write a program in python to print the latest share value of a company whose NASDAQ symbol would be given as  command line argument.

CODE EXPLANATION
----------------

step 1: From the main function check whether the input provided is a valid input or not.
step 2: If its a valid input, pass the symbol as an argument in the function, else it will display an error message and exit.
step 3: This function will provide the quoted price of the share and will print it.

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

link to the code: https://github.com/puspita23/puspita_utility/commit/291123932a2db6aca2fad1dac2133cc21118cb0c
