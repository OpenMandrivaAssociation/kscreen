%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	KDE Display Management software
Name:		kscreen
Version:	6.4.4
Release:	%{?git:0.%{git}.}2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/libs/kscreen
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kscreen/-/archive/%{gitbranch}/kscreen-%{gitbranchd}.tar.bz2#/kscreen-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/kscreen-%{version}.tar.xz
%endif
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(PlasmaQuick) >= 5.90.0
BuildRequires:	cmake(KF6Screen)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(Qt6Sensors)
BuildRequires:	cmake(LayerShellQt)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:	pkgconfig(xcb-atom)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	cmake(ECM)
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed 2025-05-01 after 6.0
%rename plasma6-kscreen

%description
KCM and KDED modules for managing displays in KDE.

%files -f %{name}.lang
%{_bindir}/kscreen-console
%{_qtdir}/plugins/kf6/kded/*.so
%{_datadir}/qlogging-categories6/kscreen.categories
%{_prefix}/lib/systemd/user/plasma-kscreen-osd.service
%{_libdir}/libexec/kscreen_osd_service
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_kscreen.so
%{_datadir}/applications/kcm_kscreen.desktop
%{_datadir}/dbus-1/services/org.kde.kscreen.osdService.service
%{_qtdir}/plugins/plasma/applets/org.kde.kscreen.so
%{_datadir}/kglobalaccel/org.kde.kscreen.desktop
%{_bindir}/hdrcalibrator
%{_datadir}/kscreen
