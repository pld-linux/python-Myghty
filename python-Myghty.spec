%define		fname	Myghty
Summary:	View/Controller Framework and Templating Engine
Summary(pl.UTF-8):	Środowisko obsługujące widok, kontroler oraz system szablonów WWW
Name:		python-%{fname}
Version:	1.2
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/M/Myghty/%{fname}-%{version}.tar.gz
# Source0-md5:	d35299a5e64d7d4ff5397d9c4b80f2cf
URL:		http://www.myghty.org/
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	python >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python-based template and view-controller framework derived from
HTML::Mason. Supports the full featureset of Mason, allowing
component-based web development with Python-embedded HTML, and
includes many new concepts and features not found in Mason.

%description -l pl.UTF-8
Przeznaczone dla języka Python środowisko widok-kontroler oraz system
szablonów. Wywodzi się z modułu HTML::Mason języka Perl. Obsługuje
wszystkie funkcje Masona, pozwalając na tworzenie modularnych
szablonów HTML z osadzonym kodem w Pythonie. Zawiera wiele idei i
możliwości nie obecnych w Masonie.

%prep
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/myghty
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
