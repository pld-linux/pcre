%define name	pcre
%define version	2.08
%define release	1

Summary:	Perl-Compatible Regular Expression library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Copyright:	GPL
Group:		Development/Libraries
Vendor:		Philip Hazel <ph10@cam.ac.uk>
Source: ftp://ftp.cus.cam.ac.uk/pub/software/programs/pcre/pcre-%{version}.tar.gz
Patch: pcre-make.patch
Packager:	Damien Miller <dmiller@ilogic.com.au>
BuildRoot:	/tmp/%{name}-%{version}

%package -n pgrep
Summary: Grep using Perl Compatible Regular Expressions
Group:		Utilities/Text

%description

PCRE stands for the Perl Compatible Regular Expression library. It 
contains routines to match text against regular expressions similar to
perl's. It also contains a POSIX compatibility library.

%description -n pgrep

pgrep is a grep workalike which uses perl-style regular expressions 
instead of POSIX regular expressions.

%prep

%setup

%patch -p0

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib
mkdir -p $RPM_BUILD_ROOT/usr/include
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/man/man3
install libpcre.a $RPM_BUILD_ROOT/usr/lib
install libpcreposix.a $RPM_BUILD_ROOT/usr/lib
install pcre.h $RPM_BUILD_ROOT/usr/include
install pcreposix.h $RPM_BUILD_ROOT/usr/include
install pcre.3 $RPM_BUILD_ROOT/usr/man/man3
install pcreposix.3 $RPM_BUILD_ROOT/usr/man/man3
install pgrep $RPM_BUILD_ROOT/usr/bin
install pgrep.1 $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENCE README Tech.Notes
%attr(0644,root,root) /usr/lib/libpcre.a
%attr(0644,root,root) /usr/lib/libpcreposix.a
%attr(0644,root,root) /usr/man/man3/pcre.3
%attr(0644,root,root) /usr/man/man3/pcreposix.3
%attr(0644,root,root) /usr/include/pcre.h
%attr(0644,root,root) /usr/include/pcreposix.h

%files -n pgrep
%defattr(-,root,root)
%attr(0755,root,root) /usr/bin/pgrep
%attr(0644,root,root) /usr/man/man1/pgrep.1

%changelog
* Thu Sep 09 1999 Damien Miller <dmiller@ilogic.com.au>
- Updated to v2.08
* Fri May 28 1999 Damien Miller <dmiller@ilogic.com.au>
- Built RPMs
