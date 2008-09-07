#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
%bcond_without	tests		# don't perform "make check"
#
Summary:	Perl-Compatible Regular Expression library
Summary(pl.UTF-8):	Biblioteka perlowych wyrażeń regularnych
Summary(pt_BR.UTF-8):	Biblioteca de expressões regulares versão
Name:		pcre
Version:	7.8
Release:	1
License:	BSD (see LICENCE)
Group:		Libraries
Source0:	ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{name}-%{version}.tar.bz2
# Source0-md5:	141132d6af14dccc7b08fa797e4fd441
Patch0:		%{name}-pcreposix-glibc-conflict.patch
Patch1:		%{name}-link.patch
URL:		http://www.pcre.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	bzip2-devel	
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	readline-devel	
BuildRequires:	zlib-devel	
Obsoletes:	libpcre0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCRE stands for the Perl Compatible Regular Expression library. It
contains routines to match text against regular expressions similar to
Perl's. It also contains a POSIX compatibility library.

%description -l es.UTF-8
A biblioteca PCRE é um set de funções que implementam expressões
regulares utilizando-se da mesma sintaxe e semântica do perl 5. Possui
sua própria API nativa, bem como um set de funções wrapper para
corresponder ao padrão POSIX de expressões regulares.

%description -l pl.UTF-8
PCRE (Perl-Compatible Regular Expression) oznacza bibliotekę wyrażeń
regularnych kompatybilnych z perlowymi. Zawiera funkcje dopasowujące
tekst do wyrażeń regularnych podobnych do tych znanych z Perla.
Zawiera także bibliotekę kompatybilną z POSIX.

%description -l pt_BR.UTF-8
A biblioteca PCRE é um conjunto de funções que implementam expressões
regulares utilizando-se da mesma sintaxe e semântica do perl 5. Possui
sua própria API nativa, bem como um conjuntos de funções wrapper para
corresponder ao padrão POSIX de expressões regulares.

%package devel
Summary:	Perl-Compatible Regular Expression header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do bibliotek pcre
Summary(pt_BR.UTF-8):	Arquivos para desenvolvimento com pcre
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libpcre0-devel

%description devel
Perl-Compatible Regular Expression header files and development
documentation.

%description devel -l es.UTF-8
A biblioteca PCRE é um set de funções que implementam expressões
regulares utilizando-se da mesma sintaxe e semântica do perl 5. Possui
sua própria API nativa, bem como um set de funções wrapper para
corresponder ao padrão POSIX de expressões regulares.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek pcre.

%description devel -l pt_BR.UTF-8
A biblioteca PCRE é um conjunto de funções que implementam expressões
regulares utilizando-se da mesma sintaxe e semântica do perl 5. Possui
sua própria API nativa, bem como um conjunto de funções wrapper para
corresponder ao padrão POSIX de expressões regulares.

%package static
Summary:	Perl-Compatible Regular Expression static libraries
Summary(pl.UTF-8):	Biblioteki statyczne pcre
Summary(pt_BR.UTF-8):	Arquivos para desenvolvimento estático com pcre
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Perl-Compatible Regular Expression library static libraries.

%description static -l es.UTF-8
A biblioteca PCRE é um set de funções que implementam expressões
regulares utilizando-se da mesma sintaxe e semântica do perl 5. Possui
sua própria API nativa, bem como um set de funções wrapper para
corresponder ao padrão POSIX de expressões regulares.

%description static -l pl.UTF-8
Biblioteki statyczne pcre.

%description static -l pt_BR.UTF-8
A biblioteca PCRE é um conjunto de funções que implementam expressões
regulares utilizando-se da mesma sintaxe e semântica do perl 5. Possui
sua própria API nativa, bem como um conjunto de funções wrapper para
corresponder ao padrão POSIX de expressões regulares.

%package cxx
Summary:	C++ wrapper to PCRE library
Summary(pl.UTF-8):	Interfejs C++ do biblioteki PCRE
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description cxx
C++ wrapper to PCRE library.

%description cxx -l pl.UTF-8
Interfejs C++ do biblioteki PCRE.

%package cxx-devel
Summary:	Header file for C++ wrapper to PCRE library
Summary(pl.UTF-8):	Plik nagłówkowy interfejsu C++ do biblioteki PCRE
Group:		Development/Libraries
Requires:	%{name}-cxx = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description cxx-devel
Header file for C++ wrapper to PCRE library.

