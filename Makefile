PYINSTALLER = pyinstaller
MKDIR = mkdir -p
RM = rm -rf
prefix = /usr/local

all: dnsbl_test

dnsbl_test: dist/__init__
	cp dist/__init__ dnsbl_test

dist/__init__:
	$(PYINSTALLER) --onefile dnsbl/__init__.py

test: dnsbl_test
	dnsbl_test 113.169.160.242
	dnsbl_test 176.106.153.120
	dnsbl_test 2001:DB8:abc:123::42
clean:
	$(RM) dnsbl/*.pyc
	$(RM) build/ dist/ dnsbl.egg-info/ *.spec *~
	$(RM) dnsbl_test

install:
	$(MKDIR) $(prefix)/bin
	cp -f dnsbl_test $(prefix)/bin
