%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
Summary:	Ruby GUID Library
Name:		ruby-guid
Version:	0.0.1
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/378/%{name}-%{version}.tar.gz
# Source0-md5:	10f50564c198db7ba0b592149f90cc52
URL:		http://rubyforge.org/projects/uuid/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
#BuildArch: noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby implementation of the IEEE GUID spec.

%prep
%setup -q

%build

ruby install.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby install.rb setup

rdoc -o rdoc lib --inline-source
rdoc --ri lib -o ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby install.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%{ruby_rubylibdir}/guid.rb
%{ruby_ridir}/*
