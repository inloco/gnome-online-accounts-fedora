Name:		gnome-online-accounts
Version:	3.19.2
Release:	1%{?dist}
Summary:	Single sign-on framework for GNOME

Group:		System Environment/Libraries
License:	LGPLv2+
URL:		https://wiki.gnome.org/Projects/GnomeOnlineAccounts
Source0:	http://download.gnome.org/sources/gnome-online-accounts/3.19/%{name}-%{version}.tar.xz

BuildRequires:	gcr-devel
BuildRequires:	glib2-devel >= 2.35
BuildRequires:	gtk3-devel >= 3.5.1
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	krb5-devel
BuildRequires:	webkitgtk4-devel
BuildRequires:	json-glib-devel
BuildRequires:	libsecret-devel >= 0.7
BuildRequires:	libsoup-devel >= 2.41
BuildRequires:	rest-devel
BuildRequires:	telepathy-glib-devel
BuildRequires:	libxml2-devel

Requires:	realmd

%description
GNOME Online Accounts provides interfaces so that applications and libraries
in GNOME can access the user's online accounts. It has providers for Google,
ownCloud, Facebook, Flickr, Windows Live, Pocket, Microsoft Exchange,
IMAP/SMTP, Jabber, SIP and Kerberos.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	gobject-introspection-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure \
  --disable-static \
  --enable-gtk-doc \
  --enable-exchange \
  --enable-facebook \
  --enable-flickr \
  --enable-foursquare \
  --enable-google \
  --enable-imap-smtp \
  --enable-kerberos \
  --enable-owncloud \
  --enable-pocket \
  --enable-telepathy \
  --enable-windows-live
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete

%find_lang %{name}
%find_lang %{name}-tpaw

%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang -f %{name}-tpaw.lang
%license COPYING
%doc COPYING
%{_libdir}/girepository-1.0/Goa-1.0.typelib
%{_libdir}/libgoa-1.0.so.0
%{_libdir}/libgoa-1.0.so.0.0.0
%{_libdir}/libgoa-backend-1.0.so.1
%{_libdir}/libgoa-backend-1.0.so.1.0.0
%dir %{_libdir}/goa-1.0
%dir %{_libdir}/goa-1.0/web-extensions
%{_libdir}/goa-1.0/web-extensions/libgoawebextension.so
%{_prefix}/libexec/goa-daemon
%{_prefix}/libexec/goa-identity-service
%{_datadir}/dbus-1/services/org.gnome.OnlineAccounts.service
%{_datadir}/dbus-1/services/org.gnome.Identity.service
%{_datadir}/icons/hicolor/*/apps/goa-*.png
%{_datadir}/icons/hicolor/*/apps/im-*.png
%{_datadir}/icons/hicolor/*/apps/im-*.svg
%{_datadir}/man/man8/goa-daemon.8.gz
%{_datadir}/glib-2.0/schemas/org.gnome.online-accounts.gschema.xml

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/irc-networks.xml

%files devel
%{_includedir}/goa-1.0/
%{_libdir}/libgoa-1.0.so
%{_libdir}/libgoa-backend-1.0.so
%{_datadir}/gir-1.0/Goa-1.0.gir
%{_libdir}/pkgconfig/goa-1.0.pc
%{_libdir}/pkgconfig/goa-backend-1.0.pc
%{_datadir}/gtk-doc/html/goa/
%{_libdir}/goa-1.0/include

%changelog
* Wed Nov 25 2015 Kalev Lember <klember@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Wed Oct 28 2015 Kalev Lember <klember@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Wed Oct 14 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0
- Use make_install macro

* Wed Sep 16 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.17.92.1-1
- Update to 3.17.92.1

* Tue Sep 15 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.17.92-1
- Update to 3.17.92

* Wed Sep 09 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.17.91-1
- Update to 3.17.91

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.17.2-1
- Update to 3.17.2

* Tue May 12 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Thu Apr 30 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.16.0-2
- Enable Foursquare

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Wed Mar 04 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91
- Use the %%license macro for the COPYING file

* Mon Feb 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.90-1
- Update to 3.15.90

* Mon Jan 19 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.15.4-1
- Update to 3.15.4

* Fri Dec 19 2014 Richard Hughes <rhughes@redhat.com> - 3.15.3-1
- Update to 3.15.3

* Wed Nov 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.2-1
- Update to 3.15.2

* Wed Nov 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.1-1
- Update to 3.15.1

* Wed Nov 12 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Thu Oct 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Wed Sep 03 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.3-3
- Rebuilt for gobject-introspection 1.41.4

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2

* Thu May 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-1
- Update to 3.13.1

* Wed Apr 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Tue Apr 01 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.12.0-2
- Popup is too small to display Facebook authorization (GNOME #726609)

* Tue Mar 25 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.11.92-1
- Update to 3.11.92

* Sat Mar 08 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Tue Feb 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Wed Jan 15 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Wed Dec 18 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.11.3-1
- Update to 3.11.3

* Mon Nov 25 2013 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Tue Nov 12 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.10.2-1
- Update to 3.10.2

* Fri Oct 18 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.10.1-2
- Adapt to changes in the redirect URI used by Facebook (GNOME #710363)

* Wed Oct 16 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Tue Oct 08 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.10.0-3
- Add a Requires on realmd (Red Hat #949741)

* Fri Sep 27 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.10.0-2
- Fix GNOME #708462 and #708832

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Thu Aug 29 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-2
- Update to new webkitgtk-2.1.90 API

* Thu Aug 22 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.9.4-1
- Update to 3.9.4
- Update summary and description to match upstream DOAP file

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.2-1
- Update to 3.9.2

* Sat May 04 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.1-1
- Update to 3.9.1

* Mon Apr 15 2013 Richard Hughes <rhughes@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Tue Mar 05 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.7.91-1
- Update to 3.7.91

* Tue Feb 26 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.7.90-2
- Enable IMAP / SMTP

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 06 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.7.5-1
- Update to 3.7.5

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.4-2
- Rebuilt for libgcr soname bump

* Mon Jan 14 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.7.4-1
- Update to 3.7.4

* Thu Jan 03 2013 Debarshi Ray <rishi@fedoraproject.org> - 3.7.3-1
- Update to 3.7.3

* Sun Nov 18 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.7.2-1
- Update to 3.7.2

* Tue Oct 23 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1

* Mon Oct 15 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Mon Sep 17 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.90-1
- Update to 3.5.90

* Tue Aug 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.5-1
- Update to 3.5.5

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.4-1
- Update to 3.5.4

* Mon Jun 25 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.3-1
- Update to 3.5.3

* Tue Jun 05 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2

* Wed May 02 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1

* Tue Apr 17 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Mon Mar 26 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.3.92.1-1
- Update to 3.3.92.1

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

