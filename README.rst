Nessus Report Parser
====================

Nessus Report Parser transforms a nessus xml report file into a Plain Python object

The object contains sub objects, mirroring the XML node hierarchy, parsing date string and integer values and attributes to their appropriate Python Datastructures.

Usage
-----

::

    from nessus import parse_nessus_file, parse_nessus_xml
    parse_nessus_file('path/to/nessus/file.nessus')

