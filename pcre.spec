Summary:	Perl-Compatible Regular Expression library
Name:		pcre
Version:	3.1
Release:	2
License:	GPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Vendor:		Philip Hazel <ph10@cam.ac.uk>
Source:		ftp://ftp.cus.cam.ac.uk/pub/software/programs/pcre/pcre-%{version}.tar.gz
patch:		pcre-DESTDIR.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCRE stands for the Perl Compatible Regular Expression library. It
contains routines to match text against regular expressions similar to
perl's. It also contains a POSIX compatibility library.

%package devel
Summary:	Perl-Compatible Regular Expression header files and development documentation
Summary(pl):	Pliki nagłówkowe i dokumentacja do blibliotek pcre
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Perl-Compatible Regular Expression header files and development
documentation.

%description -l pl devel
Pliki nagłówkowe i dokumentacja do blibliotek pcre.

%package static
Summary:	Perl-Compatible Regular Expression static libraries
Summary(pl):	Biblioteki statyczne pcre
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Perl-Compatible Regular Expression library staic libraris.

%description -l pl static
Biblioteki statyczne pcre.

%package -n pgrep
Summary:	Grep using Perl Compatible Regular Expressions
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narzędzia/Tekst

%description -n pgrep
pgrep is a grep workalike which uses perl-style regular expressions
instead of POSIX regular expressions.

%prep
%setup -q
%patch -p1

%build
%configure \
	--enable-shared
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*
strip $RPM_BUILD_ROOT%{_bindir}/pgrep

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man?/* \
	README NEWS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/pcre-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_mandir}/man3/*
%{_includedir}/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a

%files -n pgrep
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pgrep
%{_mandir}/man1/pgrep.1*
