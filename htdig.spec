Summary:	A web indexing and searching system for a small domain or intranet
Summary(pl):	System indeksowania i przeszukiwania www dla ma³ych domen i intranetu
Name:		htdig
Version:	3.1.2
Release:	1
Copyright:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source:		http://www.htdig.org/files/%{name}-%{version}.tar.gz
Patch0:		htdig-conf.patch
URL:		http://www.htdig.org/
Prereq:		webserver
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The ht://Dig system is a complete world wide web indexing and searching
system for a small domain or intranet. This system is not meant to replace
the need for powerful internet-wide search systems like Lycos, Infoseek,
Webcrawler and AltaVista. Instead it is meant to cover the search needs for
a single company, campus, or even a particular sub section of a web site.

As opposed to some WAIS-based or web-server based search engines, ht://Dig
can span several web servers at a site. The type of these different web
servers doesn't matter as long as they understand the HTTP 1.0 protocol.

%description -l pl
ht://Dig jest kompletnym systemem indeksuj±cym i przeszukuj±cym www
dla ma³ych domen oraz intranetu. System nie zosta³ opracowany jako
wielki system typu Lycos, Infoseek WebCrawler i AltaVista. Natomiast
nadeje siê do zastosowania w pojedyñczej firmie, kampusie lub jakiejkolwiek
stronie www.

W odró¿nieniu do innych bazuj±cych na WAIS-sie lub serwerch www systemach,
ht://Dig mo¿e ³±czyæ kilka serwerów www w jednym miejscu. Typ serwera nie ma
znaczenia, dopóki pracuje on zgodnie z protoko³em HTTP 1.0

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--bindir=%{_sbindir} \
	--libexec=%{_libdir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--sysconfdir=/etc/htdig \
	--localstatedir=/var/state/htdig \
	--with-image-dir=/home/httpd/html/htdig \
	--with-cgi-bin-dir=/home/httpd/cgi-bin \
	--with-search-dir=/home/httpd/html
make

%install
rm -rf $RPM_BUILD_ROOT

make INSTALL_ROOT=$RPM_BUILD_ROOT install-strip
install -d $RPM_BUILD_ROOT/etc/cron.daily
ln -s ../..%{_sbindir}/rundig $RPM_BUILD_ROOT/etc/cron.daily/htdig-dbgen
install -d $RPM_BUILD_ROOT/home/httpd/html/htdig/
ln -s ../../../../usr/doc/htdig-%{name}-%{version} \
        $RPM_BUILD_ROOT/home/httpd/html/htdig/htdoc

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Only run this if installing for the first time
if [ "$1" = 1 ]; then
	SERVERNAME="`grep '^ServerName' /etc/httpd/conf/httpd.conf | awk '{print $2}'`"
	[ -z "$SERVERNAME" ] && SERVERNAME="`hostname -f`"
	[ -z "$SERVERNAME" ] && SERVERNAME="localhost"
	echo "start_url:	http://$SERVERNAME/
local_urls:	http://$SERVERNAME/=/home/httpd/html/
local_user_urls:	http://$SERVERNAME/=/home/,/public_html/" >> /etc/htdig/htdig.conf

fi

%files
%defattr(644,root,root,755)
%doc CONFIG README htdoc/*
%attr (640,root,root) %config /etc/htdig/htdig.conf
%attr (755,root,root) %config %{_sbindir}/*
%config(missingok noreplace) %verify(not size mtime md5) /home/httpd/html/search.html
%config(missingok) /etc/cron.daily/htdig-dbgen
/var/state/htdig
%attr(755,root,root) /home/httpd/cgi-bin/htsearch
/home/httpd/html/htdig
