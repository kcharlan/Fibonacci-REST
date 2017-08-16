#!/usr/bin/env python

import sys

# this is an external framework that requires installation
import requests


#
# This program runs through several functional tests, to validate the
# fibonacci.py service is working properly. It submits several different
# inputs, some valid and some invalid, and checks the result codes.
#
# If no parameter is given, then the tests default to localhost port 8080,
# which is the default for the WebPY framework.
#
# Otherwise, the first parameter is used as the port number in the URI to
# test against
#
# NOTE: There is no validation of the parameter to validate it is a number
#       or valid URL. However, a bad URL will not crash this program. It
#       will just return the same error message as if the service was down.
#


###################  Functions #######################


#
# helper utilities
#

# pulls out the result code from the response text
def get_result_code( response_text ) :
    output = response_text.text
    return output.split('\n',1)[0]


# separated this to keep a dead connection from aborting the program
def check_url( url ):

    try:
        return requests.get( url )

    except:
        return False


# general test framework
def run_single_test( url_check, expected_code ) :

    #
    # check url, and validate return code is the one we wanted
    # output results of the test and return TRUE or FALSE
    #
    result = check_url( url_check )

    if not result:
        print "\n\nError. Service is not responding. Please check "+url_check
        return False

    else:
        returncode = get_result_code( result )

    if returncode != expected_code :
        print "Response code was not valid. Expected: '" + expected_code + "'"
        print "but instead got: '" + returncode + "'"
        return False

    else:
        print "Test successful: " + url_check
        return True



#
# Run all functionality tests - the actual main body of the testing routine
#

def run_tests() :

    #
    # check if service is running, and validate return code is for the
    # help text
    #

    All_test_OK = True

    result = check_url( url_base )

    if not result:
        print "\n\nError. Service is not responding. Please check "+url_base
        return False

    else:
        print "\nService is responding."
        returncode = get_result_code( result )

    if returncode != "1" :
        print "Response code was not valid. Expected 1 for help text, but"
        print "instead got: '" + returncode + "'"
        All_test_OK = False

    else:
        print "General help message received."


    #
    # submit an invalid paramter
    #

    print "\nTesting invalid parameters:"

    new_url = url_base + "/xyzzy"
    if not run_single_test( new_url, "2" ):
        print "***Test failed: Invalid parameter test 'xyzzy'"
        print new_url
        All_test_OK = False

    new_url = url_base + "/5a"
    if not run_single_test( new_url, "2" ):
        print "***Test failed: Invalid parameter test '5a'"
        print new_url
        All_test_OK = False

    new_url = url_base + "/0000"
    if not run_single_test( new_url, "2" ):
        print "***Test failed: Invalid parameter test '0000'"
        print new_url
        All_test_OK = False


    #
    # submit out of bounds parameters
    #

    print "\nTesting out of bounds parameters:"

    new_url = url_base + "/-6"
    if not run_single_test( new_url, "3" ):
        print "***Test failed: Invalid parameter test '-6'"
        print new_url
        All_test_OK = False

    new_url = url_base + "/10005"
    if not run_single_test( new_url, "3" ):
        print "***Test failed: Invalid parameter test '10005'"
        print new_url
        All_test_OK = False

    new_url = url_base + "/0"
    if not run_single_test( new_url, "3" ):
        print "***Test failed: Invalid parameter test '0'"
        print new_url
        All_test_OK = False


    #
    # submit valid parameters
    #

    print "\nTesting valid parameters:"

    new_url = url_base + "/12"
    if not run_single_test( new_url, "0" ):
        print "***Test failed: Invalid parameter test '12'"
        print new_url
        All_test_OK = False

    new_url = url_base + "/200"
    if not run_single_test( new_url, "0" ):
        print "***Test failed: Invalid parameter test '200'"
        print new_url
        All_test_OK = False


    # end of running test cases
    return All_test_OK


###################  Main body #######################


#
# if first parameter is a present, then we use it as a port number
# otherwise, we default to port 8080, which is the default port number
# for the WebPY framework
#

if len(sys.argv) > 1 :
    url_base = "http://localhost:"+sys.argv[1]+"/fibonacci"
else:
    url_base="http://localhost:8080/fibonacci"


# run functionality tests
all_passed = run_tests()


print "\nFunctional testing complete"

if not all_passed :
    print "Errors were detected.\n"
else:
    print "All test passed successfully.\n"



