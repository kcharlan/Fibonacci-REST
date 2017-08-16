
READ ME documentation for fibonacci.py REST service and a functionality tests
battery for the service.

Separate sections are below for each part.


====================
    fibonacci.py
====================


DESCRIPTION

The fibonacci.py service is a REST service that receives a GET command which
specifies how many Fibonacci numbers to return. The service will then return:

1) A first line indicating a status code (0 for success, 1 or higher for error
conditions), followed by additional lines.

2) Additional lines containing data or error description text.

The service will check for incorrect or missing input.

If the request was valid, the second line will be a CSV list of numbers
containing the specified quantity of Fibonacci numbers.

Otherwise, the remaining lines will be text describing the error encountered.

The Fibonacci sequence returned is the modern version starting from 0. That
sequence begins 0,1,1,2,... 


HOW TO START THE SERVICE

Please check the INSTALLATION.txt file to confirm all dependencies are met,
before attempting to start this service.

After that, also confirm your user has execute permission on the fibonacci.py
file. Then run the service with ./fibonacci.py in the directory the file
resides in. For example:

me@ubuntu:~$ cd /home/me/Downloads/fibonacci/

me@ubuntu:~/Downloads/fibonacci$ ./fibonacci.py

If no parameter is specified after the ./fibonacci.py command, the default URI
for the service is http://localhost:8080/fibonacci

If a port number is specified, like:

me@ubuntu:~/Downloads/fibonacci$ ./fibonacci.py 1234

The service will be on http://localhost:1234/fibonacci

The service will continue to run until an interrupt is sent to the
./fibonacci.py process. This could be sending control-C in the terminal where
it was run, or posting an interrupt or kill signal, etc.

The process will send log output to STDERR. This can show up on the terminal if
not redirected, or can be redirected elsewhere.


USAGE

Once the service is running, you can make a GET call or point a web browser at

http://localhost:8080/fibonacci

This will return a block of text that is a help message.


To obtain a CSV list of fibonacci numbers, use:

GET localhost:8080/fibonacci/<X>

or

http://localhost:8080/fibonacci/<X>

where <X> is a number specifying the quantity of Fibonacci numbers to return.


Examples:

GET localhost:8080/fibonacci/12

or

http://localhost:8080/fibonacci/12


Will return the result:

0,1,1,2,3,5,8,13,21,34,55,89



LIMITATIONS

- Parameter for Fibonacci sequence length is limited to a maximum of 10,000

The sequence length parameter has been capped at 10,000 Fibonacci numbers.
Attempts to request more than that will result in an out-of-bounds error
message.

This was done to protect the service from accidental or intentional requests
for extremely long lists, which would result in extensive execution times.


- WebPY framework limitations

Any and all WebPY framework limitations would also apply to this service. These
include, but are not limited to:

	o Performance considerations and limitations

	    The WebPY installation documentation explicitly calls out
	    performance limitations as a consideration. The framework's native
	    web server was not designed for production or high performance
	    workloads.

	    The framework does have the capability to be plugged into an
	    external web server for these scenarios. However, the Fibonacci
	    service was not written for nor tested in any of those
	    configurations.

	o Framework robustness

	    There may be ways to access the framework web server or to
	    inject requests that result in framework-generated errors or
	    crashes. Basic functionality and error checking testing was
	    performed and did not find any issues, but extensive testing
	    against the framework was not performed.

	   
- Built and tested on a single platform

The Fibonacci service was built and tested exclusively on the Ubuntu Desktop
64-bit 16.04.3 distribution. Although there is nothing platform or distribution
specific in this service implementation, no testing was performed on other
platforms to validate functionality or configuration on them.





=====================
    func_tests.py
=====================


DESCRIPTION

The func_tests.py program is a battery of functionality tests for the
fibonacci.py service. It makes various REST calls to the service, checks the
result codes that are returned, and validates we got the expected return code
for the input.

The results of the tests are sent to STDOUT, and are in human readable form.
Each battery of tests is run and displayed in its own section.


HOW TO RUN THE TESTS

Please check the INSTALLATION.txt file to confirm all dependencies are met,
before attempting to start the test routine.

Also confirm the fibonacci service is already running. Although the test
routine will gracefully handle and report on the service being down, the
test framework aborts and does not continue testing if the service is not
responding.

Then confirm your user has execute permission on the func_tests.py file.
Then run the service with ./func_tests.py in the directory the file
resides in. For example:

me@ubuntu:~$ cd /home/me/Downloads/fibonacci/

me@ubuntu:~/Downloads/fibonacci$ ./func_tests.py

If no parameter is specified after the ./func_tests.py command, the test 
routines will assume the default URI for the fibonacci service, which will
reside at http://localhost:8080/fibonacci

If a port number is specified, like:

me@ubuntu:~/Downloads/fibonacci$ ./func_tests.py 1234

The routine will run tests against http://localhost:1234/fibonacci

A battery of functionality tests will be run. The results of each test will
be displayed on STDOUT, along with a note at the end whether any failed tests
were detected. The output can be redirected if so desired.


LIMITATIONS

- The port number parameter is not validated

There is no validation performed against the first parameter passed into the
test routine. However, the program will gracefully handle an inability to
connect, and will report that the service is not responding and abort the
test run.

	   
- Built and tested on a single platform

The functional test routines were built and tested exclusively on the Ubuntu
Desktop 64-bit 16.04.3 distribution. Although there is nothing platform or
distribution specific in this service implementation, no testing was performed
on other platforms to validate functionality or configuration on them.

