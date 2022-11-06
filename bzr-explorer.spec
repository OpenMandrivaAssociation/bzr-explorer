Name:           bzr-explorer
Version:        1.3.0
Release:        3
Summary:        A GUI for Bazaar

Group:          Development/Other
License:        GPLv2
URL:            https://launchpad.net/bzr-explorer
Source0:        https://launchpad.net/%{name}/stable/%{version}/+download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

BuildArch:      noarch
BuildRequires:  pkgconfig(python2)
BuildRequires:  bzr
BuildRequires:  python-pkg-resources
BuildRequires:  python-paste
Requires:       bzr >= 2.1
Requires:	qbzr >= 0.18

%description
Bazaar Explorer is a desktop application for using the Bazaar Version Control 
System. It provides a high level interface to all commonly used features, 
launching "applets" from the QBzr plug-in to provide most of the 
functionality. Alternatively, the applets from the bzr-gtk plug-in 
can be used if it is installed. Bazaar Explorer runs on GNOME, KDE, 
Windows and Mac OS X.


%files 
%license COPYING.txt
%doc NEWS
%py_puresitedir/bzrlib/plugins/explorer/*
%py_puresitedir/explorer-%{version}-*.egg-info

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

