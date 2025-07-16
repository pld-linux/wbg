Summary:	Super simple wallpaper application for Wayland compositors
Name:		wbg
Version:	1.3.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://codeberg.org/dnkl/wbg/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f4d3f3e507abbb6008ec8df1295af7f2
URL:		https://codeberg.org/dnkl/wbg/
BuildRequires:	libjpeg-devel
BuildRequires:	libjxl-devel
BuildRequires:	libpng-devel
BuildRequires:	libwebp-devel
BuildRequires:	meson >= 0.58.0
BuildRequires:	ninja
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tllist-devel >= 1.0.1
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Super simple wallpaper application for Wayland compositors
implementing the layer-shell protocol.

Wbg takes a single command line argument: a path to an image file.
This image is displayed scaled-to-fit on all monitors.

More display options, and/or the ability to set a per-monitor
wallpaper may be added in the future.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/wbg
