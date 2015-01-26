%define git 0

Name: lxqt-policykit
Version: 0.8.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 3
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Patch0:	lxqt-policykit-20140803-compile.patch
Summary: LXQt PolicyKit agent
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt-qt5)
BuildRequires: qt5-devel
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(PolkitQt5-1)
Provides:	polkit-agent

%description
LXQt PolicyKit agent.

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%apply_patches
export CMAKE_PREFIX_PATH=%{_libdir}/cmake/PolkitQt-1
%cmake -DUSE_QT5:BOOL=ON

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_bindir}/lxqt-policykit-agent
