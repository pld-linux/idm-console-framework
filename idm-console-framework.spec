%define		major_version	1.1
Summary:	Identity Management Console Framework
Summary(pl.UTF-8):	Framework konsoli zarządzania tożsamościami
Name:		idm-console-framework
Version:	1.1.1
Release:	0.2
License:	LGPL
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	a23291c9aea256f075b69df981fae42a
URL:		http://directory.fedoraproject.org/wiki/BuildingConsole
BuildRequires:	ant >= 1.6
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	jss >= 3.3
BuildRequires:	ldapsdk >= 4.17
BuildRequires:	rpmbuild(macros) >= 1.294
Requires:	jre
Requires:	jss >= 3.3
Requires:	ldapsdk >= 4.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Java Management Console framework used for remote server management.

%prep
%setup -q

%build
%ant \
	-Dbuilt.dir="`pwd`/built" \
	-Djss.local.location=%{_javadir} \
	-Dlib.dir=%{_libdir} \
	-Dclassdest=%{_javadir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install built/release/jars/idm-console-* $RPM_BUILD_ROOT%{_javadir}

cd $RPM_BUILD_ROOT%{_javadir}
ln -s idm-console-base-%{version}.jar idm-console-base-%{major_version}.jar
ln -s idm-console-base-%{version}.jar idm-console-base.jar
ln -s idm-console-mcc-%{version}.jar idm-console-mcc-%{major_version}.jar
ln -s idm-console-mcc-%{version}.jar idm-console-mcc.jar
ln -s idm-console-mcc-%{version}_en.jar idm-console-mcc-%{major_version}_en.jar
ln -s idm-console-mcc-%{version}_en.jar idm-console-mcc_en.jar
ln -s idm-console-nmclf-%{version}.jar idm-console-nmclf-%{major_version}.jar
ln -s idm-console-nmclf-%{version}.jar idm-console-nmclf.jar
ln -s idm-console-nmclf-%{version}_en.jar idm-console-nmclf-%{major_version}_en.jar
ln -s idm-console-nmclf-%{version}_en.jar idm-console-nmclf_en.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*
