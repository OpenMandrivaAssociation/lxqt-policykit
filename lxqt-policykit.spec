Name: lxqt-policykit
Version: 0.7.0
Release: 1
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Summary: LXQt PolicyKit agent
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: qt4-devel
BuildRequires: polkit-qt-1-devel

%description
LXQt PolicyKit agent

%prep
%setup -q -c %{name}-%{version}
export CMAKE_PREFIX_PATH=%{_libdir}/cmake/PolkitQt-1
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_bindir}/lxqt-policykit-agent
