%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	KDE Display Management software
Name:		kscreen
Version:	6.8.1
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/libs/kscreen
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kscreen/-/archive/%{gitbranch}/kscreen-%{gitbranchd}.tar.bz2#/kscreen-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/kscreen-%{version}.tar.xz
%endif
# kwin_x11 does not apply saved layouts. This helper does that for the X11
# session only and exits immediately on any other platform.
Patch0:		kscreen-6.8.0-x11-hotplug.patch
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
BuildRequires:	cmake(KF6ItemModels)
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
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(xcb-atom)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	cmake(ECM)
BuildRequires:	qml(org.kde.kitemmodels)
BuildRequires:	qml(org.kde.plasma.plasma5support)
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed 2025-05-01 after 6.0
%rename plasma6-kscreen

%description
KCM and an X11 session helper for managing displays in KDE.

%install -a
install -d %{buildroot}%{_prefix}/lib/systemd/user/plasma-workspace-x11.target.wants
ln -s ../plasma-kscreen-x11.service %{buildroot}%{_prefix}/lib/systemd/user/plasma-workspace-x11.target.wants/plasma-kscreen-x11.service

%files -f %{name}.lang
%{_bindir}/kscreen-console
%{_bindir}/kscreenctl
%{_datadir}/fish/vendor_completions.d/kscreenctl.fish
%{_datadir}/zsh/site-functions/_kscreenctl
%{_datadir}/qlogging-categories6/kscreen.categories
%{_prefix}/lib/systemd/user/plasma-kscreen-osd.service
%{_prefix}/lib/systemd/user/plasma-kscreen-x11.service
%{_prefix}/lib/systemd/user/plasma-workspace-x11.target.wants/plasma-kscreen-x11.service
%{_libdir}/libexec/kscreen_osd_service
%{_libdir}/libexec/kscreen_x11_hotplug
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_kscreen.so
%{_datadir}/applications/kcm_kscreen.desktop
%{_datadir}/dbus-1/services/org.kde.kscreen.osdService.service
%{_qtdir}/plugins/plasma/applets/org.kde.kscreen.so
%{_datadir}/kglobalaccel/org.kde.kscreen.desktop
%{_bindir}/hdrcalibrator
