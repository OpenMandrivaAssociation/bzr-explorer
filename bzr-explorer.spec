Name:           bzr-explorer
Version:        1.3.0
Release:        1
Summary:        A GUI for Bazaar

Group:          Development/Other
License:        GPLv2
URL:            https://launchpad.net/bzr-explorer
Source0:        https://launchpad.net/%{name}/stable/%{version}/+download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

BuildArch:      noarch
BuildRequires:  python-devel 
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

%prep
%setup -q 


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
%py_puresitedir/explorer-%{version}-*.egg-info
%doc NEWS COPYING.txt



%changelog
* Sat Sep 01 2012 Crispin Boylan <crisb@mandriva.org> 1.3.0-1
+ Revision: 816163
- New release

* Wed Feb 29 2012 Crispin Boylan <crisb@mandriva.org> 1.2.2-1
+ Revision: 781437
- New release

* Sun Aug 07 2011 Crispin Boylan <crisb@mandriva.org> 1.2.1-1
+ Revision: 693586
- New release

* Thu May 12 2011 Crispin Boylan <crisb@mandriva.org> 1.1.3-1
+ Revision: 673744
- New release

* Tue Nov 30 2010 Crispin Boylan <crisb@mandriva.org> 1.1.2-1mdv2011.0
+ Revision: 603321
- New release

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 1.1.1-2mdv2011.0
+ Revision: 591771
- Fix egg-info location
- Rebuild
- New release

* Sat Oct 02 2010 Crispin Boylan <crisb@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 582490
- New release

* Sun Jun 27 2010 Crispin Boylan <crisb@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 549206
- New release

* Wed Mar 10 2010 Crispin Boylan <crisb@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 517599
- New release

* Fri Mar 05 2010 Crispin Boylan <crisb@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 514792
- Release 1.0.0

* Fri Feb 05 2010 Crispin Boylan <crisb@mandriva.org> 0.11.2-1mdv2010.1
+ Revision: 501106
- New release

* Wed Dec 30 2009 Crispin Boylan <crisb@mandriva.org> 0.10.0-1mdv2010.1
+ Revision: 483833
- New release

* Mon Nov 09 2009 Crispin Boylan <crisb@mandriva.org> 0.9.0-2mdv2010.1
+ Revision: 463709
- Bump
- Wrap description

* Sun Nov 08 2009 Crispin Boylan <crisb@mandriva.org> 0.9.0-1mdv2010.1
+ Revision: 462858
- New release

* Sat Oct 17 2009 Crispin Boylan <crisb@mandriva.org> 0.8.3-1mdv2010.0
+ Revision: 457994
- New release

* Sat Sep 26 2009 Crispin Boylan <crisb@mandriva.org> 0.8.2-1mdv2010.0
+ Revision: 449405
- 0.8.2
- create bzr-explorer

