Summary:	A web indexing and searching system for a small domain or intranet
Summary(pl):	System indeksowania i przeszukiwania www dla ma³ych domen i intranetu
Name:		htdig
Version:	3.1.5
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source0:	http://www.htdig.org/files/%{name}-%{version}.tar.gz
URL:		http://www.htdig.org/
Prereq:		webserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ht://Dig system is a complete world wide web indexing and
searching system for a small domain or intranet. This system is not
meant to replace the need for powerful internet-wide search systems
like Lycos, Infoseek, Webcrawler and AltaVista. Instead it is meant to
cover the search needs for a single company, campus, or even a
particular sub section of a web site.

As opposed to some WAIS-based or web-server based search engines,
ht://Dig can span several web servers at a site. The type of these
different web servers doesn't matter as long as they understand the
HTTP 1.0 protocol.

%description -l pl
ht://Dig jest kompletnym systemem indeksuj±cym i przeszukuj±cym www
dla ma³ych domen oraz intranetu. System nie zosta³ opracowany jako
wielki system typu Lycos, Infoseek WebCrawler i AltaVista. Natomiast
nadeje siê do zastosowania w pojedyñczej firmie, kampusie lub
jakiejkolwiek stronie www.

W odró¿nieniu do innych bazuj±cych na WAIS-sie lub serwerch www
systemach, ht://Dig mo¿e ³±czyæ kilka serwerów www w jednym miejscu.
Typ serwera nie ma znaczenia, dopóki pracuje on zgodnie z protoko³em
HTTP 1.0

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS"
LDFLAGS="-s"
export CFLAGS LDFLAGS

./configure %{_target_platform} \
	--prefix=%{_prefix}/local/htdig \
	--exec_prefix=%{_prefix}/local/htdig \
	--libexec=%{_libdir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
--sysconfdir=%{_sysconfdir}/htdig \
	--with-image-dir=/home/httpd/html/htdig \
	--with-cgi-bin-dir=/home/httpd/cgi-bin \
	--with-search-dir=/home/httpd/html

make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} INSTALL_ROOT=$RPM_BUILD_ROOT install-strip
install -d $RPM_BUILD_ROOT/etc/cron.daily
ln -s ../..%{_prefix}/local/%{name}/bin/rundig $RPM_BUILD_ROOT/etc/cron.daily/htdig-dbgen
install -d $RPM_BUILD_ROOT/home/httpd/html/htdig/
ln -s ../../../..%{_defaultdocdir}/%{name}-%{version} \
        $RPM_BUILD_ROOT/home/httpd/html/htdig/htdoc

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Only run this if installing for the first time
if [ "$1" = 1 ]; then
	for i in `grep '^ServerName' /etc/httpd/conf/httpd.conf | sort -u | awk '{print $2}'`; do echo -n http://$i/; echo -n " "; done > /tmp/htdig.tmp
	SERVERNAMES="`cat /tmp/htdig.tmp`"
	[ -z "$SERVERNAMES" ] && SERVERNAMES="`hostname -f`"
	[ -z "$SERVERNAMES" ] && SERVERNAMES="localhost"
	SERVERNAME=`grep '^ServerName' /etc/httpd/conf/httpd.conf | uniq -d | awk '{print $2}'`
	grep -v -e local_urls -e local_user_urls -e start_url /etc/htdig/htdig.conf > /tmp/htdig.tmp
	mv /tmp/htdig.tmp /etc/htdig/htdig.conf
	echo "start_url:$SERVERNAMES
local_urls:		$SERVERNAMES
local_user_urls:	http://$SERVERNAME/=/home/,/public_html/" >> /etc/htdig/htdig.conf

fi

%files
%defattr(644,root,root,755)
%doc CONFIG README htdoc/*
%attr (755,root,root) %{_prefix}/local/%{name}/bin/*
%attr (755,root,root) %{_prefix}/local/%{name}/common/*
%dir %{_prefix}/local/%{name}/db
%attr (755,nobody,nobody) /home/httpd/cgi-bin
%config(noreplace) %{_sysconfdir}/htdig/htdig.conf
%config(missingok noreplace) %verify(not size mtime md5) /home/httpd/html/search.html
%config(missingok) /etc/cron.daily/htdig-dbgen
/home/httpd/html/htdig
