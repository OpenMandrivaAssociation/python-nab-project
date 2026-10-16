%define module nab_project

Name:		python-nab-project
Version:	0.0.21
Release:	1
Summary:	Index-backed provider, lockfile emitter, and downloader for nab
License:	MIT
Group:		Development/Python
URL:		https://github.com/notatallshaw/nab
Source0:	https://files.pythonhosted.org/packages/source/n/nab-project/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)

%description
Project and lockfile support for nab.
pipdeptree 4 imports this package when it builds a dependency tree.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
