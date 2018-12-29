#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xattr
Version  : 0.9.6
Release  : 32
URL      : https://files.pythonhosted.org/packages/60/80/a1f35bfd3c7ffb78791b2a6a15c233584a102a20547fd96d48933ec453e7/xattr-0.9.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/60/80/a1f35bfd3c7ffb78791b2a6a15c233584a102a20547fd96d48933ec453e7/xattr-0.9.6.tar.gz
Summary  : Python wrapper for extended filesystem attributes
Group    : Development/Tools
License  : MIT
Requires: xattr-bin
Requires: xattr-python3
Requires: xattr-license
Requires: xattr-python
Requires: cffi
BuildRequires : buildreq-distutils3
BuildRequires : cffi

%description
Extended attributes extend the basic attributes of files and directories

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

%description python3
python3 components for the xattr package.


%prep
%setup -q -n xattr-0.9.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537395615
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/xattr
cp LICENSE.txt %{buildroot}/usr/share/doc/xattr/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xattr

%files license
%defattr(-,root,root,-)
/usr/share/doc/xattr/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
