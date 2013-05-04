Name:		kscreen
Summary:	KDE Display Management software
Version:	0.0.92
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://projects.kde.org/projects/playground/libs/kscreen
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(kscreen) = %{version}
BuildRequires:	pkgconfig(QJson)
Requires:	kdebase4-runtime
Requires:	libkscreen

%description
KCM and KDED modules for managing displays in KDE.

%files -f %{name}.lang
%{_kde_bindir}/kscreen-console
%{_kde_libdir}/kde4/kcm_kscreen.so
%{_kde_libdir}/kde4/kded_kscreen.so
%{_kde_datadir}/apps/kcm_kscreen
%{_kde_datadir}/kde4/services/kcm_kscreen.desktop
%{_kde_datadir}/kde4/services/kded/kscreen.desktop
%{_kde_iconsdir}/hicolor/*/actions/kdocumentinfo.*

#------------------------------------------------------------------------------

%package -n plasma-applet-kscreen
Summary:	Plasma applet for quick display configuration
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description -n plasma-applet-kscreen
Plasma applet for quick display configuration.

%files -n plasma-applet-kscreen -f plasma_applet_org.kde.plasma.kscreen.lang
%{_kde_libdir}/kde4/plasma_applet_kscreen.so
%{_kde_appsdir}/plasma/packages/org.kde.plasma.kscreen.qml
%{_kde_services}/plasma-applet-kscreen.desktop
%{_kde_services}/plasma-applet-kscreen-qml.desktop

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} kcm_displayconfiguration %{name}.lang

%find_lang plasma_applet_org.kde.plasma.kscreen

