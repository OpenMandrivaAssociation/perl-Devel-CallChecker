%define modname	Devel-CallChecker
%ifarch %{x86_64}
# FIXME seems to be a bug in the debugpackage generator
%global _debugsource_template %{nil}
%endif

Summary:	Perl module for custom op checking attached to subroutines
Name:		perl-%{modname}
Version:	0.008
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Devel::CallChecker
Source0:	http://search.cpan.org/CPAN/authors/id/Z/ZE/ZEFRAM/Devel-CallChecker-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(DynaLoader::Functions)
Requires:       perl(DynaLoader)
Requires:       perl(DynaLoader::Functions)

%description
Perl module for custom op checking attached to subroutines.

%prep
%autosetup -p1 -n %{modname}-%{version}
%__perl Build.PL installdirs=vendor optimize="%{optflags}"

%build
./Build

%check
./Build test

%install
./Build install destdir="%{buildroot}" create_packlist=0

%files
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/man3/*
