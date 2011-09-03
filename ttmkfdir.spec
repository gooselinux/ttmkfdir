Summary: Utility to create fonts.scale files for truetype fonts
Name: ttmkfdir
Version: 3.0.9
Release: 32.1%{?dist}
# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
Source0: %{name}-%{version}.tar.bz2
Patch: ttmkfdir-3.0.9-cpp.patch
Patch1: ttmkfdir-3.0.9-zlib.patch
Patch2: ttmkfdir-3.0.9-fix-freetype217.patch
Patch3: ttmkfdir-3.0.9-namespace.patch
Patch4: ttmkfdir-3.0.9-fix-crash.patch
Patch5: ttmkfdir-3.0.9-warnings.patch
Patch6: ttmkfdir-3.0.9-segfaults.patch
Patch7: ttmkfdir-3.0.9-encoding-dir.patch
Patch8: ttmkfdir-3.0.9-font-scale.patch
Patch9: ttmkfdir-3.0.9-bug434301.patch
# Only licensing attribution is in README, no version.
License: LGPLv2+
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: freetype-devel >= 2.0
BuildRequires: zlib-devel flex
BuildRequires: libtool

# ttmkfdir used to be in the following packages at one point
Conflicts: XFree86-font-utils < 4.2.99.2-0.20021126.3
Conflicts: freetype < 2.0.6-3

