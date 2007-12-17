%define		_snapshot 20071213

Summary:	Opensource multi-protocol instatnt messaging client
Name:		ekg2
Version:	1.0
Release:	%mkrel 0.%{_snapshot}.1
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://ekg2.org/
Source0:	http://pl.ekg2.org/%{name}-%{_snapshot}.tar.bz2
BuildRequires:	libaspell-devel
BuildRequires:	libexpat-devel
BuildRequires:	gettext-devel
BuildRequires:	libgnutls-devel		>= 1.4.5
BuildRequires:	libgpm-devel
BuildRequires:	libgtk+2-devel
BuildRequires:	libgadu-devel
BuildRequires:	libgsm-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	libncursesw-devel	>= 5.5
BuildRequires:	libopenssl-devel	>= 0.9.8g
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

%package devel
Summary:	Development files for ekg2
Group:		Development/C

%description devel
Development files for ekg2.

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ekg2-config
%{_includedir}/ekg2/*

%prep
%setup -qn %{name}-%{_snapshot}

%build

%configure2_5x \
    --with-aspell \
    --with-expat \
    --with-libgnutls \
    --with-libgadu \
    --with-libgsm \
    --with-python \
    --without-readline \
    --with-xosd \
    --with-sqlite \
    --with-sqlite3 \
    --with-gtk \
    --enable-unicode \
    --disable-rpath
					    
%make
					    
%install
rm -rf %{buildroot}
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

%ifarch i586
mv -f %{buildroot}%{perl_sitelib}/i386-linux/* %{buildroot}%{perl_vendorlib}/i386-linux
rm -rf %{buildroot}%{perl_sitelib}
%endif

%ifarch x86_64
mv -f %{buildroot}%{perl_sitelib}/x86_64-linux/* %{buildroot}%{perl_vendorlib}/i386-linux
rm -rf %{buildroot}%{perl_sitelib}

chrpath -d %{buildroot}%{_libdir}/ekg2/plugins/gpg.so %{buildroot}%{_libdir}/ekg2/plugins/gpg.so
chrpath -d %{buildroot}%{_libdir}/ekg2/plugins/jabber.so %{buildroot}%{_libdir}/ekg2/plugins/jabber.so
chrpath -d %{buildroot}%{_libdir}/ekg2/plugins/xosd.so %{buildroot}%{_libdir}/ekg2/plugins/xosd.so
%endif

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS* README-main docs/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%dir %{perl_vendorlib}/i386-linux/Ekg2
%dir %{perl_vendorlib}/i386-linux/auto/Ekg2
%{perl_vendorlib}/i386-linux/Ekg2.pm
%{perl_vendorlib}/i386-linux/Ekg2/Irc.pm
%attr(755,root,root) %{perl_vendorlib}/i386-linux/auto/Ekg2/Ekg2.so
%attr(755,root,root) %{perl_vendorlib}/i386-linux/auto/Ekg2/Irc/Irc.so
%{_datadir}/%{name}/*.txt
%{_datadir}/%{name}/plugins/*
%dir %{_datadir}/%{name}/scripts
%{_datadir}/%{name}/scripts/*.pl
%attr(755,root,root) %{_datadir}/%{name}/scripts/notify-bubble.py
%dir %{_datadir}/%{name}/themes
%{_datadir}/%{name}/themes/*
