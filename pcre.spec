# TODO
# - pcreposix subpackage?

# Conditional build:
%bcond_without	pcre16		# 16-bit character support
%bcond_without	pcre32		# 32-bit character support
%bcond_without	static_libs	# static libraries build
%bcond_without	tests		# don't perform "make check"

Summary:	Perl-Compatible Regular Expression library
Summary(pl.UTF-8):	Biblioteka perlowych wyrażeń regularnych
Summary(pt_BR.UTF-8):	Biblioteca de expressões regulares versão
Name:		pcre
Version:	8.44
Release:	1
License:	BSD (see LICENCE)
Group:		Libraries
Source0:	https://ftp.pcre.org/pub/pcre/%{name}-%{version}.tar.bz2
# Source0-md5:	cf7326204cc46c755b5b2608033d9d24
Patch0:		%{name}-pcreposix-glibc-conflict.patch
Patch1:		pcre-8.41-fix_stack_estimator.patch
URL:		http://www.pcre.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
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

%package -n pcre16
Summary:	PCRE library with 16-bit character support
Summary(pl.UTF-8):	Biblioteka PCRE z obsługą znaków 16-bitowych
Group:		Libraries

%description -n pcre16
PCRE (Perl compatible regular expressions) C library with 16-bit
character support.

%description -n pcre16 -l pl.UTF-8
Biblioteka C PCRE (perlowych wyrażeń regularnych) z obsługą znaków
16-bitowych.

%package -n pcre16-devel
Summary:	Development files for PCRE library with 16-bit character support
Summary(pl.UTF-8):	Pliki programistyczne biblioteki PCRE z obsługą znaków 16-bitowych
Group:		Development/Libraries
# base devel required for (common) headers and man page contents;
# pulling base pcre doesn't hurt, as it's already required by some basic packages
Requires:	%{name}-devel = %{version}-%{release}
Requires:	pcre16 = %{version}-%{release}

%description -n pcre16-devel
Development files for PCRE library with 16-bit character support.

%description -n pcre16-devel -l pl.UTF-8
Pliki programistyczne biblioteki PCRE z obsługą znaków 16-bitowych.

%package -n pcre16-static
Summary:	Static PCRE library with 16-bit character support
Summary(pl.UTF-8):	Biblioteka statyczna PCRE z obsługą znaków 16-bitowych
Group:		Development/Libraries
Requires:	pcre16-devel = %{version}-%{release}

%description -n pcre16-static
Static PCRE library with 16-bit character support.

%description -n pcre16-static -l pl.UTF-8
Biblioteka statyczna PCRE z obsługą znaków 16-bitowych.

%package -n pcre32
Summary:	PCRE library with 32-bit character support
Summary(pl.UTF-8):	Biblioteka PCRE z obsługą znaków 32-bitowych
Group:		Libraries

%description -n pcre32
PCRE (Perl compatible regular expressions) C library with 32-bit
character support.

%description -n pcre32 -l pl.UTF-8
Biblioteka C PCRE (perlowych wyrażeń regularnych) z obsługą znaków
32-bitowych.

%package -n pcre32-devel
Summary:	Development files for PCRE library with 32-bit character support
Summary(pl.UTF-8):	Pliki programistyczne biblioteki PCRE z obsługą znaków 32-bitowych
Group:		Development/Libraries
# base devel required for (common) headers and man page contents;
# pulling base pcre doesn't hurt, as it's already required by some basic packages
Requires:	%{name}-devel = %{version}-%{release}
Requires:	pcre32 = %{version}-%{release}

%description -n pcre32-devel
Development files for PCRE library with 32-bit character support.

%description -n pcre32-devel -l pl.UTF-8
Pliki programistyczne biblioteki PCRE z obsługą znaków 32-bitowych.

%package -n pcre32-static
Summary:	Static PCRE library with 32-bit character support
Summary(pl.UTF-8):	Biblioteka statyczna PCRE z obsługą znaków 32-bitowych
Group:		Development/Libraries
Requires:	pcre32-devel = %{version}-%{release}

%description -n pcre32-static
Static PCRE library with 32-bit character support.

%description -n pcre32-static -l pl.UTF-8
Biblioteka statyczna PCRE z obsługą znaków 32-bitowych.

