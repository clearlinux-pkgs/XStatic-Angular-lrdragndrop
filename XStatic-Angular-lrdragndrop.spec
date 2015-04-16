#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Angular-lrdragndrop
Version  : 1.0.2.2
Release  : 4
URL      : https://pypi.python.org/packages/source/X/XStatic-Angular-lrdragndrop/XStatic-Angular-lrdragndrop-1.0.2.2.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-Angular-lrdragndrop/XStatic-Angular-lrdragndrop-1.0.2.2.tar.gz
Summary  : Angular-lrdragndrop 1.0.2 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-Angular-lrdragndrop-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-Angular-lrdragndrop
-------------------
lrDragNDrop javascript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-Angular-lrdragndrop package.
Group: Default
Provides: xstatic-angular-lrdragndrop-python

%description python
python components for the XStatic-Angular-lrdragndrop package.


%prep
%setup -q -n XStatic-Angular-lrdragndrop-1.0.2.2

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
