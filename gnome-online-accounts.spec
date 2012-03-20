Name:		gnome-online-accounts
Version:	3.3.92
Release:	1%{?dist}
Summary:	Provide online accounts information

Group:		System Environment/Libraries
License:	LGPLv2+
URL:		http://people.freedesktop.org/~david/gnome-online-accounts-3.1.0/
Source0:	http://download.gnome.org/sources/gnome-online-accounts/3.3/%{name}-%{version}.tar.xz

BuildRequires:	gtk3-devel glib2-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc intltool
BuildRequires:	webkitgtk3-devel json-glib-devel libgnome-keyring-devel
BuildRequires:	libnotify-devel rest-devel
# For autoreconf, if needed
# BuildRequires:	gnome-common automake autoconf libtool

%description
gnome-online-accounts provides interfaces so applications and
libraries in GNOME can access the user's online accounts.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
Requires:	gobject-introspection-devel

%description devel
The gnome-online-accounts-devel package contains libraries and header
files for developing applications that use gnome-online-accounts.

%prep
%setup -q

%build
%configure --disable-static --enable-gtk-doc --enable-facebook --enable-windows-live
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la $RPM_BUILD_ROOT/%{_libdir}/control-center-1/panels/*.la

%find_lang %{name}

%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%doc NEWS COPYING
%{_libdir}/girepository-1.0/Goa-1.0.typelib
%{_libdir}/libgoa-1.0.so.0
%{_libdir}/libgoa-1.0.so.0.0.0
%{_libdir}/libgoa-backend-1.0.so.0
%{_libdir}/libgoa-backend-1.0.so.0.0.0
%{_prefix}/libexec/goa-daemon
%{_datadir}/dbus-1/services/org.gnome.OnlineAccounts.service
%{_datadir}/icons/hicolor/*/apps/goa-*.png
%{_datadir}/man/man8/goa-daemon.8.gz

%files devel
%{_includedir}/goa-1.0/
%{_libdir}/libgoa-1.0.so
%{_libdir}/libgoa-backend-1.0.so
%{_datadir}/gir-1.0/Goa-1.0.gir
%{_libdir}/pkgconfig/goa-1.0.pc
%{_libdir}/pkgconfig/goa-backend-1.0.pc
%{_datadir}/gtk-doc/html/goa/

%changelog
* Tue Mar 20 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.3.92-1
- Update to 3.3.92

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Brian Pepple <bpepple@fedoraproject.org> - 3.3.0-2
- Enable Windows Live provider.

* Mon Dec 19 2011 Brian Pepple <bpepple@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0.
- Update source url.

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Wed Sep 28 2011 Ray <rstrode@redhat.com> - 3.2.0.1-1
- Update to 3.2.0.1

* Mon Sep 26 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.91-1
- Update to 3.1.91

* Tue Aug 30 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.90-1
- Update to 3.1.90

* Fri Jul 01 2011 Bastien Nocera <bnocera@redhat.com> 3.1.1-1
- Update to 3.1.1

* Tue Jun 14 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-3
- Add more necessary patches

* Tue Jun 14 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-2
- Update with review comments from Peter Robinson

* Mon Jun 13 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-1
- First version

