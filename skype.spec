Summary:	p2p VoIP application
Summary(pl.UTF-8):	Aplikacja VoIP p2p
Name:		skype
Version:	1.4.0.99
Release:	0.1
# http://www.skype.com/company/legal/promote/distributionterms.html
# distributing on CD-ROM and similar media requires approval
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	http://download.skype.com/linux/%{name}-%{version}.tar.bz2
# Source0-md5:	9f5c92378ec6bb42927c9f21cd535d9a
#Patch0:		%{name}-desktop.patch
URL:		http://www.skype.com/
Requires:	QtCore >= 4.2.3
Requires:	QtDBus >= 4.2.3
Requires:	QtGui >= 4.2.3
Requires:	QtNetwork >= 4.2.3
Requires:	libsigc++ >= 2.0
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
#%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_datadir}/%{name}/{lang,sounds},%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps/,%{_desktopdir},%{_sysconfdir}/dbus-1/system.d}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install sounds/*.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
install skype.conf $RPM_BUILD_ROOT%{_sysconfdir}/dbus-1/system.d
install icons/SkypeBlue_16x16.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install icons/SkypeBlue_32x32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install icons/SkypeBlue_48x48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install *.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/sounds

%{_sysconfdir}/dbus-1/system.d/skype.conf
%{_iconsdir}/hicolor/*x*/apps/%{name}.png
%{_desktopdir}/*.desktop
