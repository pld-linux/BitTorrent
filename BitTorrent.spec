
%include /usr/lib/rpm/macros.python

Summary:	BitTorrent is a tool for distributing files.
Name:		BitTorrent
Version:	3.1
Release:	0.1
License:	MIT
Group:		Applications/Communications
Source0:	%{name}-%{version}.tar.gz
#Patch0:		%{name}-what.patch
URL:		http://bitconjurer.org/BitTorrent/
Requires:	python-wxPython
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BitTorrent is a tool for distributing files. It's extremely
easy to use - downloads are started by clicking on hyperlinks.
Whenever more than one person is downloading at once
they send pieces of the file(s) to each other, thus relieving
the central server's bandwidth burden. Even with many
simultaneous downloads, the upload burden on the central server
remains quite small, since each new downloader introduces new
upload capacity.

%prep
%setup -q

%build
find -type f | xargs perl -pi -e 's/python2/python/g'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
chmod a-x $RPM_BUILD_ROOT/%{_bindir}/btdownloadlibrary.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ.txt INSTALL.unix.txt LICENSE.txt README.txt credits.txt todo.txt
%attr(755,root,root) %{_bindir}/btdownloadgui.py
%attr(755,root,root) %{_bindir}/btdownloadheadless.py
%attr(755,root,root) %{_bindir}/btdownloadprefetched.py
%attr(755,root,root) %{_bindir}/btmakemetafile.py
%attr(755,root,root) %{_bindir}/bttrack.py
%{_bindir}/btdownloadlibrary.py
%{py_sitedir}/BitTorrent
