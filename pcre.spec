Summary:	Perl-Compatible Regular Expression library
Name:		pcre
Version:	3.4
Release:	2
License:	GPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Vendor:		Philip Hazel <ph10@cam.ac.uk>
Source0:	ftp://ftp.cus.cam.ac.uk/pub/software/programs/pcre/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCRE stands for the Perl Compatible Regular Expression library. It
contains routines to match text against regular expressions similar to
perl's. It also contains a POSIX compatibility library.

%package devel
Summary:	Perl-Compatible Regular Expression header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do blibliotek pcre
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Perl-Compatible Regular Expression header files and development
documentation.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do blibliotek pcre.

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

%package -n pcregrep
Summary:	Grep using Perl Compatible Regular Expressions
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narzêdzia/Tekst
Obsoletes:	pgrep

%description -n pcregrep
pgrep is a grep workalike which uses perl-style regular expressions
instead of POSIX regular expressions.

%prep
%setup -q

%build
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* $RPM_BUILD_ROOT/lib
(cd $RPM_BUILD_ROOT%{_libdir}
ln -sf ../../lib/libpcre.so.*.*.* libpcre.so
ln -sf ../../lib/libpcreposix.so.*.*.* libpcreposix.so)

gzip -9nf README NEWS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/pcre-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_mandir}/man3/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n pcregrep
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcregrep
%{_mandir}/man1/pcregrep.1*
