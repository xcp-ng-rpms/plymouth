%global package_speccommit 7bef2fadd2045973a66b8fcffc2e2890e900935d
%global usver 0.8.9
%global xsver 0.31.20140113.3
%global xsrel %{xsver}%{?xscount}%{?xshash}
%define plymouthdaemon_execdir %{_sbindir}
%define plymouthclient_execdir %{_bindir}
%define plymouth_libdir %{_libdir}
%define plymouth_initrd_file /boot/initrd-plymouth.img
%define plymouth_rel 0.31.20140113
%global _hardened_build 1


Summary: Graphical Boot Animation and Logger
Name: plymouth
Version: 0.8.9
Release: %{?xsrel}%{?dist}
License: GPLv2+
Group: System Environment/Base
Source0: plymouth-0.8.9.tar.bz2
Source1: boot-duration
Source2: charge.plymouth
Source3: plymouth-update-initrd
Source4: bootlog
Patch0: dont-block-show-splash.patch
Patch1: always-add-text-splash.patch
Patch2: fix-text-splash-os-string.patch
Patch3: fix-details.patch
Patch4: fix-startup-race.patch
Patch5: fix-hide-splash.patch
Patch6: ignore-early-fb-devices.patch
Patch7: fix-ask-password-race.patch
Patch8: serial-console-fixes.patch
Patch9: fix-init-bin-sh.patch
Patch10: resize-proc-cmdline-buffer.patch
Patch11: cursor-fix.patch
Patch12: fix-coldplug-detection.patch
Patch13: ensure-output-gets-terminal.patch
Patch14: activate-new-renderers.patch
Patch15: fix-progress-bar-colors.patch
Patch16: fix-escape-key-for-media-check.patch
Patch17: 0001-Revert-Recreate-boot-log-at-each-boot-instead-of-app.patch
Patch18: 0001-Revert-Make-boot.log-world-readable-by-default.patch
Patch19: 0001-device-manager-fall-back-to-text-mode-if-graphical-d.patch
Patch20: colors.patch

URL: http://www.freedesktop.org/wiki/Software/Plymouth
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: plymouth-core-libs = %{version}-%{release}
Requires: system-logos
Requires(post): plymouth-scripts
Requires: initscripts >= 8.83-1
Conflicts: filesystem < 3
Conflicts: systemd < 185-3

BuildRequires: git
BuildRequires: pkgconfig(libdrm)
BuildRequires: kernel-headers
BuildRequires: pkgconfig(libudev)
BuildRequires: automake, autoconf, libtool
BuildRequires: libxslt, docbook-style-xsl

Obsoletes: plymouth-text-and-details-only < %{version}-%{release}
Obsoletes: plymouth-plugin-pulser < 0.7.0-0.2009.05.08.2
Obsoletes: plymouth-theme-pulser < 0.7.0-0.2009.05.08.2
Obsoletes: plymouth-gdm-hooks < 0.8.4-0.20101119.4
Obsoletes: plymouth-utils < 0.8.4-0.20101119.4


%description
Plymouth provides an attractive graphical boot animation in
place of the text messages that normally get shown.  Text
messages are instead redirected to a log file for viewing
after boot.

%package system-theme
Summary: Plymouth default theme
Group: System Environment/Base
Obsoletes: rhgb < 1:10.0.0
Provides: rhgb = 1:10.0.0
Obsoletes: %{name}-system-plugin <  %{version}-%{release}
Provides: %{name}-system-plugin = %{version}-%{release}
Provides: rhgb = 1:10.0.0
Requires: plymouth(system-theme) = %{version}-%{release}

%description system-theme
This metapackage tracks the current distribution default theme.

%package core-libs
Summary: Plymouth core libraries
Group: Development/Libraries

%description core-libs
This package contains the libply and libply-splash-core libraries
used by Plymouth.

%package graphics-libs
Summary: Plymouth graphics libraries
Group: Development/Libraries
Requires: %{name}-core-libs = %{version}-%{release}
Obsoletes: %{name}-libs < %{version}-%{release}
Provides: %{name}-libs = %{version}-%{release}
BuildRequires: libpng-devel

%description graphics-libs
This package contains the libply-splash-graphics library
used by graphical Plymouth splashes.

%package devel
Summary: Libraries and headers for writing Plymouth splash plugins
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-core-libs = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}
Requires: pkgconfig
BuildRequires: pkgconfig(gtk+-2.0)

