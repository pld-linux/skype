%define		pkgname skype
%define		qtver	4.7
%define		dbus	1.0
%define		bluez	4.0.0
%define		pulseaudio	1.0
Summary:	p2p VoIP application
Summary(pl.UTF-8):	Aplikacja VoIP p2p
Name:		skype
Version:	1.6.2
Release:	1
Epoch:		1
# http://www.skype.com/company/legal/promote/distributionterms.html
# distributing on CD-ROM and similar media requires approval
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	https://repo.skype.com/latest/%{pkgname}forlinux-64.deb
# Source0-md5:	c3baf39fd1ee9ab8fd2f94a618bd6d57
Source1:	%{name}.sh
Patch0:		%{name}-desktop.patch
URL:		https://www.skype.com/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Provides:	skype-program = %{version}
Conflicts:	skype-static
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0
%define		no_install_post_strip	1

# internal caps not to require (packaged here)
%define		int_caps	libffmpeg.so libnode.so

%define		_noautoprovfiles	%{_appdir}

# list of script capabilities (regexps) not to be used in Provides
%define		_noautoreq  		%{int_caps}

%define		_appdir		%{_libdir}/skypeforlinux

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
tar xf data.tar.xz
mv .%{_docdir}/skypeforlinux doc
mv .%{_bindir} .

mv .%{_datadir}/skypeforlinux .
mv skypeforlinux/LICENSE* .

%patch0 -p1

%build
v=$(cat skypeforlinux/version)
test "$v" = "v%{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_appdir}}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
ln -s skypeforlinux $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a skypeforlinux/* $RPM_BUILD_ROOT%{_appdir}
cp -a usr/share/* $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* LICENSE*
%attr(755,root,root) %{_bindir}/skype
%attr(755,root,root) %{_bindir}/skypeforlinux
%{_desktopdir}/skypeforlinux.desktop
%{_pixmapsdir}/skypeforlinux.png
%{_iconsdir}/hicolor/*/apps/skypeforlinux.png

%dir %{_appdir}
%attr(755,root,root) %{_appdir}/libffmpeg.so
%attr(755,root,root) %{_appdir}/libnode.so
%attr(755,root,root) %{_appdir}/skypeforlinux
%{_appdir}/*.pak
%{_appdir}/icudtl.dat
%{_appdir}/natives_blob.bin
%{_appdir}/snapshot_blob.bin
%{_appdir}/version

%dir %{_appdir}/resources
%{_appdir}/resources/app.asar
%{_appdir}/resources/default_app.asar
%{_appdir}/resources/electron.asar
%dir %{_appdir}/resources/app.asar.unpacked
%dir %{_appdir}/resources/app.asar.unpacked/node_modules
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/keytar
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/keytar/build
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/keytar/build/Release
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/sqlite3
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/sqlite3/lib
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/sqlite3/lib/binding
%attr(755,root,root) %{_appdir}/resources/app.asar.unpacked/node_modules/keytar/build/Release/keytar.node
%attr(755,root,root) %{_appdir}/resources/app.asar.unpacked/node_modules/sqlite3/lib/binding/node_sqlite3.node

%{_appdir}/locales
