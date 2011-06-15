Name:		gnome-online-accounts
Version:	3.1.0
Release:	3%{?dist}
Summary:	Provide online accounts information

Group:		System Environment/Libraries
License:	LGPLv2+
URL:		http://people.freedesktop.org/~david/gnome-online-accounts-3.1.0/
Source0:	http://people.freedesktop.org/~david/%{name}-%{version}.tar.bz2

BuildRequires:	gtk3-devel glib2-devel
BuildRequires:	control-center-devel gobject-introspection-devel
BuildRequires:	gnome-common automake autoconf libtool intltool
BuildRequires:	gtk-doc
BuildRequires:	webkitgtk3-devel json-glib-devel libgnome-keyring-devel
BuildRequires:	libnotify-devel rest-devel

Patch0:		0001-Don-t-version-the-panel-plugin.patch
Patch1:		0001-Fix-.desktop-file-s-validity.patch
Patch2:		0001-Fix-panel-UI-file-loading.patch

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
%patch0 -p1 -b .version
%patch1 -p1 -b .desktop
%patch2 -p1 -b .ui-file
autoreconf -f

%build
%configure --disable-static --enable-gtk-doc
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la $RPM_BUILD_ROOT/%{_libdir}/control-center-1/panels/*.la

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

%files
%defattr(-,root,root,-)
%doc NEWS COPYING
%{_libdir}/control-center-1/panels/libgoa-panel.so
%{_libdir}/girepository-1.0/Goa-1.0.typelib
%{_libdir}/libgoa-1.0.so.0
%{_libdir}/libgoa-1.0.so.0.0.0
%{_libdir}/libgoa-backend-1.0.so.0
%{_libdir}/libgoa-backend-1.0.so.0.0.0
%{_prefix}/libexec/goa-daemon
%{_datadir}/applications/goa-prefs.desktop
%{_datadir}/dbus-1/services/org.gnome.OnlineAccounts.service
%{_datadir}/gnome-online-accounts/goapanel.ui
%{_datadir}/icons/hicolor/*/apps/goa-*.png
%{_mandir}/man8/goa-daemon.8.gz

%files devel
%defattr(-,root,root,-)
%{_includedir}/goa-1.0/
%{_libdir}/libgoa-1.0.so
%{_libdir}/libgoa-backend-1.0.so
%{_datadir}/gir-1.0/Goa-1.0.gir
%{_libdir}/pkgconfig/goa-1.0.pc
%{_libdir}/pkgconfig/goa-backend-1.0.pc
%{_datadir}/gtk-doc/html/goa/

%changelog
* Tue Jun 14 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-3
- Add more necessary patches

* Tue Jun 14 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-2
- Update with review comments from Peter Robinson

* Mon Jun 13 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-1
- First version

