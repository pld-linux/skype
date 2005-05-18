Summary:	p2p VoIP application
Summary(pl):	Aplikacja VoIP p2p
Name:		skype
Version:	1.1.0.3
Release:	2
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	http://download.skype.com/linux/%{name}-%{version}.tar.bz2
# Source0-md5:	8b0a7778c789528c2e7a4057d113d013
Patch0:		%{name}-desktop.patch
URL:		http://www.skype.com/
BuildRequires:	sed >= 4.0
Requires:	qt >= 3.2
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_datadir}/%{name}/{lang,sound},%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps/,%{_desktopdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install sound/*.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sound
install lang/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/lang
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
%lang(da) %{_datadir}/%{name}/lang/skype_da.qm
%lang(de) %{_datadir}/%{name}/lang/skype_de.qm
%lang(el) %{_datadir}/%{name}/lang/skype_el.qm
%lang(en) %{_datadir}/%{name}/lang/skype_en.qm
%lang(es) %{_datadir}/%{name}/lang/skype_es.qm
%lang(es_AR) %{_datadir}/%{name}/lang/skype_es_AR.qm
%lang(et) %{_datadir}/%{name}/lang/skype_et.qm
%lang(fi) %{_datadir}/%{name}/lang/skype_fi.qm
%lang(fr) %{_datadir}/%{name}/lang/skype_fr.qm
%lang(it) %{_datadir}/%{name}/lang/skype_it.qm
%lang(iw) %{_datadir}/%{name}/lang/skype_iw.qm
%lang(ja) %{_datadir}/%{name}/lang/skype_ja.qm
%lang(ko) %{_datadir}/%{name}/lang/skype_ko.qm
%lang(nl) %{_datadir}/%{name}/lang/skype_nl.qm
%lang(nb) %{_datadir}/%{name}/lang/skype_nb.qm
%lang(pl) %{_datadir}/%{name}/lang/skype_pl.qm
%lang(pt_BR) %{_datadir}/%{name}/lang/skype_pt_BR.qm
%lang(ro) %{_datadir}/%{name}/lang/skype_ro.qm
%lang(ru) %{_datadir}/%{name}/lang/skype_ru.qm
%lang(sv)  %{_datadir}/%{name}/lang/skype_sv.qm
%lang(zh_CN) %{_datadir}/%{name}/lang/skype_zh_CN.qm
%lang(zh_TW) %{_datadir}/%{name}/lang/skype_zh_TW.qm
%{_iconsdir}/hicolor/*x*/apps/%{name}.png
%{_desktopdir}/*.desktop
