Summary:	p2p VoIP application
Summary(pl):	Aplikacja VoIP p2p
Name:		skype
Version:	1.3.0.53
Release:	1
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	http://download.skype.com/linux/%{name}-%{version}-generic.tar.bz2
# Source0-md5:	e288e398e4a34a5760ff6321b253ed08
Patch0:		%{name}-desktop.patch
URL:		http://www.skype.com/
Requires:	qt >= 6:3.2
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
p2p VoIP application.

License requirement: The Software originates from Skype and use the
links and graphics as published and indicated on
<http://www.skype.com/go/redistribution/>.

%description -l pl
Aplikacja VoIP p2p.

Wymaganie licencyjne: to oprogramowanie pochodzi od Skype i
wykorzystuje odno¶niki i grafikê w postaci opublikowanej i oznaczonej
na <http://www.skype.com/go/redistribution/>.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_datadir}/%{name}/{lang,sound},%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps/,%{_desktopdir},%{_sysconfdir}/dbus-1/system.d}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install sound/*.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sound
install lang/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/lang
install skype.conf $RPM_BUILD_ROOT%{_sysconfdir}/dbus-1/system.d
install icons/skype_32_32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
# The following are 16x16 and 48x48 icons
install icons/skype_16_32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install icons/skype_48_32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install *.desktop $RPM_BUILD_ROOT%{_desktopdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/%{name}/lang/skype_{no,nb}.qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/sound

%dir %{_datadir}/%{name}/lang
%lang(ar) %{_datadir}/%{name}/lang/skype_ar.qm
%lang(bg) %{_datadir}/%{name}/lang/skype_bg.qm
%lang(cs) %{_datadir}/%{name}/lang/skype_cs.qm
%lang(cz) %{_datadir}/%{name}/lang/skype_cz.qm
%lang(da) %{_datadir}/%{name}/lang/skype_da.qm
%lang(de) %{_datadir}/%{name}/lang/skype_de.qm
%lang(el) %{_datadir}/%{name}/lang/skype_el.qm
%lang(en) %{_datadir}/%{name}/lang/skype_en.qm
%lang(es) %{_datadir}/%{name}/lang/skype_es.qm
%lang(et) %{_datadir}/%{name}/lang/skype_et.qm
%lang(fi) %{_datadir}/%{name}/lang/skype_fi.qm
%lang(fr) %{_datadir}/%{name}/lang/skype_fr.qm
%lang(he) %{_datadir}/%{name}/lang/skype_he.qm
%lang(hu) %{_datadir}/%{name}/lang/skype_hu.qm
%lang(it) %{_datadir}/%{name}/lang/skype_it.qm
%lang(ja) %{_datadir}/%{name}/lang/skype_ja.qm
%lang(ko) %{_datadir}/%{name}/lang/skype_ko.qm
%lang(nl) %{_datadir}/%{name}/lang/skype_nl.qm
%lang(nb) %{_datadir}/%{name}/lang/skype_nb.qm
%lang(pl) %{_datadir}/%{name}/lang/skype_pl.qm
%lang(pp) %{_datadir}/%{name}/lang/skype_pp.qm
%lang(pt) %{_datadir}/%{name}/lang/skype_pt.qm
%lang(ro) %{_datadir}/%{name}/lang/skype_ro.qm
%lang(ru) %{_datadir}/%{name}/lang/skype_ru.qm
%lang(sv)  %{_datadir}/%{name}/lang/skype_sv.qm
%lang(th) %{_datadir}/%{name}/lang/skype_th.qm
%lang(tr) %{_datadir}/%{name}/lang/skype_tr.qm
%lang(x1) %{_datadir}/%{name}/lang/skype_x1.qm
%{_sysconfdir}/dbus-1/system.d/skype.conf
%{_iconsdir}/hicolor/*x*/apps/%{name}.png
%{_desktopdir}/*.desktop
