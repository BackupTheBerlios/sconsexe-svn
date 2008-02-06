#!/usr/bin/env python

from sys import argv, stdin, stderr

if len(argv) not in (2, 3):
    from os.path import basename
    raise SystemExit("usage: %s TEMPLATE [FILENAME]" % basename(argv[0]))

if len(argv) == 2:
    info = stdin
else:
    try:
        info = open(argv[2], "rt")
    except IOError:
        raise SystemExit("error: can't open %s for reading" % argv[2])

try:
    templ = open(argv[1], "rt").read()
except IOError:
    raise SystemExit("error: can't open template %s for reading" % argv[1])

for line in info:
    if line.startswith("# END STANDARD SCons SCRIPT HEADER"):
        break
else: # Not found
    raise SystemExit("error: can't find end of script header")

print templ
for line in info:
    print line.rstrip()
