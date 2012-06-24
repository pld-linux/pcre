#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	Perl-Compatible Regular Expression library
Summary(pl):	Biblioteka perlowych wyra�e� regularnych
Summary(pt_BR):	Biblioteca de express�es regulares vers�o
Name:		pcre
Version:	7.0
Release:	1
License:	BSD (see LICENCE)
Group:		Libraries
Source0:	ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{name}-%{version}.tar.bz2
# Source0-md5:	b97e3bb84bd665e0fbb7a90344d65a43
URL:		http://www.pcre.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
Obsoletes:	libpcre0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCRE stands for the Perl Compatible Regular Expression library. It
contains routines to match text against regular expressions similar to
Perl's. It also contains a POSIX compatibility library.

%description -l es
A biblioteca PCRE � um set de fun��es que implementam express�es
regulares utilizando-se da mesma sintaxe e sem�ntica do perl 5. Possui
sua pr�pria API nativa, bem como um set de fun��es wrapper para
corresponder ao padr�o POSIX de express�es regulares.

%description -l pl
PCRE (Perl-Compatible Regular Expression) oznacza bibliotek� wyra�e�
regularnych kompatybilnych z perlowymi. Zawiera funkcje dopasowuj�ce
tekst do wyra�e� regularnych podobnych do tych znanych z Perla.
Zawiera tak�e bibliotek� kompatybiln� z POSIX.

%description -l pt_BR
A biblioteca PCRE � um conjunto de fun��es que implementam express�es
regulares utilizando-se da mesma sintaxe e sem�ntica do perl 5. Possui
sua pr�pria API nativa, bem como um conjuntos de fun��es wrapper para
corresponder ao padr�o POSIX de express�es regulares.

%package devel
Summary:	Perl-Compatible Regular Expression header files and development documentation
Summary(pl):	Pliki nag��wkowe i dokumentacja do bibliotek pcre
Summary(pt_BR):	Arquivos para desenvolvimento com pcre
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libpcre0-devel

%description devel
Perl-Compatible Regular Expression header files and development
documentation.

%description devel -l es
A biblioteca PCRE � um set de fun��es que implementam express�es
regulares utilizando-se da mesma sintaxe e sem�ntica do perl 5. Possui
sua pr�pria API nativa, bem como um set de fun��es wrapper para
corresponder ao padr�o POSIX de express�es regulares.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do bibliotek pcre.

%description devel -l pt_BR
A biblioteca PCRE � um conjunto de fun��es que implementam express�es
regulares utilizando-se da mesma sintaxe e sem�ntica do perl 5. Possui
sua pr�pria API nativa, bem como um conjunto de fun��es wrapper para
corresponder ao padr�o POSIX de express�es regulares.

%package static
Summary:	Perl-Compatible Regular Expression static libraries
Summary(pl):	Biblioteki statyczne pcre
Summary(pt_BR):	Arquivos para desenvolvimento est�tico com pcre
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Perl-Compatible Regular Expression library static libraries.

%description static -l es
A biblioteca PCRE � um set de fun��es que implementam express�es
regulares utilizando-se da mesma sintaxe e sem�ntica do perl 5. Possui
sua pr�pria API nativa, bem como um set de fun��es wrapper para
corresponder ao padr�o POSIX de express�es regulares.

%description static -l pl
Biblioteki statyczne pcre.

%description static -l pt_BR
A biblioteca PCRE � um conjunto de fun��es que implementam express�es
regulares utilizando-se da mesma sintaxe e sem�ntica do perl 5. Possui
sua pr�pria API nativa, bem como um conjunto de fun��es wrapper para
corresponder ao padr�o POSIX de express�es regulares.

%package cxx
Summary:	C++ wrapper to PCRE library
Summary(pl):	Interfejs C++ do biblioteki PCRE
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description cxx
C++ wrapper to PCRE library.

%description cxx -l pl
Interfejs C++ do biblioteki PCRE.

%package cxx-devel
Summary:	Header file for C++ wrapper to PCRE library
Summary(pl):	Plik nag��wkowy interfejsu C++ do biblioteki PCRE
Group:		Development/Libraries
Requires:	%{name}-cxx = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description cxx-devel
Header file for C++ wrapper to PCRE library.

%description cxx-devel -l pl
Plik nag��wkowy interfejsu C++ do biblioteki PCRE.

%package cxx-static
Summary:	Static version of pcrecpp library
Summary(pl):	Statyczna wersja biblioteki pcrecpp
Group:		Development/Libraries
Requires:	%{name}-cxx-devel = %{version}-%{release}

%description cxx-static
Static version of pcrecpp library.

%description cxx-static -l pl
Statyczna wersja biblioteki pcrecpp.

%package -n pcregrep
Summary:	Grep using Perl Compatible Regular Expressions
Summary(pl):	Grep u�ywaj�cy perlowych wyra�e� regularnych
Group:		Applications/Text
Obsoletes:	pgrep

%description -n pcregrep
pgrep is a grep workalike which uses perl-style regular expressions
instead of POSIX regular expressions.

%description -n pcregrep -l pl
pgrep jest programem dzia�aj�cym podobnie do grepa, ale u�ywaj�cych
perlowych wyra�e� regularnych, a nie posiksowych.

%package -n pcretest
Summary:	A program for testing Perl-comaptible regular expressions
Summary(pl):	Program do testowania kompatybilnych z perlem wyra�e� regualarnych
Group:		Applications/Text

%description -n pcretest
pcretest is a program which you can use to test regular expression

%description -n pcretest -l pl
pcretest jest programem za pomoc� mo�na sprawdzi� poprawno�� wyra�enia regularnego

%package doc-html
Summary:	Documentation for PCRE in HTML format
Summary(pl):	Dokumentacja dla PCRE w formacie HTML
Group:		Applications/Text

%description doc-html
Documentation for PCRE in HTML format.

%description doc-html -l pl
Dokumentacja dla PCRE w formacie HTML.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	CXXLDFLAGS="%{rpmldflags}" \
	%{!?with_static_libs:--enable-static=no} \
	--enable-utf8 \
	--enable-unicode-properties

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/libpcre.so.*.* $RPM_BUILD_ROOT/%{_lib}
mv -f $RPM_BUILD_ROOT%{_libdir}/libpcreposix.so.*.* $RPM_BUILD_ROOT/%{_lib}

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf /%{_lib}/`cd ../../%{_lib} ; echo libpcre.so.*.*.*` libpcre.so
ln -sf /%{_lib}/`cd ../../%{_lib} ; echo libpcreposix.so.*.*.*` libpcreposix.so

cd -
install pcredemo.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   cxx -p /sbin/ldconfig
%postun cxx -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS LICENCE
%attr(755,root,root) /%{_lib}/libpcre.so.*.*
%attr(755,root,root) /%{_lib}/libpcreposix.so.*.*

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
%{_mandir}/man3/*
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
