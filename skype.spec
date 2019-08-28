Summary:	p2p VoIP application
Summary(pl.UTF-8):	Aplikacja VoIP p2p
Name:		skype
Version:	8.51.0.92
Release:	1
Epoch:		1
# http://www.skype.com/company/legal/promote/distributionterms.html
# distributing on CD-ROM and similar media requires approval
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	https://repo.skype.com/deb/pool/main/s/skypeforlinux/skypeforlinux_%{version}_amd64.deb
# Source0-md5:	e65f32767eb510d86db889247d6e9767
Patch0:		%{name}-desktop.patch
URL:		https://www.skype.com/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Provides:	skype-program = %{version}
Conflicts:	skype-static
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0
%define		no_install_post_strip	1

# internal caps not to require (packaged here)
%define		int_caps	libEGL.so libGLESv2.so libffmpeg.so

%define		_noautoprovfiles	%{_appdir}

# list of script capabilities (regexps) not to be used in Provides
%define		_noautoreq		%{int_caps}

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
v=$(strings skypeforlinux/resources/app.asar | grep -C 3 '"productName": "Skype",' | grep -m 1 '"version":' | sed 's/.*: "\([0-9.]\+\)".*/\1/')
c=$(strings skypeforlinux/resources/app.asar | grep '"buildChannel":' | sed 's/.*: "\([^"]\+\)".*/\1/')
test "$v" = "%{version}" -a "$c" = "production"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_appdir}}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
ln -s skypeforlinux $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a skypeforlinux/* $RPM_BUILD_ROOT%{_appdir}
cp -a usr/share/* $RPM_BUILD_ROOT%{_datadir}

sed -i -e 's|/share/|/%{_lib}/|g' $RPM_BUILD_ROOT%{_bindir}/skypeforlinux

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc doc/* LICENSE*
%attr(755,root,root) %{_bindir}/skype
%attr(755,root,root) %{_bindir}/skypeforlinux
%{_desktopdir}/skypeforlinux.desktop
%{_pixmapsdir}/skypeforlinux.png
%{_iconsdir}/hicolor/*/apps/skypeforlinux.png

%dir %{_appdir}
%attr(755,root,root) %{_appdir}/chrome-sandbox
%attr(755,root,root) %{_appdir}/libEGL.so
%attr(755,root,root) %{_appdir}/libGLESv2.so
%attr(755,root,root) %{_appdir}/libffmpeg.so
%attr(755,root,root) %{_appdir}/skypeforlinux
%dir %{_appdir}/swiftshader
%attr(755,root,root) %{_appdir}/swiftshader/libEGL.so
%attr(755,root,root) %{_appdir}/swiftshader/libGLESv2.so
%{_appdir}/*.pak
%{_appdir}/icudtl.dat
%{_appdir}/natives_blob.bin
%{_appdir}/snapshot_blob.bin
%{_appdir}/v8_context_snapshot.bin
%{_appdir}/version

%dir %{_appdir}/resources
%{_appdir}/resources/app.asar
%{_appdir}/resources/default_app.asar
%{_appdir}/resources/electron.asar

%dir %{_appdir}/resources/app.asar.unpacked
%dir %{_appdir}/resources/app.asar.unpacked/node_modules
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/cld
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/cld/build
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/cld/build/Release
%{_appdir}/resources/app.asar.unpacked/node_modules/cld/build/Release/cld.node
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/desktop-idle
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/desktop-idle/build
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/desktop-idle/build/Release
%{_appdir}/resources/app.asar.unpacked/node_modules/desktop-idle/build/Release/desktopIdle.node
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/electron-ssid
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/electron-ssid/build
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/electron-ssid/build/Release
%{_appdir}/resources/app.asar.unpacked/node_modules/electron-ssid/build/Release/electron-ssid.node
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/@felixrieseberg
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/@felixrieseberg/spellchecker
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/@felixrieseberg/spellchecker/build
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/@felixrieseberg/spellchecker/build/Release
%{_appdir}/resources/app.asar.unpacked/node_modules/@felixrieseberg/spellchecker/build/Release/spellchecker.node
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/keyboard-layout
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/keyboard-layout/build
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/keyboard-layout/build/Release
%{_appdir}/resources/app.asar.unpacked/node_modules/keyboard-layout/build/Release/keyboard-layout-manager.node
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/keytar
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/keytar/build
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/keytar/build/Release
%attr(755,root,root) %{_appdir}/resources/app.asar.unpacked/node_modules/keytar/build/Release/keytar.node
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/slimcore
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/slimcore/bin
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/slimcore/bin/sharing-indicator.node
%{_appdir}/resources/app.asar.unpacked/node_modules/slimcore/bin/slimcore.node
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/sqlite3
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/sqlite3/lib
%dir %{_appdir}/resources/app.asar.unpacked/node_modules/sqlite3/lib/binding
%attr(755,root,root) %{_appdir}/resources/app.asar.unpacked/node_modules/sqlite3/lib/binding/node_sqlite3.node
%{_appdir}/locales
