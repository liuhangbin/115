# https://bugzilla.redhat.com/show_bug.cgi?id=1869423
%global __filter_GLIBC_PRIVATE 1
# do not call strip
%global __os_install_post %{nil}
# do not provides/requires for 115 private lib
%global __provides_exclude_from /usr/local/115/(lib/.*|plugins/.*)$
%global __requires_exclude_from /usr/local/115/(lib/.*|plugins/.*)$
%global __requires_exclude ^(libQt5.*|libav.*|libswresample.*)$

Name: 115
Version: 1.0.8.9
Release: 1%{?dist}
Summary: 115 PC client for Linux
License: 115 License Agreement
URL: https://pc.115.com/
Source0: https://down.115.com/client/%{name}pc/lin/%{name}pc_%{version}.deb
BuildArch: x86_64
BuildRequires: alien

%description
115 PC client for Linux

%prep
# use our own way to extract the files
cp -p %{SOURCE0} .
rm -rf %{name}pc-%{version}
rm -rf %{name}pc-%{version}
alien -t -g %{name}pc_%{version}.deb
%setup -T -D

%install
mkdir -p %{buildroot}/usr/local/
mkdir -p %{buildroot}/usr/share/applications/
# do not update via client
echo '#!/bin/bash' > usr/local/115/update.sh
echo "echo 'Fedora无法直接安装deb包，请等待repo更新或者联系liuhangbin@gmail.com'" >> usr/local/115/update.sh
cp -a usr/local/115 %{buildroot}/usr/local/
install -m 644 usr/share/applications/115.desktop %{buildroot}/usr/share/applications/115.desktop

%files
/usr/local/115
/usr/share/applications/115.desktop

%changelog
* Tue Jul 19 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.8.9-1
- Update to 1.0.8.9

* Wed Jun 15 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.7.7-1
- Update to 1.0.7.7

* Thu May 12 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.6.7-2
- Do not update via client by default

* Thu May 12 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.6.7-1
- Update to 1.0.6.7

* Wed Apr 27 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.5.18-1
- Update to 1.0.5.18

* Mon Mar 7 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.1-6
- Update to 1.0.1-6

* Mon Mar 7 2022 Hangbin Liu <liuhangbin@gmail.com> - 1.0.0-16
- Initial build
