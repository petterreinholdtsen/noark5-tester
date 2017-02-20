Verify NOARK 5 core API behaviour
=================================

Connect to an Noark 5 REST API and see if it work as expected.
Execute runtest to give it a go.

A demonstration API is available from http://n5test.kxml.no/api/ .
This is not quite working according to the specification available
from
https://samdok.com/leveranser/leveranser-2016/noark5-tjenestegrensesnitt-v-1-0-beta/ .
To connect the script to this demonstration API, run it like this::

  ./runtest --reference

This test suite was written to test the code in 
https://github.com/HiOA-ABI/nikita-noark5-core .

The latest version of the test scripts can be found in
https://github.com/petterreinholdtsen/noark5-tester

You might need to install `python-mechanize` if you don't already have it
installed.
