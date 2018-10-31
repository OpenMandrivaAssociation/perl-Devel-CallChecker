%define modname	Devel-CallChecker

Summary:	Perl module for custom op checking attached to subroutines
Name:		perl-%{modname}
Version:	0.008
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/Z/ZE/ZEFRAM/Devel-CallChecker-%{version}.tar.gz

%description
Perl module for custom op checking attached to subroutines

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
