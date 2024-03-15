#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		marble
Summary:	marble
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	61d6f7fe2631a7a2081044ee33059011
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5SerialPort-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-krunner-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	kf5-plasma-framework-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shapelib-devel
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
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

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

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
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DMARBLE_PRI_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/lt
%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/marble
%attr(755,root,root) %{_bindir}/marble-qt
%{_libdir}/libastro.so.*.*.*
%ghost %{_libdir}/libastro.so.1
%{_libdir}/libmarbledeclarative.so
%ghost %{_libdir}/libmarblewidget-qt5.so.28
%{_libdir}/libmarblewidget-qt5.so.*.*.*
%{_libdir}/marble

%dir %{_libdir}/plugins
%dir %{_libdir}/plugins/designer

%{_libdir}/qt5/plugins/libmarble_part.so
%{_libdir}/qt5/qml/org/kde/marble
%attr(755,root,root) %{_libdir}/plugins/designer/LatLonEditPlugin.so
%attr(755,root,root) %{_libdir}/plugins/designer/MarbleNavigatorPlugin.so
%attr(755,root,root) %{_libdir}/plugins/designer/MarbleWidgetPlugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/marblethumbnail.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/plasma_runner_marble.so

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/marble_geo.desktop
%{_desktopdir}/marble_geojson.desktop
%{_desktopdir}/marble_gpx.desktop
%{_desktopdir}/marble_kml.desktop
%{_desktopdir}/marble_kmz.desktop
%{_desktopdir}/marble_shp.desktop
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
%{_datadir}/kservices5/marble_thumbnail_shp.desktop
%{_datadir}/kxmlgui5/marble
%{_datadir}/marble
%{_datadir}/metainfo/org.kde.marble.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.worldclock.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.worldmap.appdata.xml
%{_datadir}/mime/packages/geo.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock
%{_datadir}/plasma/wallpapers/org.kde.plasma.worldmap
%dir %{_docdir}/HTML/{ca,de,en,es,et,fr,gl,it,lt,nl,pt,pt_BR,ru,sv,uk}/marble
%{_docdir}/HTML/*/marble/index.cache.bz2
%{_docdir}/HTML/*/marble/index.docbook
%{_docdir}/HTML/*/marble/*.png
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.worldclock.desktop
%{_datadir}/kservices5/plasma-wallpaper-org.kde.plasma.worldmap.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/astro
%{_includedir}/marble
%{_libdir}/cmake/Astro
%{_libdir}/cmake/Marble
%{_libdir}/libastro.so
%{_libdir}/libmarblewidget-qt5.so
%{_libdir}/qt5/mkspecs/modules/qt_Marble.pri
