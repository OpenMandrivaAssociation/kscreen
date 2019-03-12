%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Display Management software
Name:		kscreen
Version:	5.15.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/libs/kscreen
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/kscreen-%{version}.tar.xz
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(KF5Screen)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	pkgconfig(kscreen2)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	cmake(ECM)
%rename kscreen5

%description
KCM and KDED modules for managing displays in KDE.

%files -f kscreen.lang
%{_bindir}/kscreen-console
%{_libdir}/qt5/plugins/*.so
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_datadir}/icons/*/*/*
%{_datadir}/kcm_kscreen
%{_datadir}/kded_kscreen
%{_datadir}/kservices5/*.desktop
%{_sysconfdir}/xdg/kscreen.categories
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_kscreen.so
%{_datadir}/metainfo/org.kde.kscreen.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.kscreen

#------------------------------------------------------------------------------

%prep
%setup -qn kscreen-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kscreen --all-name --with-html
