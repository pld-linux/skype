#
# TODO: - segmentation fault
#
Summary:	p2p VoIP application
Summary(pl.UTF-8):	Aplikacja VoIP p2p
Name:		skype
Version:	2.1.0.47
Release:	0.2
# http://www.skype.com/company/legal/promote/distributionterms.html
# distributing on CD-ROM and similar media requires approval
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	http://download.skype.com/linux/%{name}-%{version}.tar.bz2
# Source0-md5:	7396164fb926705300d72cd478458d36
Patch0:		%{name}-desktop.patch
URL:		http://www.skype.com/
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
%define		no_install_post_strip	1

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
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_datadir}/%{name}/{lang,sounds,avatars},%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps,%{_desktopdir},/etc/dbus-1/system.d}

install %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
cp -a lang/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/lang
cp -a avatars/*.png $RPM_BUILD_ROOT%{_datadir}/%{name}/avatars
cp -a skype.conf $RPM_BUILD_ROOT/etc/dbus-1/system.d
cp -a icons/SkypeBlue_16x16.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
cp -a icons/SkypeBlue_32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
cp -a icons/SkypeBlue_48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png
cp -a *.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/sounds
%{_datadir}/%{name}/avatars

%dir %{_datadir}/%{name}/lang
# %lang(ar) %{_datadir}/%{name}/lang/skype_ar.qm
%lang(bg) %{_datadir}/%{name}/lang/skype_bg.qm
# %lang(cs) %{_datadir}/%{name}/lang/skype_cs.qm
# %lang(cz) %{_datadir}/%{name}/lang/skype_cz.qm
# %lang(da) %{_datadir}/%{name}/lang/skype_da.qm
%lang(de) %{_datadir}/%{name}/lang/skype_de.qm
# %lang(el) %{_datadir}/%{name}/lang/skype_el.qm
%lang(en) %{_datadir}/%{name}/lang/skype_en.qm
%lang(es) %{_datadir}/%{name}/lang/skype_es.qm
%lang(et) %{_datadir}/%{name}/lang/skype_et.qm
# %lang(fi) %{_datadir}/%{name}/lang/skype_fi.qm
%lang(fr) %{_datadir}/%{name}/lang/skype_fr.qm
# %lang(he) %{_datadir}/%{name}/lang/skype_he.qm
# %lang(hu) %{_datadir}/%{name}/lang/skype_hu.qm
%lang(it) %{_datadir}/%{name}/lang/skype_it.qm
%lang(ja) %{_datadir}/%{name}/lang/skype_ja.qm
%lang(ko) %{_datadir}/%{name}/lang/skype_ko.qm
%lang(lv) %{_datadir}/%{name}/lang/skype_lv.qm
%lang(lt) %{_datadir}/%{name}/lang/skype_lt.qm
# %lang(nl) %{_datadir}/%{name}/lang/skype_nl.qm
# %lang(nb) %{_datadir}/%{name}/lang/skype_nb.qm
%lang(pl) %{_datadir}/%{name}/lang/skype_pl.qm
# probably pt_BR
%lang(pt_BR) %{_datadir}/%{name}/lang/skype_pt_br.qm
%lang(pt) %{_datadir}/%{name}/lang/skype_pt_pt.qm
%lang(ro) %{_datadir}/%{name}/lang/skype_ro.qm
%lang(ru) %{_datadir}/%{name}/lang/skype_ru.qm
# %lang(sv)  %{_datadir}/%{name}/lang/skype_sv.qm
%lang(th) %{_datadir}/%{name}/lang/skype_th.qm
%lang(tr) %{_datadir}/%{name}/lang/skype_tr.qm
# probably zh
%lang(zh) %{_datadir}/%{name}/lang/skype_zh_s.qm
# probably zh_TW
%lang(zh_TW) %{_datadir}/%{name}/lang/skype_zh_t.qm

/etc/dbus-1/system.d/skype.conf
%{_iconsdir}/hicolor/*x*/apps/%{name}.png
%{_desktopdir}/*.desktop
