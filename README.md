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

When using the API, it is also useful to read [the Noark 5
standard](https://www.arkivverket.no/arkivverket/Offentleg-forvalting/Noark/Noark-5/Standarden),
available from Arkivverket.

This test suite was written to test the code in 
https://gitlab.com/OsloMet-ABI/nikita-noark5-core .

The latest version of the test scripts can be found in
https://codeberg.org/noark/noark5-tester


Known dependencies
------------------

- python-magic
- PyPDF2
- pytz
- six
