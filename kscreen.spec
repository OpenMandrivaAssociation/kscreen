Summary:	KDE Display Management software
Name:		kscreen
Version:	1.0.2.1
Release:	5
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/libs/kscreen
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
# From upstream
Patch0:		kscreen-1.0.2-fix-typo.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(kscreen)
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
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} kcm_displayconfiguration %{name}.lang

%find_lang plasma_applet_org.kde.plasma.kscreen

