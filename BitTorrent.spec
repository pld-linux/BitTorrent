Summary:	BitTorrent - a tool for distributing files
Summary(pl):	BitTorrent - narzêdzie do rozpowszechniania plików
Name:		BitTorrent
Version:	4.0.0
Release:	1
License:	BitTorrent Open Source License
Group:		Applications/Communications
Source0:	http://www.bittorrent.com/dl/%{name}-%{version}.tar.gz
# Source0-md5:	67f449df351b66f408b72b6bd196952f
Patch0:		%{name}-man_pages.patch
URL:		http://www.bittorrent.com/
BuildRequires:	python-devel
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
%pyrequires_eq	python-modules
Obsoletes:	BitTornado
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
Obsoletes:	BitTornado-gui

%description gui
GUI for BitTorrent.

%description gui -l pl
Graficzny interfejs u¿ytkownika dla BitTorrenta.

%prep
%setup -q
%patch0 -p1

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm
install debian/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt credits.txt 
%attr(755,root,root) %{_bindir}/btdownloadcurses.py
%attr(755,root,root) %{_bindir}/btdownloadheadless.py
%attr(755,root,root) %{_bindir}/btlaunchmany*.py
%attr(755,root,root) %{_bindir}/btmaketorrent.py
%attr(755,root,root) %{_bindir}/btr*.py
%attr(755,root,root) %{_bindir}/btt*.py
%attr(755,root,root) %{_bindir}/btshowmetainfo.py
%{py_sitescriptdir}/BitTorrent
%{_mandir}/man1/*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/btdownloadgui.py
%attr(755,root,root) %{_bindir}/btmaketorrentgui.py
%{_pixmapsdir}/BitTorrent-%{version}
