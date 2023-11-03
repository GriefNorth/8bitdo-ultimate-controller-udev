Name:           8bitdo-ultimate-controller-udev
Version:        1.1
Release:        1
Summary:        udev rules for 8bitdo controller 2.4GHz mode 
License:        GPL-3.0-or-later
Group:          Hardware/Games
URL:            https://aur.archlinux.org/8bitdo-ultimate-controller-udev.git
Source0:        https://github.com/GriefNorth/8bitdo-ultimate-controller-udev/archive/%{name}-%{version}.tar.gz
Requires:       xboxdrv
Provides:       8bitdo-ultimate-controller-udev = %{version}
Obsoletes:      8bitdo-ultimate-controller-udev < %{version}
BuildArch:      noarch
BuildRequires:  systemd

%description

%prep
%autosetup -p1

%pre

%install
install -D -m 0644 -t %{buildroot}%{_udevrulesdir} 99-8bitdo-ultimate-controllers.rules
install -D -m 0644 -t %{buildroot}%{_unitdir} 8bitdo-ultimate-xinput@.service
install -D -m 0644 -t %{buildroot}%{_unitdir} 8bitdo-ultimate-dinput@.service

%preun
%systemd_preun 8bitdo-ultimate-xinput@.service
%systemd_preun 8bitdo-ultimate-dinput@.service

%post
%udev_rules_update
%systemd_post 8bitdo-ultimate-xinput@.service
%systemd_post 8bitdo-ultimate-dinput@.service

%postun
%udev_rules_update
%systemd_postun 8bitdo-ultimate-xinput@.service
%systemd_postun 8bitdo-ultimate-dinput@.service

%files
%defattr(-,root,root,-)
%{_udevrulesdir}/99-8bitdo-ultimate-controllers.rules
%{_unitdir}/8bitdo-ultimate-xinput@.service
%{_unitdir}/8bitdo-ultimate-dinput@.service

%changelog

