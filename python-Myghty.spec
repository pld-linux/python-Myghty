%define 	module	        myghty
%define     fname           Myghty
%define     python_version  2.4
Summary:	View/Controller Framework and Templating Engine
Summary(pl):	Środowisko obsługujące widok, kontroler oraz system szablonów WWW
Name:		python-%{fname}
Version:	1.1
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:    http://cheeseshop.python.org/packages/source/M/%{fname}/%{fname}-%{version}.tar.gz
# Source0-md5:   5865361811dca4054f1ec60ac32ee965
URL:		http://www.myghty.org/
BuildRequires:  python-setuptools
Requires:	python >= %{python_version}
Requires:   python-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python-based template and view-controller framework derived from
HTML::Mason. Supports the full featureset of Mason, allowing component-based
web development with Python-embedded HTML, and includes many new concepts and
features not found in Mason.

%description -l pl
Przeznaczone dla języka Python Środowisko obsługujące model i kontroler oraz
system szablonów. Oparte na module HTML::Mason języka Perl. Obsługuje
wszystkie funkcje Masona, pozwalając na tworzenie modularnych szablonów HTML z
osadzonym kodem w Pythonie.

%prep
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{fname}-%{version}-py%{python_version}.egg-info
