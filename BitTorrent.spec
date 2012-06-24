Summary:	BitTorrent - a tool for distributing files
Summary(pl):	BitTorrent - narz�dzie do rozpowszechniania plik�w
Name:		BitTorrent
Version:	4.2.2
Release:	1
License:	BitTorrent Open Source License
Group:		Applications/Communications
Source0:	http://www.bittorrent.com/dl/%{name}-%{version}.tar.gz
# Source0-md5:	2a85715b8ef0335ecc9e8ad91860231b
Patch0:		%{name}-man_pages.patch
Patch1:		%{name}-morei18n.patch
URL:		http://www.bittorrent.com/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
%pyrequires_eq	python-modules
Requires:	python-Crypto
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
BitTorrent to narz�dzie do rozpowszechniania plik�w. Jest bardzo �atwe
w u�yciu - �ci�ganie rozpoczyna si� przez klikanie na hiper��cza.
Je�li wi�cej ni� jedna osoba �ci�ga dany plik, wysy�aj� cz�ci pliku
mi�dzy sob�, �agodz�c obci��enie ��cza centralnego serwera. Nawet przy
wielu jednoczesnych po��czeniach wykorzystanie ��cza g��wnego serwera
pozostaje do�� ma�e, poniewa� ka�dy nowy �ci�gaj�cy daje nowe
mo�liwo�ci �ci�gania.

%package gui
Summary:	GUI for BitTorrent
Summary:	Graficzny interfejs u�ytkownika dla BitTorrenta
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-gtk >= 2.4.0

%description gui
GUI for BitTorrent.

%description gui -l pl
Graficzny interfejs u�ytkownika dla BitTorrenta.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{gr,el}.po
mv -f po/he{_IL,}.po
mv -f po/nb{_NO,}.po

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

#rm -rf locale
#. ./makei18n.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm
install debian/* $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang bittorrent

%clean
rm -rf $RPM_BUILD_ROOT

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
%{py_sitescriptdir}/khashmir
%{_mandir}/man1/*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bittorrent
%attr(755,root,root) %{_bindir}/maketorrent
%{_pixmapsdir}/BitTorrent-%{version}
