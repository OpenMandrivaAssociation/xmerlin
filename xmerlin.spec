%define name    xmerlin
%define version 0.9b
%define tver    0.9
%define release %mkrel 12

Summary: Character recognition engine for X11 devices
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{tver}_public.tar.bz2
Patch0: xmerlin-0.9b-gcc3_4.patch.bz2
URL: http://www.hellkvist.org/software/index.php3#XMerlin
License: GPL
Group: System/X11
Buildrequires: X11-devel
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

