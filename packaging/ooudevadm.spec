Name:           ooudevadm
Version:        0.1.0
Release:        1%{?dist}
Summary:        Queries system device manager attributes, udev events, and hardware rules.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooudevadm
Source0:        ooudevadm-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooudevadm is a sovereign, capability-bounded UDEV DISPATCHER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooudevadm
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooudevadm-uninstall

%files
/usr/bin/ooudevadm
/usr/bin/ooudevadm-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
