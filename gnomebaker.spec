Summary:	GNOME program for creating CDs
Summary(pl):	Program dla GNOME do nagrywania p³yt CD
Name:		gnomebaker
Version:	0.3
Release:	2
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://biddell.co.uk/files/%{name}-%{version}.tar.gz
# Source0-md5:	dd8276d35a0a3e31b3c16e136b079f83
Patch0:		%{name}-desktop.patch
URL:		http://biddell.co.uk/gnomebaker.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
Requires:	cdrtools
Requires:	cdrtools-cdda2wav
Requires:	cdrtools-mkisofs
Requires:	cdrtools-readcd
Requires:	mpg123
Requires:	vorbis-tools
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnomeBaker is a GNOME CD burning application.

%description -l pl
GnomeBaker jest programem dla GNOME do nagrywania CD.

%prep
%setup -q
%patch0 -p1

%build
##cp /usr/share/gnome-common/data/omf.make .
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomemenudir=%{_desktopdir} \
	gnomebakerdoc_DATA=""

install pixmaps/gnomebaker-48.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/gnomebaker.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update -q

%postun
if [ $1 = 0 ]; then
	/usr/bin/scrollkeeper-update -q
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
