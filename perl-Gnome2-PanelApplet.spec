#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%define		pnam	Gnome2-PanelApplet
Summary:	Perl interface to the GNOME's applet library
Summary(pl.UTF-8):	Interfejs perlowy do biblioteki apletów GNOME
Name:		perl-Gnome2-PanelApplet
Version:	0.04
Release:	0.1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	513cddd6aa7f6b4c92a68331733817fe
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gnome-panel-devel >= 2.0.0
BuildRequires:	gnome-panel-devel < 3
# probably should be required by perl-Gnome2
BuildRequires:	libgnomeui-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.200
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.160
BuildRequires:	perl-Gnome2-devel >= 1.042
BuildRequires:	perl-Gnome2-GConf-devel >= 1.044
BuildRequires:	perl-Gtk2 >= 1.160
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	gnome-panel-libs >= 2.0.0
Requires:	perl-Glib >= 1.160
Requires:	perl-Gnome2 >= 1.042
Requires:	perl-Gnome2-GConf >= 1.044
Requires:	perl-Gtk2 >= 1.160
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to the GNOME's applet library.

Note: this module is deprecated and no longer maintained.

%description -l pl.UTF-8
Interfejs perlowy do biblioteki apletów GNOME.

Uwaga: ten moduł jest przestarzały i nie jest już utrzymywany.

%package devel
Summary:	Development files for Perl Gnome2-PanelApplet bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gnome2-PanelApplet dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-panel-devel >= 2.0.0
Requires:	gnome-panel-devel < 3
Requires:	perl-Cairo-devel
Requires:	perl-Glib-devel >= 1.160
Requires:	perl-Gnome2-devel >= 1.042
Requires:	perl-Gnome2-Canvas-devel
Requires:	perl-Gnome2-GConf-devel >= 1.044
Requires:	perl-Gnome2-VFS-devel
Requires:	perl-Gtk2-devel >= 1.160

%description devel
Development files for Perl Gnome2-PanelApplet bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gnome2-PanelApplet dla Perla.

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/PanelApplet/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHOR NEWS README
%{perl_vendorarch}/Gnome2/PanelApplet.pm
%dir %{perl_vendorarch}/Gnome2/PanelApplet
%dir %{perl_vendorarch}/auto/Gnome2/PanelApplet
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/PanelApplet/PanelApplet.so
%{_mandir}/man3/Gnome2::PanelApplet*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome2/PanelApplet/Install
