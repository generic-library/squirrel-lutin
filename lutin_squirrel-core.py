#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "squirrel script interpreter"

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
	    'squirrel/squirrel/sqmem.cpp',
	    'squirrel/squirrel/sqbaselib.cpp',
	    'squirrel/squirrel/sqapi.cpp',
	    'squirrel/squirrel/sqlexer.cpp',
	    'squirrel/squirrel/sqclass.cpp',
	    'squirrel/squirrel/sqvm.cpp',
	    'squirrel/squirrel/sqtable.cpp',
	    'squirrel/squirrel/sqstate.cpp',
	    'squirrel/squirrel/sqobject.cpp',
	    'squirrel/squirrel/sqcompiler.cpp',
	    'squirrel/squirrel/sqdebug.cpp',
	    'squirrel/squirrel/sqfuncstate.cpp',
	    ])
	my_module.compile_version("c++", 2011)
	my_module.add_depend([
	    'z',
	    'm',
	    'c'
	    ])
	my_module.add_header_file([
	    'squirrel/include/sqstdblob.h',
	    'squirrel/include/sqstdio.h',
	    'squirrel/include/sqconfig.h',
	    'squirrel/include/squirrel.h',
	    ],
	    destination_path="squirrel")
	#my_module.add_path("squirrel/squirrel/")
	return True


