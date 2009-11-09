Name:           bzr-explorer
Version:        0.9.0
Release:        %mkrel 2
Summary:        A GUI for Bazaar

Group:          Development/Other
License:        GPL
URL:            https://launchpad.net/bzr-explorer
Source0:        https://launchpad.net/%{name}/stable/%{version}/+download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

BuildArch:      noarch
BuildRequires:  python-devel 
BuildRequires:  bzr
BuildRequires:  python-pkg-resources
BuildRequires:	python-paste
Requires:       bzr >= 1.14
Requires:	qbzr >= 0.11

%description
Bazaar Explorer is a desktop application for using the Bazaar Version Control System. It provides a 
high level interface to all commonly used features, launching "applets" from the QBzr plug-in to 
provide most of the functionality. Alternatively, the applets from the bzr-gtk plug-in can be used 
if it is installed. Bazaar Explorer runs on GNOME, KDE, Windows and Mac OS X. It requires 
Bazaar 1.14 or later and QBzr 0.11 or later.

%prep
%setup -q -n %{name}-%{version}


%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --prefix=%{buildroot}/%_prefix

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%dir %py_puresitedir/bzrlib/plugins/explorer
%py_puresitedir/bzrlib/plugins/explorer/*
%py_puresitedir/explorer-%{version}-py2.6.egg-info
%doc NEWS COPYING.txt

