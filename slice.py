#!/usr/bin/env python

import sys

# Slice each file into 32 parts by dealing
NUM_SLICES = 32
numlines = 0
for f in sys.argv[1:]:
	outf = [open('slices/%s-slice%02d' % (f, i), 'w') for i in xrange(NUM_SLICES)]
	inf = open(f, 'r')
	i = 0
	for line in inf:
		numlines += 1
		if numlines % 10000 == 0:
			print numlines
		outf[i].write(line)
		i = (i + 1) % NUM_SLICES
print numlines
