#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests [require dbus and some Secret Service daemon running]
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 bindings to Freedesktop.org Secret Service API
Summary(pl.UTF-8):	Wiązania Pythona 2 do API Secret Service z Freedesktop.org
Name:		python-secretstorage
Version:	2.1.4
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/secretstorage
Source0:	https://pypi.python.org/packages/c9/b0/833d13a07319ff9b9815d1683c5ece719f6e467b8217c1c6a42bc37a3aa9/SecretStorage-%{version}.tar.gz
# Source0-md5:	80ca4a4a0614daf45ee3d0fb17eb41cd
URL:		https://github.com/mitya57/secretstorage
BuildRequires:	rpm-pythonprov
# for the py_build, py_install macros
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with doc}
BuildRequires:	python3-Sphinx
%endif
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a way for securely storing passwords and other
secrets.

It uses D-Bus Secret Service API that is supported by GNOME Keyring
(since version 2.30) and KSecretsService.

%description -l pl.UTF-8
Ten moduł udostępnia sposób bezpiecznego przechowywania haseł i innych
tajnych danych.

Wykorzystuje API D-Bus Secret Service, obsługiwane przez GNOME Keyring
(od wersji 2.30) oraz KSecretsService.

%package -n python3-secretstorage
Summary:	Python 3 bindings to Freedesktop.org Secret Service API
Summary(pl.UTF-8):	Wiązania Pythona 3 do API Secret Service z Freedesktop.org
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-secretstorage
This module provides a way for securely storing passwords and other
secrets.

It uses D-Bus Secret Service API that is supported by GNOME Keyring
(since version 2.30) and KSecretsService.

%description -n python3-secretstorage -l pl.UTF-8
Ten moduł udostępnia sposób bezpiecznego przechowywania haseł i innych
tajnych danych.

Wykorzystuje API D-Bus Secret Service, obsługiwane przez GNOME Keyring
(od wersji 2.30) oraz KSecretsService.

%package apidocs
Summary:	secretstorage API documentation
Summary(pl.UTF-8):	Dokumentacja API secretstorage
Group:		Documentation

%description apidocs
API documentation for secretstorage.

%description apidocs -l pl.UTF-8
Dokumentacja API secretstorage.

%prep
%setup -q -n SecretStorage-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}

%if %{with tests}
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build %{?with_tests:test} %{?with_doc:build_sphinx}

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst changelog
%{py_sitescriptdir}/secretstorage
%{py_sitescriptdir}/SecretStorage-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-secretstorage
%defattr(644,root,root,755)
%doc LICENSE README.rst changelog
%{py3_sitescriptdir}/secretstorage
%{py3_sitescriptdir}/SecretStorage-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc build-3/sphinx/html/{_modules,_static,*.html,*.js}
%endif
