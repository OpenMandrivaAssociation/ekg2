%define		_snapshot 20120212

Summary:	Opensource multi-protocol instatnt messaging client
Name:		ekg2
Version:	1.0
Release:	7.%{_snapshot}.1
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		https://ekg2.org/
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


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0-7.20120212.1
+ Revision: 773530
- new snapshot
- devel package dropped
- clean out some misc junk...
- use pkgconfig() dependencies
- svn commit -m mass rebuild of perl extension against perl 5.14.2
- cleanup

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0-0.20071213.5mdv2011.0
+ Revision: 555669
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 1.0-0.20071213.4mdv2010.1
+ Revision: 537456
- rebuild

* Thu Oct 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-0.20071213.3mdv2010.0
+ Revision: 456005
- fix perl modules installation
- %%files section cleanup
- fix build, using fedora patches

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Rebuild for new perl

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.20071213.1mdv2008.1
+ Revision: 120031
- new snapshot
- drop patch 0

* Fri Dec 14 2007 Thierry Vignaud <tv@mandriva.org> 1.0-0.20070226.5mdv2008.1
+ Revision: 119946
- simplify file list
- there's no more *.a files on x86_64
- rebuild (missing devel package on ia32)
- rebuild because static devel package didn't reach ia32 mirrors

* Wed Jun 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.20070226.2mdv2008.0
+ Revision: 38574
- rebuild against libgadu


* Tue Feb 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.20070226.1mdv2007.0
+ Revision: 126626
- new snapshot
- remove duplicated provides/requires

* Wed Feb 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.20070220.1mdv2007.1
+ Revision: 123635
- update to latest snapshot

* Mon Jan 29 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.20070128.2mdv2007.1
+ Revision: 115182
- bump release tag
- fix buildrequires
- new snapshot
- fix provides
- remove rpatch from gpg.so
- fix buildrequires
- new snapshot
- fixed path for perl modules
- remove rpath for gpg.so
- regenerate patch 0

* Mon Jan 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.20070107.3mdv2007.1
+ Revision: 105428
- new snapshot, with new features

* Sun Dec 24 2006 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.20061223.3mdv2007.1
+ Revision: 101968
- new snapshot

* Fri Dec 08 2006 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.20061203.3mdv2007.1
+ Revision: 92157
- bump release tag
- fixed path for ioctld
- Bump release tag
- Fix build on x86_64
- New snapshot
- Add missing build requires
- import ekg2
- Import ekg2

* Sun Dec 03 2006 TPG
- initial package for mdv

