%define module yamlloader

Name:		python-yamlloader
Version:	1.6.0
Release:	1
Summary:	Ordered YAML loader and dumper for PyYAML.
License:	BSD
Group:		Development/Python
URL:		https://pypi.org/project/yamlloader/
Source0:	https://files.pythonhosted.org/packages/source/y/%{module}/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)

%description
Ordered YAML loader and dumper for PyYAML.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
