# TODO:
#	- seperate translations
#
Summary:	p2p VoIP application
Summary(pl):	Aplikacja VoIP p2p
Name:		skype
Version:	0.91.0.12
Release:	0.3
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	http://download.skype.com/linux/%{name}_ver-%(echo %{version} | tr . _).tar.bz2
# Source0-md5:	1cb31f95ecf3521615e4ceb1b3841b65
URL:		http://www.skype.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
p2p VoIP application.

License requirement: The Software originates from Skype and use the
links and graphics as published and indicated on
http://www.skype.com/go/redistribution/ .

%description -l pl
Aplikacja VoIP p2p.

Wymaganie licencyjne: to oprogramowanie pochodzi od Skype i
wykorzystuje odno¶niki i grafikê w postaci opublikowanej i oznaczonej
na http://www.skype.com/go/redistribution/ .

%prep
%setup -q -n %{name}_ver-%(echo %{version} | tr '.' '_')

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_datadir}/%{name}/lang,%{_pixmapsdir},%{_desktopdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install *.wav $RPM_BUILD_ROOT%{_datadir}/%{name}
mv -f *.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/lang/
install icons/skype_32_32.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install *.desktop $RPM_BUILD_ROOT%{_desktopdir}
echo "Categories=Qt;KDE;Network;InstantMessaging;">> $RPM_BUILD_ROOT%{_desktopdir}/skype.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%lang(da) %{_datadir}/%{name}/lang/skype_da.qm
%lang(de) %{_datadir}/%{name}/lang/skype_de.qm
%lang(el) %{_datadir}/%{name}/lang/skype_el.qm
%lang(en) %{_datadir}/%{name}/lang/skype_en.qm
%lang(es) %{_datadir}/%{name}/lang/skype_es.qm
%lang(es_ar) %{_datadir}/%{name}/lang/skype_es_AR.qm
%lang(et) %{_datadir}/%{name}/lang/skype_et.qm
%lang(fi) %{_datadir}/%{name}/lang/skype_fi.qm
%lang(fr) %{_datadir}/%{name}/lang/skype_fr.qm
%lang(it) %{_datadir}/%{name}/lang/skype_it.qm
%lang(iw) %{_datadir}/%{name}/lang/skype_iw.qm
%lang(ja) %{_datadir}/%{name}/lang/skype_ja.qm
%lang(ko) %{_datadir}/%{name}/lang/skype_ko.qm
%lang(nl) %{_datadir}/%{name}/lang/skype_nl.qm
%lang(no) %{_datadir}/%{name}/lang/skype_no.qm
%lang(pl) %{_datadir}/%{name}/lang/skype_pl.qm
%lang(pt_br) %{_datadir}/%{name}/lang/skype_pt_BR.qm
%lang(ro) %{_datadir}/%{name}/lang/skype_ro.qm
%lang(ru) %{_datadir}/%{name}/lang/skype_ru.qm
%lang(sv)  %{_datadir}/%{name}/lang/skype_sv.qm
%lang(zh_cn) %{_datadir}/%{name}/lang/skype_zh_CN.qm
%lang(zh_tw) %{_datadir}/%{name}/lang/skype_zh_TW.qm

%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
