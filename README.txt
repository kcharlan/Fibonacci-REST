
READ ME documentation for fibonacci.py REST service


DESCRIPTION

The fibonacci.py service is a REST service that receives a GET command which
specifies how many Fibonacci numbers to return. The service will then return
a CSV list of numbers containing the specified quantity of Fibonacci numbers.

The Fibonacci sequence returned is the modern version starting from 0. That
sequence begins 0,1,1,2,... 

The service will check for incorrect or missing input, and will respond with
text results describing the error encountered. Otherwise, if the input is
valid, it will return a CSV list of Fibonacci numbers.


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

This was done to protect the service from accidental or intentional malformed
requests for extremely long lists, which would result in extensive execution
times.


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