%description devel
This package contains the libply and libplybootsplash libraries
and headers needed to develop 3rd party splash plugins for Plymouth.

%package scripts
Summary: Plymouth related scripts
Group: Applications/System
Requires: findutils, coreutils, gzip, cpio, dracut, plymouth

%description scripts
This package contains scripts that help integrate Plymouth with
the system.

%package plugin-label
Summary: Plymouth label plugin
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}
Requires: %{name}-core-libs = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}
BuildRequires: pango-devel >= 1.21.0
BuildRequires: cairo-devel

%description plugin-label
This package contains the label control plugin for
Plymouth. It provides the ability to render text on
graphical boot splashes using pango and cairo.

%package plugin-fade-throbber
Summary: Plymouth "Fade-Throbber" plugin
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}
Requires: %{name}-core-libs = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}

%description plugin-fade-throbber
This package contains the "Fade-In" boot splash plugin for
Plymouth. It features a centered image that fades in and out
while other images pulsate around during system boot up.

%package theme-fade-in
Summary: Plymouth "Fade-In" theme
Group: System Environment/Base
Requires: %{name}-plugin-fade-throbber = %{version}-%{release}
Requires(post): plymouth-scripts
Obsoletes: plymouth-plugin-fade-in <= 0.7.0-0.2009.05.08.2
Provides: plymouth-plugin-fade-in = 0.7.0-0.2009.05.08.2

%description theme-fade-in
This package contains the "Fade-In" boot splash theme for
Plymouth. It features a centered logo that fades in and out
while stars twinkle around the logo during system boot up.

%package plugin-throbgress
Summary: Plymouth "Throbgress" plugin
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}
Requires: %{name}-core-libs = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}
Requires: plymouth-plugin-label

%description plugin-throbgress
This package contains the "throbgress" boot splash plugin for
Plymouth. It features a centered logo and animated spinner that
spins repeatedly while a progress bar advances at the bottom of
the screen.

%package theme-spinfinity
Summary: Plymouth "Spinfinity" theme
Group: System Environment/Base
Requires: %{name}-plugin-throbgress = %{version}-%{release}
Requires(post): plymouth-scripts
Obsoletes: plymouth-plugin-spinfinity <= 0.7.0-0.2009.05.08.2
Provides: plymouth-plugin-spinfinity = 0.7.0-0.2009.05.08.2

%description theme-spinfinity
This package contains the "Spinfinity" boot splash theme for
Plymouth. It features a centered logo and animated spinner that
spins in the shape of an infinity sign.

%package plugin-space-flares
Summary: Plymouth "space-flares" plugin
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}
Requires: %{name}-core-libs = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}
Requires: plymouth-plugin-label

%description plugin-space-flares
This package contains the "space-flares" boot splash plugin for
Plymouth. It features a corner image with animated flares.

%package theme-solar
Summary: Plymouth "Solar" theme
Group: System Environment/Base
Requires: %{name}-plugin-space-flares = %{version}-%{release}
Requires(post): plymouth-scripts
Obsoletes: plymouth-plugin-solar <= 0.7.0-0.2009.05.08.2
Provides: plymouth-plugin-solar = 0.7.0-0.2009.05.08.2
# We require this to fix upgrades (see bug 499940).
Requires: plymouth-system-theme

%description theme-solar
This package contains the "Solar" boot splash theme for
Plymouth. It features a blue flamed sun with animated solar flares.

%package plugin-two-step
Summary: Plymouth "two-step" plugin
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}
Requires: %{name}-core-libs = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}
Requires: plymouth-plugin-label

%description plugin-two-step
This package contains the "two-step" boot splash plugin for
Plymouth. It features a two phased boot process that starts with
a progressing animation synced to boot time and finishes with a
short, fast one-shot animation.

%package theme-charge
Summary: Plymouth "Charge" plugin
Group: System Environment/Base
Requires: %{name}-plugin-two-step = %{version}-%{release}
Requires(post): plymouth-scripts
Provides: plymouth(system-theme) = %{version}-%{release}

%description theme-charge
This package contains the "charge" boot splash theme for
Plymouth. It is the default theme for CentOS Linux.

%package plugin-script
Summary: Plymouth "script" plugin
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}
Requires: %{name}-core-libs = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}

%description plugin-script
This package contains the "script" boot splash plugin for
Plymouth. It features an extensible, scriptable boot splash
language that simplifies the process of designing custom
boot splash themes.

