%define	upstream_name	 Devel-StackTrace
%define upstream_version 1.32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Stack trace and stack trace frame objects 

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} module for perl.  Simple objects to deal with stack traces.
The parent object, Devel::StackTrace, holds a number of
Devel::StackTraceFrame objects (which have the same information as is
returned from caller()).  You can step through these frames forwards
and backwards as you want or retrieve specific frames.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 lib/Devel/StackTrace.pm

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Devel
%{_mandir}/*/*



