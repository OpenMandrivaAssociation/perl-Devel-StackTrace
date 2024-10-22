%define	upstream_name	 Devel-StackTrace

Name:		perl-%{upstream_name}
Version:	2.05
Release:	1

Summary:	Stack trace and stack trace frame objects 

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Devel::StackTrace
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} module for perl.  Simple objects to deal with stack traces.
The parent object, Devel::StackTrace, holds a number of
Devel::StackTraceFrame objects (which have the same information as is
returned from caller()).  You can step through these frames forwards
and backwards as you want or retrieve specific frames.

%prep
%setup -q -n %{upstream_name}-%{version}
chmod 644 lib/Devel/StackTrace.pm

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%make_install

%files
%doc Changes LICENSE 
%{perl_vendorlib}/Devel
%{_mandir}/*/*
