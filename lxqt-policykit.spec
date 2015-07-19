%define git 0

Name: lxqt-policykit
Version: 0.9.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 3
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Patch1: lxqt-policykit-0.9.0-cmake-libexec.patch
Summary: LXQt PolicyKit agent
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: cmake(qt5xdg)
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt5Widgets)
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

export CMAKE_PREFIX_PATH=%{_libdir}/cmake/PolkitQt5-1
%cmake -DPOLKIT_AGENT_BINARY_DIR=%{_libexecdir}

%build
%make -C build

%install
%makeinstall_std -C build

%find_lang %{name}-agent --with-qt

%files -f %{name}-agent.lang
%{_libexecdir}/lxqt-policykit-agent
