#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-Daemon
Summary:	POE::Component::Daemon - Handles all the housework for a daemon.
#Summary(pl.UTF-8):	
Name:		perl-POE-Component-Daemon
Version:	0.1006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b6ba32dfcaf612b12af181e0e83e9a67
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/POE-Component-Daemon/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(POE::API::Peek) >= 1
BuildRequires:	perl-POE >= 0.3202
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dealing with all the little details of a forking daemon can be annoying and
hard.  POE::Component::Daemon encapsulates all the details into one place
and (hopefully) gets them right.

POE::Component::Daemon will deal with all the annoying details of creating
and maintaining daemon processes.  It can detach from the console, handle
pre-forking pools or post-forking (ie, fork on each request). It will also
redirect STDERR to a log file if asked.

POE::Component::Daemon also babysits child processes, handling their
CHLD.  POE::Component::Daemon can also makes sure requests don't take
to long.  If they do, it will try to get rid of them.  See /BABYSITING
below.

POE::Component::Daemon does not handle listening on sockets.  That is up to
your code.

Like all of POE, POE::Component::Daemon works cooperatively.  It is up your
code to tell POE::Component::Daemon when it is time to fork, block incoming
requests when approriate and so on.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/*.pm
%{perl_vendorlib}/POE/Component/Daemon
%{_mandir}/man3/*
