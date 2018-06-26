#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os


def get_type():
	return "BINARY"

def get_desc():
	return "squirrel command line interpreter"

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
	    'squirrel/sq/sq.c',
	    ])
	my_module.compile_version("c++", 2011)
	my_module.add_depend([
	    'squirrel-core',
	    'squirrel-std',
	    'cxx',
	    ])
	return True