%package -n pcregrep
Summary:	Grep using Perl Compatible Regular Expressions
Summary(pl.UTF-8):	Grep używający perlowych wyrażeń regularnych
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
Obsoletes:	pgrep

%description -n pcregrep
pgrep is a grep workalike which uses perl-style regular expressions
instead of POSIX regular expressions.

%description -n pcregrep -l pl.UTF-8
pgrep jest programem działającym podobnie do grepa, ale używających
perlowych wyrażeń regularnych, a nie posiksowych.

%package -n pcretest
Summary:	A program for testing Perl-compatible regular expressions
Summary(pl.UTF-8):	Program do testowania kompatybilnych z perlem wyrażeń regularnych
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
%{?with_pcre16:Requires:	pcre16 = %{version}-%{release}}
%{?with_pcre32:Requires:	pcre32 = %{version}-%{release}}

%description -n pcretest
pcretest is a program which you can use to test regular expression.

%description -n pcretest -l pl.UTF-8
pcretest jest programem, za pomocą którego można sprawdzić poprawność
wyrażenia regularnego.

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
%patch1 -p2

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CXXLDFLAGS="%{rpmldflags}" \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
%ifnarch x32
	--enable-jit \
%endif
	%{?with_pcre16:--enable-pcre16} \
	%{?with_pcre32:--enable-pcre32} \
	--enable-pcregrep-libz \
	--enable-pcregrep-libbz2 \
	--enable-pcretest-libreadline \
	--enable-unicode-properties \
	--enable-utf8

%{__make}

%if %{with tests}
# tests need big stack
ulimit -s 32768
%{__make} -j1 check
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

cp -p pcredemo.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf $RPM_BUILD_ROOT%{_docdir}/pcre

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   cxx -p /sbin/ldconfig
%postun cxx -p /sbin/ldconfig

%post	-n pcre16 -p /sbin/ldconfig
%postun	-n pcre16 -p /sbin/ldconfig

%post	-n pcre32 -p /sbin/ldconfig
%postun	-n pcre32 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENCE NEWS README
%attr(755,root,root) /%{_lib}/libpcre.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libpcre.so.1
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
%{_pkgconfigdir}/libpcreposix.pc
%{_mandir}/man1/pcre-config.1*
%{_mandir}/man3/pcre.3*
%{_mandir}/man3/pcre_*.3*
%{_mandir}/man3/pcreapi.3*
%{_mandir}/man3/pcrebuild.3*
%{_mandir}/man3/pcrecallout.3*
%{_mandir}/man3/pcrecompat.3*
%{_mandir}/man3/pcredemo.3*
%{_mandir}/man3/pcrejit.3*
%{_mandir}/man3/pcrelimits.3*
%{_mandir}/man3/pcrematching.3*
%{_mandir}/man3/pcrepartial.3*
%{_mandir}/man3/pcrepattern.3*
%{_mandir}/man3/pcreperform.3*
%{_mandir}/man3/pcreposix.3*
%{_mandir}/man3/pcreprecompile.3*
%{_mandir}/man3/pcresample.3*
%{_mandir}/man3/pcrestack.3*
%{_mandir}/man3/pcresyntax.3*
%{_mandir}/man3/pcreunicode.3*
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

%if %{with pcre16}
%files -n pcre16
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcre16.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcre16.so.0

%files -n pcre16-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcre16.so
%{_libdir}/libpcre16.la
%{_pkgconfigdir}/libpcre16.pc
%{_mandir}/man3/pcre16.3*
%{_mandir}/man3/pcre16_*.3*

%if %{with static_libs}
%files -n pcre16-static
%defattr(644,root,root,755)
%{_libdir}/libpcre16.a
%endif
%endif

%if %{with pcre32}
%files -n pcre32
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcre32.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcre32.so.0

%files -n pcre32-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcre32.so
%{_libdir}/libpcre32.la
%{_pkgconfigdir}/libpcre32.pc
%{_mandir}/man3/pcre32.3*
%{_mandir}/man3/pcre32_*.3*

%if %{with static_libs}
%files -n pcre32-static
%defattr(644,root,root,755)
%{_libdir}/libpcre32.a
%endif
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
