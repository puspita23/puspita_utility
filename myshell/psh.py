from cmd2 import Cmd
from getpass import getuser
import sys
import requests

__version__ = '0.1'

class Application(Cmd):
    """
   The main Application class
 
   """

    def __init__(self):
        Cmd.__init__(self)
    def do_hello(self, line):
        print "Hello:", line
    def do_sayit(self,line):
        print "Python Rocks!"
    def do_stock(self,line): 
        """
        using requests.get() to get the url and then printing the value of the stock inputted
        """
        r=requests.get('http://download.finance.yahoo.com/d/quote.csv?s='+line+'&f=l1')
        data=r.text
        value=float(data)
        print value
    def do_greet(self,line):
        """
        getuser() used to get the user that is logged in 
        """
        print "Hi! %s" %(getuser())

if __name__ == '__main__':
    app = Application()
    app.cmdloop()

