Summary:	GNOME program for creating CDs
Summary(pl.UTF-8):	Program dla GNOME do nagrywania płyt CD
Name:		gnomebaker
Version:	0.6.2
Release:	3
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/gnomebaker/%{name}-%{version}.tar.gz
# Source0-md5:	0f9bcc1ff2640b0705c4999dc98dc501
Patch0:		%{name}-desktop.patch
URL:		http://gnomebaker.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gstreamer-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires:	gstreamer-gnomevfs
Suggests:	cdrdao
Suggests:	cdrtools
Suggests:	cdda2wav
Suggests:	mkisofs
Suggests:	readcd
Suggests:	dvd+rw-tools
Suggests:	gstreamer-flac
Suggests:	gstreamer-mad
Suggests:	gstreamer-vorbis
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnomeBaker is a GNOME CD burning application.

%description -l pl.UTF-8
GnomeBaker jest programem dla GNOME do nagrywania CD.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
# these seem to be more up-to-date
cp -f po/es{_ES,}.po
# this one is not so obvious...
# cp -f po/sv{_SE,}.po
rm -f po/*.gmo

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-libnotify
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

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{es_ES,fr_FR,de_CH,es_CR,eu_ES,fr_CH,it,no,nl,pt,zh,de} #FIXME
mv $RPM_BUILD_ROOT%{_datadir}/locale/de{_DE,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/it{_IT,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/nl{_NL,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

%find_lang %{name} --with-gnome

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
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/48x48/apps/gnomebaker-48.png