%package theme-script
Summary: Plymouth "Script" plugin
Group: System Environment/Base
Requires: %{name}-plugin-script = %{version}-%{release}
Requires(post): %{_sbindir}/plymouth-set-default-theme

%description theme-script
This package contains the "script" boot splash theme for
Plymouth. It it is a simple example theme the uses the "script"
plugin.

%package theme-spinner
Summary: Plymouth "Spinner" theme
Group: System Environment/Base
Requires: %{name}-plugin-two-step = %{version}-%{release}
Requires(post): plymouth-scripts

%description theme-spinner
This package contains the "spinner" boot splash theme for
Plymouth. It features a small spinner on a dark background.

%prep
%autosetup -S git

# Change the default theme
sed -i -e 's/fade-in/charge/g' src/plymouthd.defaults

%build
autoreconf -f -i
%configure --enable-tracing --disable-tests                      \
           --with-release-file=/etc/os-release                   \
           --with-logo=%{_datadir}/pixmaps/system-logo-white.png \
           --with-background-start-color-stop=0xc6bdd2           \
           --with-background-end-color-stop=0x4e376b             \
           --with-background-color=0x8d59d2                      \
           --disable-gdm-transition                              \
           --enable-systemd-integration                          \
           --without-system-root-install                         \
           --without-rhgb-compat-link                            \
           --without-log-viewer                                  \
           --enable-documentation                                \
           --disable-libkms

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# Glow isn't quite ready for primetime
rm -rf $RPM_BUILD_ROOT%{_datadir}/plymouth/glow/
rm -f $RPM_BUILD_ROOT%{_libdir}/plymouth/glow.so

find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} \;
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} \;

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/plymouth/default-boot-duration
cp %{SOURCE1} $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth

# Add charge, our new default
mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
cp $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/glow/{box,bullet,entry,lock}.png $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge

# Drop glow, it's not very Fedora-y
rm -rf $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/glow

# Revert text theme back to the tribar one
rm -rf $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/text
mv $RPM_BUILD_ROOT%{_libdir}/plymouth/tribar.so $RPM_BUILD_ROOT%{_libdir}/plymouth/text.so
mv $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/tribar $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/text
mv $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/text/tribar.plymouth $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/text/text.plymouth
sed -i -e 's/tribar/text/' $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/text/text.plymouth

cp %{SOURCE3} $RPM_BUILD_ROOT%{_libexecdir}/plymouth/plymouth-update-initrd

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/bootlog

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -f %{_localstatedir}/lib/plymouth/boot-duration ] || cp -f %{_datadir}/plymouth/default-boot-duration %{_localstatedir}/lib/plymouth/boot-duration

%postun
if [ $1 -eq 0 ]; then
    rm -f %{_libdir}/plymouth/default.so
    rm -f /boot/initrd-plymouth.img
fi

%post core-libs -p /sbin/ldconfig
%postun core-libs -p /sbin/ldconfig

%post graphics-libs -p /sbin/ldconfig
%postun graphics-libs -p /sbin/ldconfig

%post theme-charge
export LIB=%{_lib}
if [ $1 -eq 1 ]; then
    %{_sbindir}/plymouth-set-default-theme charge
fi

%postun theme-charge
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "charge" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi

