#define git 0

Name: lxqt-policykit
Version: 2.4.0
%if 0%{?git:1}
Source0: %{name}-%{git}.tar.xz
%else
Source0: https://github.com/lxqt/lxqt-policykit/releases/download/%{version}/lxqt-policykit-%{version}.tar.xz
%endif
Release: %{?git:0.%{git}.}2
Summary: LXQt PolicyKit agent
URL: https://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
Patch0: lxqt-policykit-0.12.0-fix-path-lxqt-policykit-agent.patch
BuildSystem: cmake
BuildOption: -DPULL_TRANSLATIONS:BOOL=OFF
BuildOption: -DPOLKIT_AGENT_BINARY_DIR=%{_libexecdir}
BuildRequires: cmake(qt6xdg)
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(PolkitQt6-1)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: cmake(lxqt2-build-tools)
Provides: polkit-agent

%description
LXQt PolicyKit agent.

%conf -p
export CMAKE_PREFIX_PATH=%{_libdir}/cmake/PolkitQt6-1

%build -p
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

%install -p
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

%files -f %{name}.lang
%{_libexecdir}/lxqt-policykit-agent
%{_sysconfdir}/xdg/autostart/lxqt-policykit-agent.desktop
%{_mandir}/man1/*.1*
%dir %{_datadir}/lxqt/translations/lxqt-policykit-agent
