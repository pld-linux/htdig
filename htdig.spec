Summary:	A web indexing and searching system for a small domain or intranet
Summary(pl):	System indeksowania i przeszukiwania www dla ma³ych domen i intranetu
Name:		htdig
Version:	3.2.0b3
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(cs):	Sí»ové/Utility
Group(da):	Netværks/Værktøj
Group(de):	Netzwerkwesen/Dienstprogramme
Group(es):	Red/Utilitarios
Group(fr):	Réseau/Utilitaires
Group(is):	Net/Tól
Group(it):	Rete/Utility
Group(no):	Nettverks/Verktøy
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Group(pt):	Rede/Utilidades
Group(ru):	óÅÔØ/õÔÉÌÉÔÙ
Group(sl):	Omre¾ni/Pripomoèki
Group(sv):	Nätverk/Verktyg
Group(uk):	íÅÒÅÖÁ/õÔÉÌ¦ÔÉ
Source0:	http://www.htdig.org/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-glibc22.patch
URL:		http://www.htdig.org/
BuildRequires:	zlib-devel
BuildRequires:	libstdc++-devel
PreReq:		webserver
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

%package devel
Summary:	Include files and libraries for htdig
Summary(pl):	Pliki nag³ówkowe dla htdig
Group:		Development/Libraries
Group(cs):	Vývojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	Þróunartól/Aðgerðasöfn
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	Razvoj/Knji¾nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
This package contains devlopment files for htdig.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe htdig.

%package static
Summary:	htdig static libraries
Summary(pl):	Biblioteki statyczne htdig
Group:		Development/Libraries
Group(cs):	Vývojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	Þróunartól/Aðgerðasöfn
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	Razvoj/Knji¾nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries of htdig.

%description static -l pl
Statyczne biblioteki htdig.

%prep
%setup -q
%patch -p1

%build
%configure2_13 \
	--libexec=%{_libdir} \
	--sysconfdir=%{_sysconfdir}/%{name} \
	--with-image-dir=/home/httpd/html/%{name} \
	--with-cgi-bin-dir=/home/httpd/cgi-bin \
	--with-search-dir=/home/httpd/html \
	--with-config-dir=%{_sysconfdir}/%{name} \
	--localstatedir=%{_var}/lib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/cron.daily
ln -sf ../..%{_bindir}/rundig \
	$RPM_BUILD_ROOT/etc/cron.daily/htdig-dbgen

install -d $RPM_BUILD_ROOT/home/httpd/html/htdig/
ln -sf ../../../..%{_defaultdocdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT/home/httpd/html/htdig/htdoc

install -d $RPM_BUILD_ROOT/var/lib/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Only run this if installing for the first time
if [ "$1" = 1 ]; then
	for i in `grep '^ServerName' /etc/httpd/httpd.conf | sort -u | awk '{print $2}'`; do echo -n http://$i/; echo -n " "; done > /tmp/htdig.tmp
	SERVERNAMES="`cat /tmp/htdig.tmp`"
	[ -z "$SERVERNAMES" ] && SERVERNAMES="`hostname -f`"
	[ -z "$SERVERNAMES" ] && SERVERNAMES="localhost"
	SERVERNAME=`grep '^ServerName' /etc/httpd/httpd.conf | uniq -d | awk '{print $2}'`
	grep -v -e local_urls -e local_user_urls -e start_url /etc/htdig/htdig.conf > /tmp/htdig.tmp
	mv -f /tmp/htdig.tmp /etc/htdig/htdig.conf
	echo "start_url:$SERVERNAMES
local_urls:		$SERVERNAMES
local_user_urls:	http://$SERVERNAME/=/home/,/public_html/" >> /etc/htdig/htdig.conf

fi

%files
%defattr(644,root,root,755)
%doc COPYING README htdoc
%dir /var/lib/%{name}
%attr (755,nobody,nobody) /home/httpd/cgi-bin/*
%attr (755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/mifluz
%attr (755,root,root) %{_libdir}/*/*.so
%attr (755,root,root) %{_libdir}/*/*.la
/home/httpd/html/%{name}/*
%{_datadir}/%{name}/*
%config(noreplace) %{_sysconfdir}/htdig/*
%config(missingok noreplace) %verify(not size mtime md5) /home/httpd/html/search.html
%config(missingok) %{_sysconfdir}/cron.daily/htdig-dbgen

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/*
%{_includedir}/*/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*/*.a
