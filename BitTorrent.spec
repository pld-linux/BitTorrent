Summary:	BitTorrent - a tool for distributing files
Summary(pl.UTF-8):	BitTorrent - narzędzie do rozpowszechniania plików
Name:		BitTorrent
Version:	5.0.8
Release:	2
License:	BitTorrent Open Source License
Group:		Applications/Communications
Source0:	http://download.bittorrent.com/dl/%{name}-%{version}.tar.gz
# Source0-md5:	43935e080fade4726fa07bb2565f5f48
Source1:	%{name}.desktop
Patch0:		%{name}-man_pages.patch
Patch1:		%{name}-morei18n.patch
Patch2:		%{name}-pl.patch
URL:		http://www.bittorrent.com/
BuildRequires:	python-devel
BuildRequires:	python-devel-tools
BuildRequires:	python-TwistedCore
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-modules
Requires:	python-Crypto
Requires:	python-TwistedCore
Requires:	python-TwistedWeb
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

%description -l pl.UTF-8
BitTorrent to narzędzie do rozpowszechniania plików. Jest bardzo łatwe
w użyciu - ściąganie rozpoczyna się przez klikanie na hiperłącza.
Jeśli więcej niż jedna osoba ściąga dany plik, wysyłają części pliku
między sobą, łagodząc obciążenie łącza centralnego serwera. Nawet przy
wielu jednoczesnych połączeniach wykorzystanie łącza głównego serwera
pozostaje dość małe, ponieważ każdy nowy ściągający daje nowe
możliwości ściągania.

%package gui
Summary:	GUI for BitTorrent
Summary(pl.UTF-8):	Graficzny interfejs użytkownika dla BitTorrenta
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-wxPython
Requires(post,postun):	desktop-file-utils

%description gui
GUI for BitTorrent.

%description gui -l pl.UTF-8
Graficzny interfejs użytkownika dla BitTorrenta.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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

cp $RPM_BUILD_ROOT%{_pixmapsdir}/*-%{version}/logo/bittorrent_icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/bittorrent.png
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
%dir %{py_sitescriptdir}/BitTorrent
%{py_sitescriptdir}/BitTorrent/*.py[co]
%{py_sitescriptdir}/Zeroconf.py[co]
%{py_sitescriptdir}/khashmir
%{py_sitescriptdir}/BTL
%{_mandir}/man1/*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bittorrent
%attr(755,root,root) %{_bindir}/maketorrent
%{py_sitescriptdir}/BitTorrent/GUI_wx
%{_pixmapsdir}/*-%{version}
%{_pixmapsdir}/bittorrent.png
%{_desktopdir}/%{name}.desktop
