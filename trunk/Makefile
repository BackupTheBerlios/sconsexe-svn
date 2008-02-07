# Makefile for SCons executable project
#
# To build you need Python (of course) from http://www.python.org and Inno
# Setup installer from http://www.jrsoftware.org/
#
# NOTE: Last changes where tests *only* on an MSYS system

# Miki Tebeka <miki.tebeka@gmail.com>

# Find Python and Inno Setup
ifeq ($(OSTYPE),cygwin)
	PYTHON = $(shell cygpath -au `cmd /c pyexe.py`)
	INNO = $(shell cygpath -au `cmd /c innoexe.py`)
else
	PYTHON = $(shell cmd /c pyexe.py)
	INNO = $(shell cmd /c innoexe.py)
endif
PYDIR=$(dir $(PYTHON))

# Version of SCons
VERSION = $(shell $(PYTHON) setup.py --version)

ARCHIVE = scons-$(VERSION)-build.zip
BUILD_FILES = \
	DLLs.zip \
	Makefile \
	bin/*.exe \
	exe-setup.py \
	genscript.py \
	header.txt \
	innoexe.py \
	pyexe.py \
	pylib.zip \
	scons-man.html \
	scons-user.pdf \
	scons.iss \
	wizard.bmp \
	wizard_small.bmp
			  
all: version.iss scons.py sconsign.py scons-time.py DLLs pylib
	$(PYTHON) exe-setup.py py2exe -i zlib
	"$(INNO)" scons.iss

version.iss:
	echo > $@ "AppVerName=SCons $(VERSION)"
	echo >> $@ "OutputBaseFilename=scons_$(VERSION)_setup"

scons.py: script/scons
	$(PYTHON) genscript.py header.txt $< > $@

sconsign.py: script/sconsign
	$(PYTHON) genscript.py header.txt $< > $@

scons-time.py: script/scons-time
	$(PYTHON) genscript.py header.txt $< > $@

DLLs:
	mkdir $@
	cp $(PYDIR)/DLLs/* $@
	cp $(shell which msvcp71.dll) $@
	cp $(shell which msvcr71.dll) $@

pylib:
	cp -ru $(PYDIR)/Lib $@
	rm -fr $@/site-packages/*

dist:
	zip -r9 $(ARCHIVE) $(BUILD_FILES)

clean:
	rm -fr Output
	rm -fr dist build
	rm -f scons.py sconsign.py
	rm -f version.iss
	rm -f $(ARCHIVE)
	rm -fr DLLs pylib

fresh: clean all

.PHONY: all clean fresh
