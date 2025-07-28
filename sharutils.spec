Name:       sharutils
Summary:    The GNU shar utilities for packaging and unpackaging shell archives
Version:    4.15.2
Release:    2
# The main code:                GPLv3+
# intl/dngettext.c:             LGPLv2+
# lib (gnulib):                 GPLv3+
# lib/md5.c:                    GPLv3+ and Public Domain
# libopts/file.c:               LGPLv3+ or BSD
# libopts/genshell.h:           LGPLv2+
# libopts/m4/libopts.m4:        GPLv3+
# doc/sharutils.texi:           GFDL
# src/uuencode.c:               GPLv3+ and BSD
## Not in the binary package
# ar-lib:                       GPLv2+
# config.rpath:                 FSFULLR
# INSTALL:                      FSFAPP
# install-sh:                   MIT
License:    GPLv3+ and (GPLv3+ and BSD) and (LGPLv3+ or BSD) and LGPLv2+ and Public Domain and GFDL
URL:        http://www.gnu.org/software/sharutils/
Source0:    sharutils-%{version}.tar.xz
# Pass compilation with -Werror=format-security, bug #1037323
Patch0:     %{name}-4.14.2-Pass-compilation-with-Werror-format-security.patch
# Fix CVE-2018-1000097 (a heap buffer overflow in find_archive()),
# bug #1548019,
# <http://lists.gnu.org/archive/html/bug-gnu-utils/2018-02/msg00004.html>
Patch1:     %{name}-4.15.2-Fix-a-heap-buffer-overflow-in-find_archive.patch
# Adapt bundled gnulib to glibc-2.28
Patch2:     %{name}-4.15.2-fflush-adjust-to-glibc-2.28-libio.h-removal.patch
# Fix building with GCC 10,
# <https://lists.gnu.org/archive/html/bug-gnu-utils/2020-01/msg00001.html>
Patch3:     %{name}-4.15.2-Fix-building-with-GCC-10.patch
# Fix building with GCC 10,
# <https://lists.gnu.org/archive/html/bug-gnu-utils/2020-01/msg00001.html>
Patch4:     %{name}-4.15.2-Do-not-include-lib-md5.c-into-src-shar.c.patch
# 1/3 Fix building with GCC 15, bug #2341343,
# <https://lists.gnu.org/archive/html/bug-gnu-utils/2025-03/msg00000.html>
Patch5:     %{name}-4.15.2-ISO-C23-Backport-stdbool.m4-from-gnulib-devel-0-52.2.patch
# 2/3 Fix building with GCC 15, bug #2341343,
Patch6:     %{name}-4.15.2-ISO-C23-Port-getcwd.m4-to-ISO-C23.patch
# 3/3 Fix building with GCC 15, bug #2341343,
Patch7:     %{name}-4.15.2-ISO-C23-Port-the-code-to-ISO-C23.patch
BuildRequires:  gettext

%description
The sharutils package contains the GNU shar utilities, a set of tools
for encoding and decoding packages of files (in binary or text format)
in a special plain text format called shell archives (shar).  This
format can be sent through e-mail (which can be problematic for regular
binary files).  The shar utility supports a wide range of capabilities
(compressing, uuencoding, splitting long files for multi-part
mailings, providing checksums), which make it very flexible at
creating shar files.  After the files have been sent, the unshar tool
scans mail messages looking for shar files.  Unshar automatically
strips off mail headers and introductory text and then unpacks the
shar files.

Install sharutils if you send binary files through e-mail.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
autoreconf
%configure --disable-static
%make_build

%install
%make_install

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir
chmod 644 AUTHORS ChangeLog COPYING NEWS README THANKS TODO

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README THANKS TODO
%{_bindir}/*
%doc %{_infodir}/*info*
%doc %{_mandir}/*/*
