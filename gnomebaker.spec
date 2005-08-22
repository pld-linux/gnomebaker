Summary:	GNOME program for creating CDs
Summary(pl):	Program dla GNOME do nagrywania p�yt CD
Name:		gnomebaker
Version:	0.4.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/gnomebaker/%{name}-%{version}.tar.gz
# Source0-md5:	caac582ec6896a49cd76779e54ef6d3e
Patch0:		%{name}-desktop.patch
URL:		http://gnomebaker.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires:	gstreamer-gnomevfs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnomeBaker is a GNOME CD burning application.

%description -l pl
GnomeBaker jest programem dla GNOME do nagrywania CD.

%prep
%setup -q
%patch0 -p1
# these seem to be more up-to-date
cp -f po/es{_ES,}.po
# this one is not so obvious...
# cp -f po/sv{_SE,}.po
rm -f po/*.gmo

%build
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

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{es_ES,fr_FR,sv_SE}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/nl{_NL,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%banner %{name} -e << EOF
Suggested packages for use with Gnomebaker:
for CD recording
- cdrdao
- cdrtools
- cdrtools-cdda2wav
- cdrtools-mkisofs
- cdrtools-readcd
- dvd+rw-tools
for operations on audio files
- gstreamer-flac
- gstreamer-mad
- gstreamer-vorbis
EOF

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
