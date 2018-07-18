#!/usr/bin/env python

import sys
import io

# Slice each file into 32 parts by dealing
NUM_SLICES = 32
numlines = 0
for f in sys.argv[1:]:
	outf = [io.open('slices/%s-slice%02d' % (f, i), 'w', 1024*1024/NUM_SLICES) for i in xrange(NUM_SLICES)]
	inf = io.open(f, 'r', 1024*1024)
	i = 0
	for line in inf:
		numlines += 1
		if numlines % 10000 == 0:
			print numlines
		outf[i].write(line)
		i = (i + 1) % NUM_SLICES
print numlines
