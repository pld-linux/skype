Summary:	p2p voip application
Name:		skype
Version:	0.90.0.3
Release:	0.1
License:	Commercial, redistributable
Group:		Applications/Communications
Source0:	http://download.skype.com/linux/skype_ver-%(echo %{version} | tr '.' '_').tar.bz2
# Source0-md5:	60f4d878a5fddebb2d744822833a5697
URL:		http://www.skype.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
p2p voip application.

License requirement:
The Software originates from Skype and use the links
and graphics as published and indicated on
www.skype.com/go/redistribution

%prep
%setup -q -n %{name}_ver-%(echo %{version} | tr '.' '_')

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_pixmapsdir},%{_applnkdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install *.wav $RPM_BUILD_ROOT%{_datadir}/%{name}
install icons/skype_32_32.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install *.desktop $RPM_BUILD_ROOT%{_applnkdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*.png
%{_applnkdir}/*.desktop
