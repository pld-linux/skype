Summary:	p2p VoIP application
Summary(pl.UTF-8):	Aplikacja VoIP p2p
Name:		skype
Version:	2.1.0.81
Release:	1
# http://www.skype.com/company/legal/promote/distributionterms.html
# distributing on CD-ROM and similar media requires approval
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	http://download.skype.com/linux/%{name}-%{version}-fc10.i586.rpm
# Source0-md5:	fe9ba37b14d9a9ac2c8f65ac0721e5bd
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
rpm2cpio %{SOURCE0} | cpio -dimu
mv usr/bin/skype .
mv usr/share/skype/sounds .
mv usr/share/skype/lang .
mv etc/dbus-1/system.d/skype.conf .
mv usr/share/pixmaps/skype.png .
mv usr/share/applications/skype.desktop .
mv usr/share/doc/skype-%{version}/LICENSE .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_datadir}/%{name}/{lang,sounds,avatars},%{_pixmapsdir},%{_desktopdir},/etc/dbus-1/system.d}

install -p %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
cp -a lang/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/lang
cp -a skype.conf $RPM_BUILD_ROOT/etc/dbus-1/system.d
cp -a skype.png $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a *.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/skype

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/sounds

%dir %{_datadir}/%{name}/lang
%lang(bg) %{_datadir}/%{name}/lang/skype_bg.qm
%lang(de) %{_datadir}/%{name}/lang/skype_de.qm
%lang(en) %{_datadir}/%{name}/lang/skype_en.qm
%lang(es) %{_datadir}/%{name}/lang/skype_es.qm
%lang(et) %{_datadir}/%{name}/lang/skype_et.qm
%lang(fr) %{_datadir}/%{name}/lang/skype_fr.qm
%lang(it) %{_datadir}/%{name}/lang/skype_it.qm
%lang(ja) %{_datadir}/%{name}/lang/skype_ja.qm
%lang(ko) %{_datadir}/%{name}/lang/skype_ko.qm
%lang(lv) %{_datadir}/%{name}/lang/skype_lv.qm
%lang(lt) %{_datadir}/%{name}/lang/skype_lt.qm
%lang(pl) %{_datadir}/%{name}/lang/skype_pl.qm
%lang(pt_BR) %{_datadir}/%{name}/lang/skype_pt_br.qm
%lang(pt) %{_datadir}/%{name}/lang/skype_pt_pt.qm
%lang(ro) %{_datadir}/%{name}/lang/skype_ro.qm
%lang(ru) %{_datadir}/%{name}/lang/skype_ru.qm
%lang(th) %{_datadir}/%{name}/lang/skype_th.qm
%lang(tr) %{_datadir}/%{name}/lang/skype_tr.qm
%lang(zh) %{_datadir}/%{name}/lang/skype_zh_s.qm
%lang(zh_TW) %{_datadir}/%{name}/lang/skype_zh_t.qm

/etc/dbus-1/system.d/skype.conf
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
