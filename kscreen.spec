Name:		kscreen
Summary:	KDE Display Management software
Version:	0.0.71
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://projects.kde.org/projects/playground/libs/kscreen
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(kscreen)
BuildRequires:	pkgconfig(QJson)
Requires:	kdebase4-runtime
Requires:	libkscreen

%description
KCM and KDED modules for managing displays in KDE.

%files
%{_kde_bindir}/kscreen-console
%{_kde_libdir}/kde4/kcm_kscreen.so
%{_kde_libdir}/kde4/kded_kscreen.so
%{_kde_datadir}/apps/kcm_kscreen
%{_kde_datadir}/kde4/services/kcm_kscreen.desktop
%{_kde_datadir}/kde4/services/kded/kscreen.desktop

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

