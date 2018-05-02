Nessus Report Parser
====================

[![Build Status](https://travis-ci.org/siteblindado/nessus-report-parser.svg?branch=master)](https://travis-ci.org/siteblindado/nessus-report-parser#)

Nessus Report Parser transforms a nessus xml report file into a Plain Python object

The object contains sub objects, mirroring the XML node hierarchy, parsing date string and integer values and attributes to their appropriate Python Datastructures.

Usage
-----

::

    from nessus_parser import parse_nessus_file, parse_nessus_xml
    parse_nessus_file('path/to/nessus/file.nessus')