%description cxx-devel -l pl.UTF-8
Plik nagłówkowy interfejsu C++ do biblioteki PCRE.

%package cxx-static
Summary:	Static version of pcrecpp library
Summary(pl.UTF-8):	Statyczna wersja biblioteki pcrecpp
Group:		Development/Libraries
Requires:	%{name}-cxx-devel = %{version}-%{release}

%description cxx-static
Static version of pcrecpp library.

%description cxx-static -l pl.UTF-8
Statyczna wersja biblioteki pcrecpp.

%package -n pcregrep
Summary:	Grep using Perl Compatible Regular Expressions
Summary(pl.UTF-8):	Grep używający perlowych wyrażeń regularnych
Group:		Applications/Text
Obsoletes:	pgrep

%description -n pcregrep
pgrep is a grep workalike which uses perl-style regular expressions
instead of POSIX regular expressions.

%description -n pcregrep -l pl.UTF-8
pgrep jest programem działającym podobnie do grepa, ale używających
perlowych wyrażeń regularnych, a nie posiksowych.

%package -n pcretest
Summary:	A program for testing Perl-comaptible regular expressions
Summary(pl.UTF-8):	Program do testowania kompatybilnych z perlem wyrażeń regualarnych
Group:		Applications/Text

%description -n pcretest
pcretest is a program which you can use to test regular expression

%description -n pcretest -l pl.UTF-8
pcretest jest programem za pomocą można sprawdzić poprawność wyrażenia regularnego

%package doc-html
Summary:	Documentation for PCRE in HTML format
Summary(pl.UTF-8):	Dokumentacja dla PCRE w formacie HTML
Group:		Applications/Text

%description doc-html
Documentation for PCRE in HTML format.

%description doc-html -l pl.UTF-8
Dokumentacja dla PCRE w formacie HTML.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CXXLDFLAGS="%{rpmldflags}" \
	%{!?with_static_libs:--enable-static=no} \
	--enable-utf8 \
	--enable-unicode-properties \
	--enable-pcregrep-libz \
	--enable-pcregrep-libbz2 \
	--enable-pcretest-libreadline

%{__make}

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/libpcre.so.* $RPM_BUILD_ROOT/%{_lib}
mv -f $RPM_BUILD_ROOT%{_libdir}/libpcreposix.so.* $RPM_BUILD_ROOT/%{_lib}

ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libpcre.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpcre.so
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libpcreposix.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpcreposix.so

install pcredemo.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf $RPM_BUILD_ROOT%{_docdir}/pcre

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   cxx -p /sbin/ldconfig
%postun cxx -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS LICENCE ChangeLog
%attr(755,root,root) /%{_lib}/libpcre.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libpcre.so.0
%attr(755,root,root) /%{_lib}/libpcreposix.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libpcreposix.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcre-config
%attr(755,root,root) %{_libdir}/libpcre.so
%attr(755,root,root) %{_libdir}/libpcreposix.so
%{_libdir}/libpcre.la
%{_libdir}/libpcreposix.la
%{_includedir}/pcre.h
%{_includedir}/pcreposix.h
%{_pkgconfigdir}/libpcre.pc
%{_mandir}/man1/pcre-config.1*
%{_mandir}/man3/pcre*.3*
%exclude %{_mandir}/man3/pcrecpp.3*
%{_examplesdir}/%{name}-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpcre.a
%{_libdir}/libpcreposix.a
%endif

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcrecpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcrecpp.so.0

%files cxx-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcrecpp.so
%{_libdir}/libpcrecpp.la
%{_includedir}/pcrecpp.h
%{_includedir}/pcre_scanner.h
%{_includedir}/pcre_stringpiece.h
%{_includedir}/pcrecpparg.h
%{_pkgconfigdir}/libpcrecpp.pc
%{_mandir}/man3/pcrecpp.3*

%if %{with static_libs}
%files cxx-static
%defattr(644,root,root,755)
%{_libdir}/libpcrecpp.a
%endif

%files -n pcregrep
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcregrep
%{_mandir}/man1/pcregrep.1*

%files -n pcretest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcretest
%{_mandir}/man1/pcretest.1*

%files doc-html
%defattr(644,root,root,755)
%doc doc/html/*
