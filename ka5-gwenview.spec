# TODO, fix build with ka5-libkdcraw-devel and ka5-libkipi-devel (missing cmake files)
%define		kdeappsver	15.08.0
%define		qtver		5.3.2
%define		kaname		gwenview
Summary:	Simple image viewer
Name:		ka5-%{kaname}
Version:	15.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7e5ef1e30584e22bfb81c9b86e08a67d
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	exiv2-devel
BuildRequires:	gettext-tools
BuildRequires:	ka5-libkdcraw-devel
BuildRequires:	ka5-libkipi-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kactivities-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	lcms2-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# -f %{kaname}.lang
%attr(755,root,root) %{_bindir}/gwenview
%attr(755,root,root) %{_libdir}/libgwenviewlib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgwenviewlib.so.5
%attr(755,root,root)        %{_libdir}/qt5/plugins/gvpart.so
%{_datadir}/appdata/gwenview.appdata.xml
%{_desktopdir}/org.kde.gwenview.desktop
%{_datadir}/gwenview
%{_iconsdir}/hicolor/*/actions/document-share.png
%{_iconsdir}/hicolor/*/apps/gwenview.png
%{_datadir}/kservices5/ServiceMenus/slideshow.desktop
%{_datadir}/kservices5/gvpart.desktop
%{_datadir}/kxmlgui5/gvpart/gvpart.rc
%{_datadir}/kxmlgui5/gwenview/gwenviewui.rc
