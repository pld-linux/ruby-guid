Summary:	Ruby GUID Library
Summary(pl.UTF-8):   Biblioteka Ruby GUID
Name:		ruby-guid
Version:	0.0.1
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/378/%{name}-%{version}.tar.gz
# Source0-md5:	10f50564c198db7ba0b592149f90cc52
URL:		http://rubyforge.org/projects/uuid/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
#BuildArch: noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby implementation of the IEEE GUID spec.

%description -l pl.UTF-8
Implementacja specyfikacji IEEE GUID dla języka Ruby.

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
