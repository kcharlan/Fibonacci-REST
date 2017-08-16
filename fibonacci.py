#!/usr/bin/env python


#
# NOTE: Web framework defaults to port 8080, unless the first parameter specifies
# an alternate port to listen on.
#


# Include web server framework. Needed for mini web server to listen on port for requests, and
# provide responses.

import web



###################  Functions #######################

def help_text():
    output = "1\n\nFibonacci computation routine\n\n"
    output += "A GET request with no paramters or an invalid parameter returns\n"
    output += "this help message. A parameter that is not a number is considered invalid.\n\n"
    output += "Use an HTTP GET with /fibonacci/X  where X is the length of the\n"
    output += "Fibonacci sequence to return, starting from the beginning.\n\n"
    output += "The length is capped at a maximum of 10,000 Fibonacci numbers.\n"
    output += "Attempting to request more than that will return an out of bounds error.\n\n\n"
    output += "Example:\n\n"
    output += "/fibonacci/5  will output the first 5 Fibonacci numbers, in sequence.\n\n"
    return output


def convert_number( x ):
    try:
        return int( x )
    except:
        return False


#
# compute the sequence of Fibonacci numbers, starting from 0,1,1,2...
#
# input paramter is the length of the sequence to return. i.e. 5 means give
# the first 5 numbers. NOTE: the input value is capped at a maximum of 10,000.
# requesting more than 10,000 (10000) will return an out-of-bounds error.
#
# output: - the first line is a status code indicating success or failure
#           0 means success, 1 and higher are error indicators
#
#        - second line will be a CSV list of the requested length of Fibonacci
#          numbers, or additional lines of error messaging
#
# assumptions:
# - 10,000 length Fibonacci sequence computation is maximum reasonable
#     computational effort and delay
#
# - function will gracefully handle a bad input parameter, and will do its own checking
#
# dependencies:
# - the convert_number() function defined above, to convert the input
# parameter to an integer, or else notify us of an error
#  

def fibonacci_sequence( num ):

    seed1 = 0
    seed2 = 1

    # convert/validate parameter
    result = convert_number( num )

    # extra check required because False evaluates to 0 as well, and we want to display
    # that 0 is out of bounds instead of "is not a number"
    if not result and num != "0" :
        output = "2\n\nError: Parameter '" + num + "' is not a number.\n"

    # capping at 10,000 requests, to protect the service
    # even 10,000 runs for quite a while (a few seconds)
    elif result < 1 or result > 10000 or num == "0" :
        output = "3\n\nError: Parameter " + str( num ) + " is out of bounds.\n"

    else:

        output = "0\n"
        output += str( seed1 )
        result -= 1

        while result > 0 :
            newseed = seed1 + seed2
            seed1 = seed2
            seed2 = newseed
            output += "," + str( seed1 )
            result -= 1

    return output


###################  Main body #######################


urls = (
    '/fibonacci', 'help',
    '/fibonacci/(.*)', 'compute'
)

app = web.application(urls, globals())

class help:        
    def GET(self):
        return help_text()

class compute:
    def GET(self, count):
        return fibonacci_sequence( count )


if __name__ == "__main__":
    app.run()
