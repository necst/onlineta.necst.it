#!/usr/bin/env python

import os
import re
from os import listdir
from os.path import isfile, join

pages_dir = './'
website_dir = '../'
include_dir = '../html/'

include_regexp = re.compile('.*<!--[\s]*include[\s]*:[\s]*([a-zA-Z\._-]+)[\s]*-->.*')

for filename in listdir(pages_dir):
	in_fullpath = join(pages_dir, filename) 
	if in_fullpath.endswith('.html') and isfile(join(pages_dir, filename)):

		print('processing: ' + in_fullpath)
		out_fullpath = join(website_dir, filename)

		with open(in_fullpath, 'rt') as data_in, open(out_fullpath, 'wt') as data_out:
			for l in data_in:
				res = include_regexp.match(l)
				if res:
					include_filename = res.groups(1)[0]
					print('detected in_fullpathclude: ' + include_filename)
					include_fullpath = join(include_dir, include_filename)
					with open(include_fullpath, 'rt') as include_in:
						for l_include in include_in:
							data_out.write(l_include)
				else:
					data_out.write(l)