Name:           cargs
Version:        1.2.0
Release:        0%{?autorelease}
Summary:        A lightweight cross-platform getopt alternative that is tested on Linux, Windows, FreeBSD and macOS..

License:        LGPL
URL:            https://github.com/likle/cargs/
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  rpm_macro(cmake)
BuildRequires:  rpm_macro(cmake_build)
BuildRequires:  rpm_macro(cmake_install)
BuildRequires:  cmake
BuildRequires:  gcc

%description
libcargs - command line argument library for C/C++
This is a lighweight C command line argument library which does not require any malloc. It is currently compiled and tested under Linux, FreeBSD, macOS and Windows.

Features
Please have a look at the reference for detailed information. Some features this library includes:

cross-platform on windows, linux and macOS
simple interface - just one header
one simple loop - to iterate over the arguments
automatic help output - showing all options available
long and short options - giving users alternatives
option values - for options which are more than just flags
no malloc needed - for situations where that's not available.

%package devel
Summary:        Development libraries and header files for %{name}

%description devel
%{summary}.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_libdir}/lib%{name}.so{,.0}
ln -s %{buildroot}%{_libdir}/lib%{name}.so{.0,}

%files
%{_libdir}/lib%{name}.so.0

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
