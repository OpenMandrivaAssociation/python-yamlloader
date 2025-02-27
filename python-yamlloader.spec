Name:		python-yamlloader
Version:	1.5.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/y/yamlloader/yamlloader-%{version}.tar.gz
Summary:	Ordered YAML loader and dumper for PyYAML.
URL:		https://pypi.org/project/yamlloader/
License:	BSD
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildSystem:	python
BuildArch:	noarch

%description
Ordered YAML loader and dumper for PyYAML.

%files
%{py_sitedir}/yamlloader
%{py_sitedir}/yamlloader-*.*-info
