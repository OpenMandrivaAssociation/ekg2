%define		_snapshot 20071213

Summary:	Opensource multi-protocol instatnt messaging client
Name:		ekg2
Version:	1.0
Release:	5
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://ekg2.org/
Source0:	http://pl.ekg2.org/%{name}-%{_snapshot}.tar.bz2
Patch0:		ekg2-gcc43.patch
Patch1:		ekg2-gtk2-2.13.patch
Patch2:		ekg2-20071213-perl-install.patch
BuildRequires:	libaspell-devel
BuildRequires:	libexpat-devel
BuildRequires:	gettext-devel
BuildRequires:	libgnutls-devel >= 1.4.5
BuildRequires:	libgpm-devel
BuildRequires:	libgtk+2-devel
BuildRequires:	libgadu-devel
BuildRequires:	libgsm-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	libncursesw-devel >= 5.5
BuildRequires:	libopenssl-devel >= 0.9.8g
BuildRequires:	libpython-devel
BuildRequires:	perl-devel
BuildRequires:	libreadline-devel
BuildRequires:	libxosd-devel
BuildRequires:	libsqlite-devel
BuildRequires:	libsqlite3-devel
BuildRequires:	libgpgme-devel
BuildRequires:	chrpath
Conflicts:	ekg

%description
EKG2 is opensource IM client for Unix systems. 
Program supports plugins, which make possibility 
to support many diffrent protocols.

%package	devel
Summary:	Development files for ekg2
Group:		Development/C

%description	devel
Development files for ekg2.

%prep
%setup -qn %{name}-%{_snapshot}
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1
export AUTOMAKE="automake --foreign"
autoreconf -fi

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
mv -f README README-main
mv %{buildroot}%{_libdir}/ioctld %{buildroot}%{_bindir}

%ifarch x86_64
chrpath -d %{buildroot}%{_libdir}/ekg2/plugins/gpg.so %{buildroot}%{_libdir}/ekg2/plugins/gpg.so
chrpath -d %{buildroot}%{_libdir}/ekg2/plugins/jabber.so %{buildroot}%{_libdir}/ekg2/plugins/jabber.so
chrpath -d %{buildroot}%{_libdir}/ekg2/plugins/xosd.so %{buildroot}%{_libdir}/ekg2/plugins/xosd.so
%endif

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS* README-main docs/*
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{perl_vendorarch}/Ekg2
%{perl_vendorarch}/Ekg2.pm
%{perl_vendorarch}/auto/Ekg2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ekg2-config
%{_includedir}/ekg2/*