%description
ttmkfdir is a utility used to create fonts.scale files in
TrueType font directories in order to prepare them for use
by the font server.

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
make OPTFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/ttmkfdir

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.0.9-32.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Jens Petersen <petersen@redhat.com> - 3.0.9-31
- simplify ttmkfdir-3.0.9-encoding-dir.patch to drop X11R6/ check (#173705)

* Tue Mar 03 2009 Caolán McNamara <caolanm@redhat.com> - 3.0.9-30
- fix ttmkfdir-3.0.9-segfaults.patch to include stdio.h for added printf

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Pravin Satpute <psatpute@redhat.com> - 3.0.9-28
- modified spec file as per merge review suggestions bug 226506

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.0.9-27
- fix license tag

* Wed Feb 27 2008 Lingning Zhang <lizhang@redhat.com> - 3.0.9-26
- fix bug434301.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.0.9-25
- Autorebuild for GCC 4.3

* Thu Nov 30 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-24.fc7
- add ttmkfdir-3.0.9-font-scale.patch to fix bug #209102.
- Patch from Akira TAGOH.

* Wed Oct 18 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-23
- rebuild

* Fri Sep 29 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-22
- delete "%%post" and "Requires(post)" in ttmkfdir.spec

* Thu Sep 28 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-21
- modify release

* Wed Sep 27 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-20.4
- modify "%%post" and add "Requires(post)" in ttmkfdir.spec for fixing bug173591, bug207279, bug208122

* Wed Sep 06 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-20.3
- add "%%post" in ttmkfdir.spec for fixing bug173591

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.0.9-20.2.1
- rebuild

* Tue Jun 20 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-20.2
- add "BuildRequires: libtool" in ttmkfdir.spec

* Mon Jun 19 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-20.1
- remove the modifying part of ttmkfdir-3.0.9/Makefile, recover the old Makefile
- modify ttmkfdir-3.0.9-encoding-dir.patch about Makefile

* Thu Jun 15 2006 Lingning Zhang <lizhang@redhat.com> - 3.0.9-20
- add ttmkfdir-3.0.9-encoding-dir.patch to fix bug #173705
- modify ttmkfdir-3.0.9/Makefile to delete the compiling flag of "ggdb"

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.0.9-19.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.0.9-19.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Oct 8 2005 LingNing Zhang <lizhang@redhat.com> -3.0.9-19
- add ttmkfdir-3.0.9-segfaults.patch to fix bug #164969

* Wed Aug  3 2005 Jens Petersen <petersen@redhat.com> - 3.0.9-17
- replace ttmkfdir-3.0.9-defautl_enc_size.patch and
  ttmkfdir-3.0.9-crashplus.patch with ttmkfdir-3.0.9-fix-crash.patch
  to fix missing native encodings of fonts
  (Akira Tagoh, #143941)
- buildrequire flex
- add ttmkfdir-3.0.9-warnings.patch to silence most of compiler warnings

* Sun Mar 20 2005 Yu Shao <yshao@redhat.com> 3.0.9-16
- rebuild with GCC 4

* Fri Sep 10 2004 Yu Shao <yshao@redhat.com> 3.0.9-14
- bug #100560, requires zlib-devel rather than zlib

* Tue Aug 17 2004 Elliot Lee <sopwith@redhat.com> 3.0.9-13
- Follow-on fix for the issue detailed in #118713
- Improve performance when checking if a font has a mapping present
- Base font file selection on the magic at the start of the file, rather than the filename

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Mar 19 2004 Yu Shao <yshao@redhat.com> 3.0.9-11
- set default encoding size to DEFAULT_SIZE, bug #118713

* Fri Mar 12 2004 Yu Shao <yshao@redhat.com> 3.0.9-10
- patch suggested from law@redhat.com not to use semicolon in GCC3.4, 3.5

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 12 2004 Yu Shao <yshao@redhat.com> 3.0.9-8
- patch for building package against freetype-2.1.7
- from kanagawa jigorou (jigorou3@mail.goo.ne.jp) #114682

* Mon Sep 15 2003 Yu Shao <yshao@redhat.com> 3.0.9-6
- updated zlib patch from Nalin Dahyabhai #104331

* Thu Aug 21 2003 Yu Shao <yshao@redhat.com> 3.0.9-4
- added zlib build requirement, partly releated to #100560
- other fixes

* Thu Aug  7 2003 Elliot Lee <sopwith@redhat.com>
- Fix compile error (cpp.patch)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 23 2003 Yu Shao <yshao@redhat.com> 3.0.9-1
- added freetype-devel build requirement #82468

* Mon Jan 20 2003 Yu Shao <yshao@redhat.com> 3.0.8-1
- revert additional-entries to 0 #82125

* Wed Jan 15 2003 Yu Shao <yshao@redhat.com> 3.0.7-1
- set default value of additional-entries to 1

* Mon Jan 13 2003 Yu Shao <yshao@redhat.com> 3.0.6-1
- added iso8859-13 support from Nerijus Baliunas #77289
- added README 

* Wed Jan 8 2003 Yu Shao <yshao@redhat.com> 3.0.5-1
- encoding.l fix and ttc support patch 
- default read system encodings.dir instead of the one
- in current directory

* Wed Dec 18 2002 Yu Shao <yshao@redhat.com> 3.0.4-1
- make ttmkfdir keep silent with FIRSTINDEX. #61769

* Wed Dec 18 2002 Yu Shao <yshao@redhat.com> 3.0.3-1
- Applied new patches to make ttmkfdir provide more infomation when meets 
- bad fonts

* Mon Dec  9 2002 Mike A. Harris <mharris@devel.capslock.lan> 3.0.2-1
- Changed the nonstandard RPM Group from System/Utilities to Applications/System
- Added a new Makefile install target, and changed specfile to use makeinstall

* Mon Dec  9 2002 Mike A. Harris <mharris@devel.capslock.lan> 3.0.1-1
- Imported ttmkfdir into CVS on cvs.devel and applied all patches to CVS
- Removed patches from spec file
- Rewrote Makefile, now uses freetype-config to autodetect CFLAGS and libs,
  allowing a lot of spec file cleanups.  Added new targets for tagging CVS,
  making tarball, and making srpm.

* Mon Dec  2 2002 Mike A. Harris <mharris@devel.capslock.lan> 3.0.0-2
- Added Conflicts for prior packages which contained ttmkfdir

* Fri Nov 29 2002 Mike A. Harris <mharris@devel.capslock.lan> 3.0.0-1
- Initial build.  Basically just renamed our existing ttmkfdir to version
  3.0.0 to differentiate it.  It's the same old thing as before, but is
  likely going to move to CVS for easier development.
