Summary:	Perl-Compatible Regular Expression library
Summary(pl):	Biblioteka perlowych wyraøeÒ regularnych
Name:		pcre
Version:	3.7
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Vendor:		Philip Hazel <ph10@cam.ac.uk>
Source0:	ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCRE stands for the Perl Compatible Regular Expression library. It
contains routines to match text against regular expressions similar to
perl's. It also contains a POSIX compatibility library.

%description -l pl
PCRE (Perl-Compatible Regular Expression) oznacza bibliotekÍ wyraøeÒ
regularnych kompatybilnych z perlowymi. Zawiera funkcje dopasowuj±ce
tekst do wyraøeÒ regularnych podobnych do tych znanych z perla.
Zawiera takøe bibliotekÍ kompatybiln± z POSIX.

%package devel
Summary:	Perl-Compatible Regular Expression header files and development documentation
Summary(pl):	Pliki nag≥Ûwkowe i dokumentacja do bibliotek pcre
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Perl-Compatible Regular Expression header files and development
documentation.

%description -l pl devel
Pliki nag≥Ûwkowe i dokumentacja do blibliotek pcre.

%package static
Summary:	Perl-Compatible Regular Expression static libraries
Summary(pl):	Biblioteki statyczne pcre
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Perl-Compatible Regular Expression library staic libraris.

%description -l pl static
Biblioteki statyczne pcre.

%package -n pcregrep
Summary:	Grep using Perl Compatible Regular Expressions
Summary(pl):	Grep uøywaj±cy perlowych wyraøeÒ regularnych
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Obsoletes:	pgrep

%description -n pcregrep
pgrep is a grep workalike which uses perl-style regular expressions
instead of POSIX regular expressions.

%description -n pcregrep -l pl
pgrep jest programem dzia≥aj±cym podobnie do grepa, ale uøywaj±cych
perlowych wyraøeÒ regularnych, a nie posiksowych.

%prep
%setup -q

%build
aclocal
autoconf
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
