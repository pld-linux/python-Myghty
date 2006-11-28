%define		fname	Myghty
Summary:	View/Controller Framework and Templating Engine
Summary(pl):	¦rodowisko obs³uguj±ce widok, kontroler oraz system szablonów WWW
Name:		python-%{fname}
Version:	1.1
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/M/Myghty/%{fname}-%{version}.tar.gz
# Source0-md5:	5865361811dca4054f1ec60ac32ee965
URL:		http://www.myghty.org/
BuildRequires:	python-setuptools
BuildRequires:	python >= 1:2.5
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python-based template and view-controller framework derived from
HTML::Mason. Supports the full featureset of Mason, allowing
component-based web development with Python-embedded HTML, and
includes many new concepts and features not found in Mason.

%description -l pl
Przeznaczone dla jêzyka Python ¶rodowisko widok-kontroler oraz system
szablonów. Wywodzi siê z modu³u HTML::Mason jêzyka Perl. Obs³uguje
wszystkie funkcje Masona, pozwalaj±c na tworzenie modularnych
szablonów HTML z osadzonym kodem w Pythonie. Zawiera wiele idei i
mo¿liwo¶ci nie obecnych w Masonie.

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
%{py_sitescriptdir}/myghty
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
