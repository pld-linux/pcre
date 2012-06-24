Summary:	Perl-Compatible Regular Expression library
Summary(pl):	Biblioteka perlowych wyra�e� regularnych
Summary(pt_BR):	Biblioteca de express�es regulares vers�o
Name:		pcre
Version:	3.9
Release:	2
License:	GPL
Vendor:		Philip Hazel <ph10@cam.ac.uk>
Group:		Libraries
Source0:	ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libpcre0

%description
PCRE stands for the Perl Compatible Regular Expression library. It
contains routines to match text against regular expressions similar to
perl's. It also contains a POSIX compatibility library.

%description -l es
A biblioteca PCRE � um set de fun��es que implementam express�es
regulares utilizando-se da mesma sintaxe e sem�ntica do perl 5. Possui
sua pr�pria API nativa, bem como um set de fun��es wrapper para
corresponder ao padr�o POSIX de express�es regulares.

%description -l pl
PCRE (Perl-Compatible Regular Expression) oznacza bibliotek� wyra�e�
regularnych kompatybilnych z perlowymi. Zawiera funkcje dopasowuj�ce
tekst do wyra�e� regularnych podobnych do tych znanych z perla.
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
Requires:	%{name} = %{version}
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
Pliki nag��wkowe i dokumentacja do blibliotek pcre.

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
Requires:	%{name}-devel = %{version}

%description static
Perl-Compatible Regular Expression library staic libraris.

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

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
