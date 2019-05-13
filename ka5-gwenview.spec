%define		kdeappsver	19.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		gwenview
Summary:	Simple image viewer
Name:		ka5-%{kaname}
Version:	19.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ab67e12f3e9cc851464741bcf8a0cd74
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	exiv2-devel
BuildRequires:	gettext-tools
BuildRequires:	ka5-libkdcraw-devel >= %{kdeappsver}
BuildRequires:	ka5-libkipi-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kactivities-devel >= %{kframever}
BuildRequires:	kf5-kdelibs4support-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	lcms2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gwenview is an image viewer for KDE.

It features a folder tree window and a file list window to provide
easy navigation in your file hierarchy. Image loading is done by the
Qt library, so it supports all image formats your Qt installation
supports.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gwenview
%attr(755,root,root) %{_libdir}/libgwenviewlib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwenviewlib.so.5
%attr(755,root,root)        %{_libdir}/qt5/plugins/gvpart.so
%{_desktopdir}/org.kde.gwenview.desktop
%{_datadir}/gwenview
%{_iconsdir}/hicolor/*/actions/document-share.png
%{_iconsdir}/hicolor/*/apps/gwenview.png
%{_datadir}/kservices5/ServiceMenus/slideshow.desktop
%{_datadir}/kservices5/gvpart.desktop
%dir %{_datadir}/kxmlgui5/gvpart
%{_datadir}/kxmlgui5/gvpart/gvpart.rc
#%%dir %{_datadir}/kxmlgui5/gwenview
#%%{_datadir}/kxmlgui5/gwenview/gwenviewui.rc
%attr(755,root,root) %{_bindir}/gwenview_importer
%{_datadir}/metainfo/org.kde.gwenview.appdata.xml
%{_datadir}/solid/actions/gwenview_importer.desktop
%{_datadir}/solid/actions/gwenview_importer_camera.desktop
%attr(755,root,root) %{_datadir}/kconf_update/gwenview-imageview-alphabackgroundmode-update.pl
%{_datadir}/kconf_update/gwenview.upd
