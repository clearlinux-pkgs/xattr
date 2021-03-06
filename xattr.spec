#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xattr
Version  : 0.9.7
Release  : 40
URL      : https://files.pythonhosted.org/packages/c1/74/1ff659d6deb1d2d6babb9483171edfa330264ae2cbf005035bb7a77b07d2/xattr-0.9.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/c1/74/1ff659d6deb1d2d6babb9483171edfa330264ae2cbf005035bb7a77b07d2/xattr-0.9.7.tar.gz
Summary  : Python wrapper for extended filesystem attributes
Group    : Development/Tools
License  : MIT
Requires: xattr-bin = %{version}-%{release}
Requires: xattr-license = %{version}-%{release}
Requires: xattr-python = %{version}-%{release}
Requires: xattr-python3 = %{version}-%{release}
Requires: cffi
BuildRequires : buildreq-distutils3
BuildRequires : cffi

%description
Extended attributes extend the basic attributes of files and directories
in the file system.  They are stored as name:data pairs associated with
file system objects (files, directories, symlinks, etc).

Extended attributes are currently only available on Darwin 8.0+ (Mac OS X 10.4)
and Linux 2.6+. Experimental support is included for Solaris and FreeBSD.

%package bin
Summary: bin components for the xattr package.
Group: Binaries
Requires: xattr-license = %{version}-%{release}

%description bin
bin components for the xattr package.


%package license
Summary: license components for the xattr package.
Group: Default

%description license
license components for the xattr package.


%package python
Summary: python components for the xattr package.
Group: Default
Requires: xattr-python3 = %{version}-%{release}

%description python
python components for the xattr package.


%package python3
Summary: python3 components for the xattr package.
Group: Default
Requires: python3-core
Provides: pypi(xattr)

%description python3
python3 components for the xattr package.


%prep
%setup -q -n xattr-0.9.7
cd %{_builddir}/xattr-0.9.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582901875
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xattr
cp %{_builddir}/xattr-0.9.7/LICENSE.txt %{buildroot}/usr/share/package-licenses/xattr/36073575ee7f723a03044c63ea17697f848b2e77
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xattr

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xattr/36073575ee7f723a03044c63ea17697f848b2e77

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
