%define		pkgname skype
Summary:	p2p VoIP application
Summary(pl.UTF-8):	Aplikacja VoIP p2p
Name:		skype
Version:	2.1.0.81
Release:	4
# http://www.skype.com/company/legal/promote/distributionterms.html
# distributing on CD-ROM and similar media requires approval
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	http://download.skype.com/linux/%{pkgname}-ubuntu-intrepid_%{version}-1_amd64.deb
# Source0-md5:	1c4da1a157e95418be10e84900924f92
Patch0:		%{name}-desktop.patch
URL:		http://www.skype.com/
BuildRequires:	rpm-utils
# to force 32bit iconv
Requires:	%{_libdir}/gconv
Requires:	QtCore >= 4.2.1
Requires:	QtDBus >= 4.2.1
Requires:	QtGui >= 4.2.1
Requires:	QtNetwork >= 4.2.1
Requires:	alsa-lib >= 1.0.12
Requires:	iconv
Requires:	libsigc++ >= 2.0
Provides:	skype-program = %{version}
Conflicts:	skype-static
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0
# https://developer.skype.com/jira/browse/SCL-569
%define		no_install_post_strip	1

# So that building package on AC system won't write package name dep that Th system can't understand (libstdc++4)
%define		_noautoreqdep	libstdc++.so.6

%description
p2p VoIP application.

License requirement: The Software originates from Skype and use the
links and graphics as published and indicated on
<http://www.skype.com/go/redistribution/>.

%description -l pl.UTF-8
Aplikacja VoIP p2p.

Wymaganie licencyjne: to oprogramowanie pochodzi od Skype i
wykorzystuje odnośniki i grafikę w postaci opublikowanej i oznaczonej
na <http://www.skype.com/go/redistribution/>.

%prep
%setup -qcT
ar x %{SOURCE0}
tar xzf data.tar.gz
mv usr/share/doc/skype/copyright LICENSE
mv usr/share/skype/avatars .
mv usr/bin/skype .
mv usr/share/skype/sounds .
mv usr/share/skype/lang .
mv etc/dbus-1/system.d/skype.conf .
mv usr/share/pixmaps/skype.png .
mv usr/share/applications/skype.desktop .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{pkgname},%{_datadir}/%{pkgname}/{lang,sounds,avatars},%{_desktopdir},/etc/dbus-1/system.d}

install -p %{pkgname} $RPM_BUILD_ROOT%{_bindir}
cp -a sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/sounds
cp -a lang/*.qm $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/lang
cp -a avatars/*.png $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/avatars
cp -a skype.conf $RPM_BUILD_ROOT/etc/dbus-1/system.d
cp -a *.desktop $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a skype.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
/etc/dbus-1/system.d/skype.conf
%attr(755,root,root) %{_bindir}/skype

%dir %{_datadir}/%{pkgname}
%{_datadir}/%{pkgname}/sounds
%{_datadir}/%{pkgname}/avatars

%dir %{_datadir}/%{pkgname}/lang
%lang(bg) %{_datadir}/%{pkgname}/lang/skype_bg.qm
%lang(de) %{_datadir}/%{pkgname}/lang/skype_de.qm
%lang(en) %{_datadir}/%{pkgname}/lang/skype_en.qm
%lang(es) %{_datadir}/%{pkgname}/lang/skype_es.qm
%lang(et) %{_datadir}/%{pkgname}/lang/skype_et.qm
%lang(fr) %{_datadir}/%{pkgname}/lang/skype_fr.qm
%lang(it) %{_datadir}/%{pkgname}/lang/skype_it.qm
%lang(ja) %{_datadir}/%{pkgname}/lang/skype_ja.qm
%lang(ko) %{_datadir}/%{pkgname}/lang/skype_ko.qm
%lang(lt) %{_datadir}/%{pkgname}/lang/skype_lt.qm
%lang(lv) %{_datadir}/%{pkgname}/lang/skype_lv.qm
%lang(pl) %{_datadir}/%{pkgname}/lang/skype_pl.qm
%lang(pt) %{_datadir}/%{pkgname}/lang/skype_pt_pt.qm
%lang(pt_BR) %{_datadir}/%{pkgname}/lang/skype_pt_br.qm
%lang(ro) %{_datadir}/%{pkgname}/lang/skype_ro.qm
%lang(ru) %{_datadir}/%{pkgname}/lang/skype_ru.qm
%lang(th) %{_datadir}/%{pkgname}/lang/skype_th.qm
%lang(tr) %{_datadir}/%{pkgname}/lang/skype_tr.qm
%lang(uk) %{_datadir}/%{pkgname}/lang/skype_uk.qm
%lang(zh) %{_datadir}/%{pkgname}/lang/skype_zh_s.qm
%lang(zh_TW) %{_datadir}/%{pkgname}/lang/skype_zh_t.qm

%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
