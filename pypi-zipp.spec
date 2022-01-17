#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-zipp
Version  : 3.7.0
Release  : 42
URL      : https://files.pythonhosted.org/packages/94/64/3115548d41cb001378099cb4fc6a6889c64ef43ac1b0e68c9e80b55884fa/zipp-3.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/94/64/3115548d41cb001378099cb4fc6a6889c64ef43ac1b0e68c9e80b55884fa/zipp-3.7.0.tar.gz
Summary  : Backport of pathlib-compatible object wrapper for zip files
Group    : Development/Tools
License  : MIT
Requires: pypi-zipp-license = %{version}-%{release}
Requires: pypi-zipp-python = %{version}-%{release}
Requires: pypi-zipp-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://img.shields.io/pypi/v/zipp.svg
:target: `PyPI link`_
.. image:: https://img.shields.io/pypi/pyversions/zipp.svg
:target: `PyPI link`_

%package license
Summary: license components for the pypi-zipp package.
Group: Default

%description license
license components for the pypi-zipp package.


%package python
Summary: python components for the pypi-zipp package.
Group: Default
Requires: pypi-zipp-python3 = %{version}-%{release}

%description python
python components for the pypi-zipp package.


%package python3
Summary: python3 components for the pypi-zipp package.
Group: Default
Requires: python3-core
Provides: pypi(zipp)

%description python3
python3 components for the pypi-zipp package.


%prep
%setup -q -n zipp-3.7.0
cd %{_builddir}/zipp-3.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642463943
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zipp
cp %{_builddir}/zipp-3.7.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-zipp/8e6689d37f82d5617b7f7f7232c94024d41066d1
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zipp/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
