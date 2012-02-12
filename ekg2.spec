%define		_snapshot 20120212

Summary:	Opensource multi-protocol instatnt messaging client
Name:		ekg2
Version:	1.0
Release:	7.%{_snapshot}.1
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://ekg2.org/
Source0:	http://pl.ekg2.org/%{name}-%{_snapshot}.tar.bz2
BuildRequires:	aspell-devel
BuildRequires:	expat-devel
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	gpm-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgadu)
BuildRequires:	libgsm-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)
BuildRequires:	perl-devel
BuildRequires:	readline-devel
BuildRequires:	xosd-devel
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	gpgme-devel
Conflicts:	ekg
Conflicts:	%{name}-devel

%description
EKG2 is opensource IM client for Unix systems. 
Program supports plugins, which make possibility 
to support many diffrent protocols.

%prep
%setup -qn %{name}-%{_snapshot}
export AUTOMAKE="automake --foreign"
autoreconf -fi
sed -i "s/);/,\n\t'INSTALLDIRS' => 'vendor');/" plugins/perl/common/Makefile.PL
sed -i "s/);/,\n\t'INSTALLDIRS' => 'vendor');/" plugins/perl/irc/Makefile.PL

%build
%configure2_5x \
    --with-aspell \
    --with-expat \
    --with-libgnutls \
    --with-libgadu \
    --with-libgsm \
    --with-python \
    --without-readline \
    --with-sqlite \
    --with-sqlite3 \
    --with-gtk \
    --enable-unicode \
    --disable-rpath
					    
# /usr/bin/gpgme-config --cflags returns empty string, but build fails:
# error: GPGME was compiled with _FILE_OFFSET_BITS = 64
%make GPGME_CFLAGS="-D_FILE_OFFSET_BITS=64"
					    
%install
install -d %{buildroot}%{_datadir}/%{name}/scripts
install -d  %{buildroot}%{perl_vendorlib}/i386-linux

%makeinstall_std

rm -rf docs/{CVS,.cvsignore,Makefile*}
rm -rf docs/ekg2book/{CVS,.cvsignore,Makefile*}
rm -rf docs/ekg2book/design/CVS
rm -rf docs/ekg2book-en/{CVS,.cvsignore,Makefile*}
rm -rf docs/ekg2book-en/design/CVS
rm -f %{buildroot}%{_libdir}/%{name}/plugins/*.la

%find_lang %{name}

%files -f %{name}.lang
%doc docs/*
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{perl_vendorarch}/Ekg2
%{perl_vendorarch}/Ekg2.pm
%{perl_vendorarch}/auto/Ekg2
