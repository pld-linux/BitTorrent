%include	/usr/lib/rpm/macros.python
Summary:	BitTorrent - a tool for distributing files
Summary(pl):	BitTorrent - narzêdzie do rozpowszechniania plików
Name:		BitTorrent
Version:	3.3
Release:	2
License:	MIT
Group:		Applications/Communications
#Source0Download:	http://bitconjurer.org/BitTorrent/download.html
Source0:	http://bitconjurer.org/BitTorrent/%{name}-%{version}.tar.gz
# Source0-md5:	1ecf1fc40b4972470313f9ae728206e8
URL:		http://bitconjurer.org/BitTorrent/
BuildRequires:  python-devel
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
Requires:	BitTorrent = %{name}-%{version}
Requires:	python-wxPython

%description gui
wxWindows based GUI for BitTorrent.

%description gui -l pl
Bazuj±cy na wxWindows graficzny interfejs u¿ytkownika dla BitTorrenta.

%prep
%setup -q

%build
find -type f | xargs perl -pi -e 's/python2/python/g'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

./setup.py install --prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL.unix.txt LICENSE.txt README.txt credits.txt 
%attr(755,root,root) %{_bindir}/btcompletedir.py
%attr(755,root,root) %{_bindir}/btdownloadcurses.py
%attr(755,root,root) %{_bindir}/btdownloadheadless.py
%attr(644,root,root) %{_bindir}/btdownloadlibrary.py
%attr(755,root,root) %{_bindir}/btlaunchmany*.py
%attr(755,root,root) %{_bindir}/btmakemetafile.py
%attr(755,root,root) %{_bindir}/btr*.py
%attr(755,root,root) %{_bindir}/btt*.py
%attr(755,root,root) %{_bindir}/btshowmetainfo.py
%{py_sitedir}/BitTorrent

%files gui
%attr(755,root,root) %{_bindir}/btdownloadgui.py
%attr(755,root,root) %{_bindir}/btcompletedirgui.py