%files
%defattr(-, root, root)
%doc AUTHORS NEWS README
%dir %{_datadir}/plymouth
%dir %{_datadir}/plymouth/themes
%dir %{_datadir}/plymouth/themes/details
%dir %{_datadir}/plymouth/themes/text
%dir %{_libexecdir}/plymouth
%dir %{_localstatedir}/lib/plymouth
%dir %{_libdir}/plymouth/renderers
%dir %{_sysconfdir}/plymouth
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/plymouth/plymouthd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/bootlog
%{plymouthdaemon_execdir}/plymouthd
%{plymouthclient_execdir}/plymouth
%{_bindir}/plymouth
%{_libdir}/plymouth/details.so
%{_libdir}/plymouth/text.so
%{_libdir}/plymouth/renderers/drm*
%{_libdir}/plymouth/renderers/frame-buffer*
%{_datadir}/plymouth/default-boot-duration
%{_datadir}/plymouth/themes/details/details.plymouth
%{_datadir}/plymouth/themes/text/text.plymouth
%{_datadir}/plymouth/plymouthd.defaults
%{_localstatedir}/run/plymouth
%{_localstatedir}/spool/plymouth
%{_mandir}/man?/*
%ghost %{_localstatedir}/lib/plymouth/boot-duration
%{_unitdir}/*

%files devel
%defattr(-, root, root)
%{plymouth_libdir}/libply.so
%{plymouth_libdir}/libply-splash-core.so
%{_libdir}/libply-boot-client.so
%{_libdir}/libply-splash-graphics.so
%{_libdir}/pkgconfig/ply-splash-core.pc
%{_libdir}/pkgconfig/ply-splash-graphics.pc
%{_libdir}/pkgconfig/ply-boot-client.pc
%{_libdir}/plymouth/renderers/x11*
%{_includedir}/plymouth-1

%files core-libs
%defattr(-, root, root)
%{plymouth_libdir}/libply.so.*
%{plymouth_libdir}/libply-splash-core.so.*
%{_libdir}/libply-boot-client.so.*
%dir %{_libdir}/plymouth

%files graphics-libs
%defattr(-, root, root)
%{_libdir}/libply-splash-graphics.so.*

%files scripts
%defattr(-, root, root)
%{_sbindir}/plymouth-set-default-theme
%{_libexecdir}/plymouth/plymouth-update-initrd
%{_libexecdir}/plymouth/plymouth-generate-initrd
%{_libexecdir}/plymouth/plymouth-populate-initrd

%files plugin-label
%defattr(-, root, root)
%{_libdir}/plymouth/label.so

%files plugin-fade-throbber
%defattr(-, root, root)
%{_libdir}/plymouth/fade-throbber.so

%files theme-fade-in
%defattr(-, root, root)
%dir %{_datadir}/plymouth/themes/fade-in
%{_datadir}/plymouth/themes/fade-in/bullet.png
%{_datadir}/plymouth/themes/fade-in/entry.png
%{_datadir}/plymouth/themes/fade-in/lock.png
%{_datadir}/plymouth/themes/fade-in/star.png
%{_datadir}/plymouth/themes/fade-in/fade-in.plymouth

%files theme-spinner
%defattr(-, root, root)
%dir %{_datadir}/plymouth/themes/spinner
%{_datadir}/plymouth/themes/spinner/*.png
%{_datadir}/plymouth/themes/spinner/spinner.plymouth

%files plugin-throbgress
%defattr(-, root, root)
%{_libdir}/plymouth/throbgress.so

%files theme-spinfinity
%defattr(-, root, root)
%dir %{_datadir}/plymouth/themes/spinfinity
%{_datadir}/plymouth/themes/spinfinity/box.png
%{_datadir}/plymouth/themes/spinfinity/bullet.png
%{_datadir}/plymouth/themes/spinfinity/entry.png
%{_datadir}/plymouth/themes/spinfinity/lock.png
%{_datadir}/plymouth/themes/spinfinity/throbber-[0-3][0-9].png
%{_datadir}/plymouth/themes/spinfinity/spinfinity.plymouth

%files plugin-space-flares
%defattr(-, root, root)
%{_libdir}/plymouth/space-flares.so

%files theme-solar
%defattr(-, root, root)
%dir %{_datadir}/plymouth/themes/solar
%{_datadir}/plymouth/themes/solar/*.png
%{_datadir}/plymouth/themes/solar/solar.plymouth

%files plugin-two-step
%defattr(-, root, root)
%{_libdir}/plymouth/two-step.so

%files theme-charge
%defattr(-, root, root)
%dir %{_datadir}/plymouth/themes/charge
%{_datadir}/plymouth/themes/charge/*.png
%{_datadir}/plymouth/themes/charge/charge.plymouth

%files plugin-script
%defattr(-, root, root)
%{_libdir}/plymouth/script.so

%files theme-script
%defattr(-, root, root)
%dir %{_datadir}/plymouth/themes/script
%{_datadir}/plymouth/themes/script/*.png
%{_datadir}/plymouth/themes/script/script.script
%{_datadir}/plymouth/themes/script/script.plymouth

%files system-theme
%defattr(-, root, root)

%changelog
* Fri Jul 12 2024 Alex Brett <alex.brett@cloud.com> - 0.8.9-0.31.20140113.3
- Tweak RPM packaging to satisfy rpmlint

* Wed Jul 10 2024 Alex Brett <alex.brett@cloud.com> - 0.8.9-0.31.20140113.2
- CA-393520: Drop ship-label-plugin-in-initrd.patch as not required for XS, and
  causes warnings following removal of fontconfig

* Wed Jul 10 2024 Alex Brett <alex.brett@cloud.com> - 0.8.9-0.31.20140113.1
- Imported plymouth-0.89-0.31.20140113 from CentOS
