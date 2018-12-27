%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		marble
Summary:	marble
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	eded2e2c97bec61e605e65e463d0b66d
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Marble is a Virtual Globe and World Atlas that you can use to learn
more about the Earth.

Features

• You can pan and zoom around and you can look up places and roads • A
mouse click on a place label will provide the respective Wikipedia
article • You can measure distances between locations • It offers
different thematic maps: a classroom-style topographic map, a
satellite view, street map, Earth at night and temperature and
precipitation maps. All maps include a custom map key, so it can also
be used as an educational tool for use in classrooms • For educational
purposes you can also change date and time and watch how the starry
sky and the twilight zone on the map change • Supports multiple
projections: choose between a Flat Map ("Plate carré"), Mercator or
the Globe • Promotes the usage of free maps

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
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
#%%{_datadir}/metainfo/org.kde.plasma.worldmap.appdata.xml
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
