Summary:	BitTorrent - a tool for distributing files
Summary(pl):	BitTorrent - narzêdzie do rozpowszechniania plików
Name:		BitTorrent
Version:	4.20.7
Release:	1
License:	BitTorrent Open Source License
Group:		Applications/Communications
Source0:	http://www.bittorrent.com/dl/%{name}-%{version}.tar.gz
# Source0-md5:	285f238330992fda6688f70ab377f2c3
Source1:	%{name}.desktop
Patch0:		%{name}-man_pages.patch
Patch1:		%{name}-morei18n.patch
URL:		http://www.bittorrent.com/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-modules
Requires:	python-Crypto
Requires:	python-TwistedCore
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BitTorrent is a tool for distributing files. It's extremely easy to
use - downloads are started by clicking on hyperlinks. Whenever more
than one person is downloading at once they send pieces of the file(s)
to each other, thus relieving the central server's bandwidth burden.
Even with many simultaneous downloads, the upload burden on the
central server remains quite small, since each new downloader
introduces new upload capacity.

%description -l pl
BitTorrent to narzêdzie do rozpowszechniania plików. Jest bardzo ³atwe
w u¿yciu - ¶ci±ganie rozpoczyna siê przez klikanie na hiper³±cza.
Je¶li wiêcej ni¿ jedna osoba ¶ci±ga dany plik, wysy³aj± czê¶ci pliku
miêdzy sob±, ³agodz±c obci±¿enie ³±cza centralnego serwera. Nawet przy
wielu jednoczesnych po³±czeniach wykorzystanie ³±cza g³ównego serwera
pozostaje do¶æ ma³e, poniewa¿ ka¿dy nowy ¶ci±gaj±cy daje nowe
mo¿liwo¶ci ¶ci±gania.

%package gui
Summary:	GUI for BitTorrent
Summary:	Graficzny interfejs u¿ytkownika dla BitTorrenta
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-gtk >= 2.4.0

%description gui
GUI for BitTorrent.

%description gui -l pl
Graficzny interfejs u¿ytkownika dla BitTorrenta.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/nb{_NO,}.po
rm -rf locale
sed -i -e "s/'nb_NO'/'nb'   /;s/'gr'/'el'/;s/'he_IL'/'he'   /" BitTorrent/__init__.py

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

sh makei18n.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_mandir}/man1}

python ./setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm
install debian/* $RPM_BUILD_ROOT%{_mandir}/man1

rm -rf locale/{in,nn_NO,piglatin}
find locale -type f ! -name '*.mo' -exec rm "{}" ";"
cp -a locale/*  $RPM_BUILD_ROOT%{_datadir}/locale

cp $RPM_BUILD_ROOT%{_pixmapsdir}/BitTorrent-%{version}/logo/bittorrent_icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/bittorrent.png
cp %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang bittorrent

%clean
rm -rf $RPM_BUILD_ROOT

%post gui
%update_desktop_database_post

%postun gui
%update_desktop_database_postun

%files -f bittorrent.lang
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt credits.txt 
%attr(755,root,root) %{_bindir}/bittorrent-console
%attr(755,root,root) %{_bindir}/bittorrent-curses
%attr(755,root,root) %{_bindir}/bittorrent-tracker
%attr(755,root,root) %{_bindir}/changetracker-console
%attr(755,root,root) %{_bindir}/launchmany-console
%attr(755,root,root) %{_bindir}/launchmany-curses
%attr(755,root,root) %{_bindir}/maketorrent-console
%attr(755,root,root) %{_bindir}/torrentinfo-console
%{py_sitescriptdir}/BitTorrent
%{py_sitescriptdir}/Zeroconf.py[co]
%{py_sitescriptdir}/khashmir
%{_mandir}/man1/*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bittorrent
%attr(755,root,root) %{_bindir}/maketorrent
%{_pixmapsdir}/BitTorrent-%{version}
%{_pixmapsdir}/bittorrent.png
%{_desktopdir}/%{name}.desktop
