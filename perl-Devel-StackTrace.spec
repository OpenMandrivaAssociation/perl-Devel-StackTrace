%define	upstream_name	 Devel-StackTrace
%define upstream_version 1.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Stack trace and stack trace frame objects 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Devel-StackTrace-%{upstream_version}.tar.gz

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.270.0-4mdv2012.0
+ Revision: 765183
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.270.0-3
+ Revision: 763699
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.270.0-2
+ Revision: 667116
- mass rebuild

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.270.0-1
+ Revision: 634268
- update to new version 1.27

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.260.0-1mdv2011.0
+ Revision: 587609
- update to new version 1.26

* Sat Sep 04 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.240.0-2mdv2011.0
+ Revision: 575738
- update to 1.24

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.220.0-2mdv2010.1
+ Revision: 405855
- bump mkrel to force rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.220.0-1mdv2010.0
+ Revision: 403104
- rebuild using %%perl_convert_version

* Thu Jul 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2010.0
+ Revision: 396544
- update to new version 1.22

* Fri Jul 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdv2010.0
+ Revision: 391943
- update to new version 1.21

* Mon Oct 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2009.1
+ Revision: 297539
- update to new version 1.20

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.18-2mdv2009.0
+ Revision: 268419
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.18-1mdv2009.0
+ Revision: 194847
- update to new version 1.18

* Sun Feb 03 2008 Funda Wang <fwang@mandriva.org> 1.16-1mdv2008.1
+ Revision: 161657
- update to new version 1.16

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 1.15-2mdv2008.0
+ Revision: 64784
- rebuild

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.15-1mdv2008.0
+ Revision: 20058
- 1.15


* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-1mdk
- New release 1.13

* Tue Oct 04 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdk
- New release 1.12
- spec cleanup
- fix directory onwership
- %%mkrel
- make test in %%check
- better summary
- better url
- fix sources url

* Fri Jun 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.11-1mdk
- ARG! 1.11 !"!!"#"!*#E*FRI)ET"¤5IXUUSJFH fsck this§

* Wed Jun 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.03-1mdk
- 1.03
- wipe out buildroot in %%install, not %%prep
- coosmetics

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.03-3mdk
- rebuild for new auto{prov,req}


