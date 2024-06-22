#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	qtwebengine	# Qt WebEngine widgets

%ifarch x32
%undefine	with_qt5webengine
%endif
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		marble
Summary:	Marble - virtual globe and world atlas
Summary(pl.UTF-8):	Marble - wirtualny globus i atlas świata
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	61d6f7fe2631a7a2081044ee33059011
URL:		https://kde.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Positioning-devel >= %{qtver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5SerialPort-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5UiTools-devel >= %{qtver}
BuildRequires:	Qt5WebChannel-devel >= %{qtver}
%{?with_qtwebengine:BuildRequires:	Qt5WebEngine-devel >= %{qtver}}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.20
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gettext-tools
BuildRequires:	gpsd-devel
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
BuildRequires:	libwlocate-devel
BuildRequires:	ninja
BuildRequires:	perl-base
BuildRequires:	phonon-qt5-devel
BuildRequires:	pkgconfig
BuildRequires:	protobuf-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shapelib-devel
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
%{!?with_qtwebengine:BuildConflicts:	Qt5WebEngine-devel}
Requires:	%{name}-data = %{version}-%{release}
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5Gui >= %{qtver}
Requires:	Qt5Network >= %{qtver}
Requires:	Qt5Positioning >= %{qtver}
Requires:	Qt5PrintSupport >= %{qtver}
Requires:	Qt5Qml >= %{qtver}
Requires:	Qt5Quick >= %{qtver}
Requires:	Qt5SerialPort >= %{qtver}
Requires:	Qt5Sql >= %{qtver}
Requires:	Qt5Svg >= %{qtver}
Requires:	Qt5WebChannel >= %{qtver}
%{?with_qtwebengine:Requires:	Qt5WebEngine >= %{qtver}}
Requires:	Qt5Widgets >= %{qtver}
Requires:	Qt5Xml >= %{qtver}
Requires:	kf5-kcoreaddons >= %{kframever}
Requires:	kf5-kcrash >= %{kframever}
Requires:	kf5-ki18n >= %{kframever}
Requires:	kf5-kio >= %{kframever}
Requires:	kf5-kparts >= %{kframever}
Requires:	kf5-krunner >= %{kframever}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Marble is a Virtual Globe and World Atlas that you can use to learn
more about the Earth.

Features:
- You can pan and zoom around and you can look up places and roads
- A mouse click on a place label will provide the respective Wikipedia
  article
- You can measure distances between locations
- It offers different thematic maps: a classroom-style topographic
  map, a satellite view, street map, Earth at night and temperature
  and precipitation maps. All maps include a custom map key, so it can
  also be used as an educational tool for use in classrooms
- For educational purposes you can also change date and time and watch
  how the starry sky and the twilight zone on the map change
- Supports multiple projections: choose between a Flat Map ("Plate
  carré"), Mercator or the Globe
- Promotes the usage of free maps

%description -l pl.UTF-8
Marble to wirtualny globus i atlas świata, pozwalający uczyć się
więcej o Ziemi.

Cechy:
- można przesuwać i powiększać, szukać miejsc i dróg
- kliknięcie na etykiecie miejsca daje odpowiedni artykuł z Wikipedii
- można mierzyć odległości między położeniami
- różne mapy tematyczne: mapa topograficzna w stylu szkolnym, widok
  satelitarny, mapa ulic, Ziemia nocą, mapy temperatur i opadów;
  wszystkie mapy zawierają własny klucz, więc mogą służyć jako
  narzędzie edukacyjne
- w celach edukacyjnych można zmieniać datę oraz czas i obserwować,
  jak zmienia się gwieździste niebo i strefa zmierzchu
- obsługa wielu rzutów: wybór między płaską mapą, odwzorowaniem
  Mercatora i globusem
- promowanie używania map wolnodostępnych

%package data
Summary:	Data files for Marble
Summary(pl.UTF-8):	Dane dla Marble
Group:		X11/Applications
BuildArch:	noarch

%description data
Data files for Marble.

%description data -l pl.UTF-8
Dane dla Marble.

%package devel
Summary:	Header files for Marble development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających Marble
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_qtwebengine:Requires:	Qt5WebEngine-devel >= %{qtver}}
Requires:	Qt5Widgets-devel >= %{qtver}
Requires:	Qt5Xml-devel >= %{qtver}

%description devel
Header files for Marble development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających Marble.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_MARBLE_TESTS=OFF} \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DMARBLE_PRI_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/marble
%attr(755,root,root) %{_bindir}/marble-qt
%attr(755,root,root) %{_libdir}/libastro.so.*.*.*
%ghost %{_libdir}/libastro.so.1
%attr(755,root,root) %{_libdir}/libmarbledeclarative.so
%attr(755,root,root) %{_libdir}/libmarblewidget-qt5.so.*.*.*
%ghost %{_libdir}/libmarblewidget-qt5.so.28
%{_libdir}/marble

%dir %{_libdir}/plugins
%dir %{_libdir}/plugins/designer
%attr(755,root,root) %{_libdir}/plugins/designer/LatLonEditPlugin.so
%attr(755,root,root) %{_libdir}/plugins/designer/MarbleNavigatorPlugin.so
%attr(755,root,root) %{_libdir}/plugins/designer/MarbleWidgetPlugin.so

%attr(755,root,root) %{_libdir}/qt5/plugins/libmarble_part.so
%attr(755,root,root) %{_libdir}/qt5/plugins/marblethumbnail.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/plasma_runner_marble.so
%{_libdir}/qt5/qml/org/kde/marble

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
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.worldclock.desktop
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
%{_libdir}/libastro.so
%{_libdir}/libmarblewidget-qt5.so
%{_includedir}/astro
%{_includedir}/marble
%{_libdir}/cmake/Astro
%{_libdir}/cmake/Marble
%{_libdir}/qt5/mkspecs/modules/qt_Marble.pri
