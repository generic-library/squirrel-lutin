#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "squirrel script interpreter (std wrapping)"

def get_licence():
	return "MIT"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "squirrel"

def get_maintainer():
	return ["Alberto Demichelis <albertodemichelis@hotmail.com>"]

def get_version():
	return [3,1]

def configure(target, my_module):
	my_module.add_src_file([
	    'squirrel/sqstdlib/sqstdaux.cpp',
	    'squirrel/sqstdlib/sqstdstream.cpp',
	    'squirrel/sqstdlib/sqstdrex.cpp',
	    'squirrel/sqstdlib/sqstdsystem.cpp',
	    'squirrel/sqstdlib/sqstdio.cpp',
	    'squirrel/sqstdlib/sqstdblob.cpp',
	    'squirrel/sqstdlib/sqstdmath.cpp',
	    'squirrel/sqstdlib/sqstdstring.cpp',
	    ])
	my_module.compile_version("c++", 2011)
	my_module.add_depend([
	    'squirrel-core'
	    ])
	my_module.add_header_file([
	    'squirrel/include/sqstdsystem.h',
	    'squirrel/include/sqstdaux.h',
	    'squirrel/include/sqstdstring.h',
	    'squirrel/include/sqstdblob.h',
	    'squirrel/include/sqstdio.h',
	    'squirrel/include/sqconfig.h',
	    'squirrel/include/squirrel.h',
	    'squirrel/include/sqstdmath.h',
	    ],
	    destination_path="squirrel")
	return True


