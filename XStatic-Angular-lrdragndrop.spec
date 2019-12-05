#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Angular-lrdragndrop
Version  : 1.0.2.4
Release  : 18
URL      : https://files.pythonhosted.org/packages/58/0a/922a53c43903ca88ea172a26057688fe8b83c9a20323dc6769951db12fd4/XStatic-Angular-lrdragndrop-1.0.2.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/58/0a/922a53c43903ca88ea172a26057688fe8b83c9a20323dc6769951db12fd4/XStatic-Angular-lrdragndrop-1.0.2.4.tar.gz
Summary  : Angular-lrdragndrop 1.0.2 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-Angular-lrdragndrop-python = %{version}-%{release}
Requires: XStatic-Angular-lrdragndrop-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
---------------------------
        
        lrDragNDrop javascript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package
        `XStatic`.

%package python
Summary: python components for the XStatic-Angular-lrdragndrop package.
Group: Default
Requires: XStatic-Angular-lrdragndrop-python3 = %{version}-%{release}
Provides: xstatic-angular-lrdragndrop-python

%description python
python components for the XStatic-Angular-lrdragndrop package.


%package python3
Summary: python3 components for the XStatic-Angular-lrdragndrop package.
Group: Default
Requires: python3-core

%description python3
python3 components for the XStatic-Angular-lrdragndrop package.


%prep
%setup -q -n XStatic-Angular-lrdragndrop-1.0.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570210914
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
