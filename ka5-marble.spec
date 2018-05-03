%define		kdeappsver	18.04.0
%define		qtver		5.3.2
%define		kaname		marble
Summary:	marble
Name:		ka5-%{kaname}
Version:	18.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	571cb31746a0eaa4aa9c9b0363b12d25
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
marble

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.


%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig


%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/marble.knsrc
%attr(755,root,root) %{_bindir}/marble
%attr(755,root,root) %{_bindir}/marble-qt
%{_libdir}/libastro.so.0.*.*
%ghost %{_libdir}/libastro.so.1
%{_libdir}/libmarbledeclarative.so
%{_libdir}/libmarblewidget-qt5.so.0.*.*
%ghost %{_libdir}/libmarblewidget-qt5.so.28
%{_libdir}/marble

%dir %{_libdir}/plugins
%dir %{_libdir}/plugins/designer

%{_libdir}/plugins/designer/libLatLonEditPlugin.so
%{_libdir}/plugins/designer/libMarbleNavigatorPlugin.so
%{_libdir}/plugins/designer/libMarbleWidgetPlugin.so
%{_libdir}/qt5/plugins/libmarble_part.so
%{_libdir}/qt5/plugins/libmarblethumbnail.so
%{_libdir}/qt5/plugins/plasma_runner_marble.so
%{_libdir}/qt5/qml/org/kde/marble
%{_desktopdir}/marble_geo.desktop
%{_desktopdir}/marble_geojson.desktop
%{_desktopdir}/marble_gpx.desktop
%{_desktopdir}/marble_kml.desktop
%{_desktopdir}/marble_kmz.desktop
%{_desktopdir}/marble_worldwind.desktop
%{_desktopdir}/org.kde.marble-qt.desktop
%{_desktopdir}/org.kde.marble.desktop
%{_datadir}/config.kcfg/marble.kcfg
%{_iconsdir}/hicolor/128x128/apps/marble.png
%{_iconsdir}/hicolor/16x16/apps/marble.png
%{_iconsdir}/hicolor/22x22/apps/marble.png
%{_iconsdir}/hicolor/32x32/apps/marble.png
%{_iconsdir}/hicolor/48x48/apps/marble.png
%{_iconsdir}/hicolor/64x64/apps/marble.png
%{_datadir}/kservices5/marble_part.desktop
%{_datadir}/kservices5/marble_thumbnail_geojson.desktop
%{_datadir}/kservices5/marble_thumbnail_gpx.desktop
%{_datadir}/kservices5/marble_thumbnail_kml.desktop
%{_datadir}/kservices5/marble_thumbnail_kmz.desktop
%{_datadir}/kservices5/marble_thumbnail_osm.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.worldclock.desktop
%{_datadir}/kservices5/plasma-runner-marble.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.plasma.worldmap.desktop
%{_datadir}/kxmlgui5/marble
%{_datadir}/marble
%{_datadir}/metainfo/org.kde.marble.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.worldclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.worldmap.appdata.xml
%{_datadir}/mime/packages/geo.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock
%{_datadir}/plasma/wallpapers/org.kde.plasma.worldmap

%files devel
%defattr(644,root,root,755)
%{_includedir}/astro
%{_includedir}/marble
%{_libdir}/cmake/Astro
%{_libdir}/cmake/Marble
%{_libdir}/libastro.so
%{_libdir}/libmarblewidget-qt5.so

#%dir %{_prefix}/mkspecs
#%dir %{_prefix}/mkspecs/modules
#%{_prefix}/mkspecs/modules/qt_Marble.pri
