%define name    xmerlin
%define version 0.9b
%define tver    0.9
%define release %mkrel 13

Summary: Character recognition engine for X11 devices
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{tver}_public.tar.bz2
Patch0: xmerlin-0.9b-gcc3_4.patch
URL: http://www.hellkvist.org/software/index.php3#XMerlin
License: GPL
Group: System/X11
Buildrequires: libx11-devel
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
XMerlin is a simple character recognition engine for X11-based Web pads
and such devices where a regular keyboard is not an option. You write your
characters in a window, and after recognition the character is sent to the
window in focus, which could we an editor, web browser, or any other
window/widget that accepts SendEvents.

%prep

%setup -q -n %{name}-%{tver}_public
%patch0 -p1 -b .gcc3_4

%build
# modify Makefile
perl -pi -e "s|/usr/local/share/merlin|\\$\(INSTALL_PREFIX)/share/merlin||g;" Makefile
perl -pi -e "s|/usr/X11R6/bin|\\$\(INSTALL_PREFIX)/bin||g;" Makefile
perl -pi -e "s|-O2 -Wall |\\$\(OTHER_CFLAGS) -O2 -Wall ||g;" Makefile

# build
make OTHER_CFLAGS="$RPM_OPT_FLAGS" INSTALL_PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/{bin,share/merlin}/
make INSTALL_PREFIX=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/* COPYING INSTALL WHATISNEW
%{_bindir}/*
%dir %{_datadir}/merlin/
%{_datadir}/merlin/*



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 0.9b-13mdv2011.0
+ Revision: 634904
- bunzip2 the patch
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.9b-12mdv2010.0
+ Revision: 435146
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.9b-11mdv2009.0
+ Revision: 262459
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.9b-10mdv2009.0
+ Revision: 257133
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.9b-8mdv2008.1
+ Revision: 140963
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import xmerlin


* Thu Aug 24 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.9b-8mdv2007.0
- Fix group
- Use mkrel 
- Fix some rpmlint errors

* Sat Oct 30 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.9b-7mdk
- fix build with gcc 3.4

* Tue May 06 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9b-6mdk
- buildrequires

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9b-5mdk
- rebuild

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.9b-4mdk
- rebuild

* Fri Aug 24 2001 Etienne Faure <etienne@mandrakesoft.com> 0.9b-3mdk
- rebuild

* Thu Feb 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.9b-2mdk
- rebuild

* Fri Sep 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.9b-1mdk
- used srpm from rufus t firefly :
        Thu Sep 28 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com>
            v0.9b (initial packaging)
