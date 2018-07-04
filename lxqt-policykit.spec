%define git 0

Name: lxqt-policykit
Version: 0.13.0
%if %git
Release: 1.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 1
Source0: https://downloads.lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
%endif
Patch1: lxqt-policykit-0.9.0-cmake-libexec.patch
Summary: LXQt PolicyKit agent
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
Patch0: lxqt-policykit-0.12.0-fix-path-lxqt-policykit-agent.patch
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: ninja
BuildRequires: cmake(qt5xdg)
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(PolkitQt5-1)
BuildRequires: cmake(lxqt-build-tools)
BuildRequires: git-core
Provides: polkit-agent

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
%cmake_qt5 -DPOLKIT_AGENT_BINARY_DIR=%{_libexecdir} -G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build

%find_lang %{name}-agent --with-qt

%files -f %{name}-agent.lang
%{_libexecdir}/lxqt-policykit-agent
%{_sysconfdir}/xdg/autostart/lxqt-policykit-agent.desktop
