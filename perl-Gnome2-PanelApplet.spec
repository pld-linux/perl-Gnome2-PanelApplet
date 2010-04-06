#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Gnome2-PanelApplet
Summary:	Perl interface to the GNOME's applet library
Summary(pl.UTF-8):	Interfejs perlowy do biblioteki apletów GNOME
Name:		perl-Gnome2-PanelApplet
Version:	0.03
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	f41e33ef3cbba5c3be1a17038ccc877e
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gnome-panel-devel >= 2.0.0
# probably should be required by perl-Gnome2
BuildRequires:	libgnomeui-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.200
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.160
BuildRequires:	perl-Gnome2 >= 1.042
BuildRequires:	perl-Gnome2-GConf >= 1.044
BuildRequires:	perl-Gtk2 >= 1.160
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gnome-panel-libs >= 2.0.0
Requires:	perl-Glib >= 1.160
Requires:	perl-Gnome2 >= 1.042
Requires:	perl-Gnome2-GConf >= 1.044
Requires:	perl-Gtk2 >= 1.160
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to the GNOME's applet library.

%description -l pl.UTF-8
Interfejs perlowy do biblioteki apletów GNOME.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/PanelApplet/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHOR NEWS README
%{perl_vendorarch}/Gnome2/PanelApplet.pm
%dir %{perl_vendorarch}/Gnome2/PanelApplet
%{perl_vendorarch}/Gnome2/PanelApplet/Install
%dir %{perl_vendorarch}/auto/Gnome2/PanelApplet
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/PanelApplet/PanelApplet.so
%{perl_vendorarch}/auto/Gnome2/PanelApplet/PanelApplet.bs
%{_mandir}/man3/Gnome2::PanelApplet*.3pm*
