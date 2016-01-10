Green Graph Assignment
======================

This is a simple program to plot the proportion of green space between two locations.
This forms part of the Research Software Engineering With Python MPHYG001 course.

Instalation
-----------

In the root directory enter

$ python install setup.py

or
 
$ sudo python install setup.py

Usage
-----

To display all options:

$ greengraph --help

A typical graph showing green space between London and Manchester would look like:

$ greengraph --start London --end Manchester --steps 50 --out London_to_manchester.png

(C) University College London 2010-2014
This software is licensed under the terms of the MIT license
See LICENSE.md for the license details.
