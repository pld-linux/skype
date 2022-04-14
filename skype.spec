Summary:	p2p VoIP application
Summary(pl.UTF-8):	Aplikacja VoIP p2p
Name:		skype
Version:	8.83.0.408
Release:	1
Epoch:		1
# http://www.skype.com/company/legal/promote/distributionterms.html
# distributing on CD-ROM and similar media requires approval
License:	Commercial, redistributable (see LICENSE)
Group:		Applications/Communications
Source0:	https://repo.skype.com/deb/pool/main/s/skypeforlinux/skypeforlinux_%{version}_amd64.deb
# Source0-md5:	8839f2711546edd95a665265504ca7b2
Patch0:		%{name}-desktop.patch
URL:		https://www.skype.com/
BuildRequires:	tar >= 1:1.22
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
tar xf data.tar.gz
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

%{__rm} -r $RPM_BUILD_ROOT%{_appdir}/resources/app.asar.unpacked/images/tray/{mac,win}

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
%{_desktopdir}/skypeforlinux-share.desktop
%{_pixmapsdir}/skypeforlinux.png
%{_iconsdir}/hicolor/*/apps/skypeforlinux.png
%{_datadir}/kservices5/ServiceMenus/skypeforlinux.desktop

%dir %{_appdir}
%attr(755,root,root) %{_appdir}/chrome-sandbox
%attr(755,root,root) %{_appdir}/chrome_crashpad_handler
%attr(755,root,root) %{_appdir}/libEGL.so
%attr(755,root,root) %{_appdir}/libGLESv2.so
%attr(755,root,root) %{_appdir}/libffmpeg.so
%attr(755,root,root) %{_appdir}/libvulkan.so.1
%attr(755,root,root) %{_appdir}/skypeforlinux
%attr(755,root,root) %{_appdir}/libvk_swiftshader.so
%{_appdir}/vk_swiftshader_icd.json
%dir %{_appdir}/swiftshader
%attr(755,root,root) %{_appdir}/swiftshader/libEGL.so
%attr(755,root,root) %{_appdir}/swiftshader/libGLESv2.so
%{_appdir}/*.pak
%{_appdir}/icudtl.dat
%{_appdir}/snapshot_blob.bin
%{_appdir}/v8_context_snapshot.bin
%{_appdir}/version

%dir %{_appdir}/resources
%{_appdir}/resources/app.asar
%{_appdir}/resources/default_app.asar

%dir %{_appdir}/resources/app.asar.unpacked
%dir %{_appdir}/resources/app.asar.unpacked/images
%dir %{_appdir}/resources/app.asar.unpacked/images/tray
%{_appdir}/resources/app.asar.unpacked/images/tray/linux
%{_appdir}/resources/app.asar.unpacked/images/tray/presence
%dir %{_appdir}/resources/app.asar.unpacked/modules
%{_appdir}/resources/app.asar.unpacked/modules/electron_utility.node
%{_appdir}/resources/app.asar.unpacked/modules/keytar.node
%{_appdir}/resources/app.asar.unpacked/modules/platform.node
%{_appdir}/resources/app.asar.unpacked/modules/sharing-indicator.node
%{_appdir}/resources/app.asar.unpacked/modules/slimcore.node
%{_appdir}/resources/app.asar.unpacked/modules/trouter-client.node
%{_appdir}/locales
