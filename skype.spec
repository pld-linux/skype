# TODO:
#	- seperate translations
#
Summary:	p2p VoIP application
Summary(pl):	Aplikacja VoIP p2p
Name:		skype
Version:	0.91.0.12
Release:	0.2
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
install *.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/lang
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
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
