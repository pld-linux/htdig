Summary:	A web indexing and searching system for a small domain or intranet
Summary(es):	Indexador y mАquina de bЗsqueda para web
Summary(pl):	System indeksowania i przeszukiwania www dla maЁych domen i intranetu
Summary(pt_BR):	Indexador e mАquina de procura para web
Summary(ru):	Индексирующая система web-поиска для небольших доменов или intranet
Summary(uk):	╤ндексуюча система web-пошуку для невеликих домен╕в чи intranet
Name:		htdig
Version:	3.2.0b3
Release:	1
License:	GPL
Group:		Networking/Utilities
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

%description -l es
El ht://Dig es un sistema completo para indexaciСn y bЗsqueda en un
dominio pequeЯo o intranet. El sistema no fue proyectado para
substituir sistemas mАs potentes en Internet como el Lycos, Infoseek,
Webcrawler o Altavista. Su propСsito es cubrir las necesidades de una
compaЯМa, campus o mismo una secciСn particular de un sitio Web.
Diferentemente de sistemas de bЗsqueda basados en WAIS o servidores
web el ht://Dig puede cubrir varios servidores web en una
localizaciСn. El tipo de estos diferentes servidores web no interesa
desde que entiendan el protocolo HTTP 1.0.

%description -l pl
ht://Dig jest kompletnym systemem indeksuj╠cym i przeszukuj╠cym www
dla maЁych domen oraz intranetu. System nie zostaЁ opracowany jako
wielki system typu Lycos, Infoseek WebCrawler i AltaVista. Natomiast
nadeje siЙ do zastosowania w pojedyЯczej firmie, kampusie lub
jakiejkolwiek stronie www.

W odrС©nieniu do innych bazuj╠cych na WAIS-sie lub serwerch www
systemach, ht://Dig mo©e Ё╠czyФ kilka serwerСw www w jednym miejscu.
Typ serwera nie ma znaczenia, dopСki pracuje on zgodnie z protokoЁem
HTTP 1.0

%description -l pt_BR
O ht://Dig И um sistema completo para indexaГЦo e busca em um domМnio
pequeno ou intranet. O sistema nЦo foi projetado para substituir
sistemas mais poderosos para a Internet como o Lycos, Infoseek,
Webcrawler ou Altavista. Seu propСsito И cobrir as necessidades para
uma companhia, campus ou mesmo uma seГЦo particular de um site Web.

Diferentemente de sistemas de busca baseados em WAIS ou servidores web
o ht://Dig pode cobrir vАrios servidores web em uma localizaГЦo. O
tipo destes diferentes servidores web nЦo interessa desde que eles
entendam o protocolo HTTP 1.0.

%description -l ru
Система ht://Dig является законченной системой индексирования и поиска
в веб-страницах для небольших доменов или intranet. Эта система не
предназначена для замены мощных общеинтернетовских поисковых систем
типа Lycos, Infoseek, Webcrawler или AltaVista. Ее назначение -
обеспечить потребности в средствах поиска для компании, кампуса или
даже подраздела одного веб-сайта.

В противоположность некоторым поисковым машинам, основанным на WAIS
или средствах веб-сервера, ht://Dig может обслуживать несколько
веб-серверов в одном поисковом сайте. Типы этих различных веб-серверов
значения не имеют, необходима всего лишь поддержка протокола HTTP 1.0.

%description -l uk
Система ht://Dig ╓ завершеною системою ╕ндексування та пошуку у
веб-стор╕нках для невеликих домен╕в та intranet. Ця система не
призначена для зам╕ни потужних загально╕нтернет╕вських пошукових
систем типу Lycos, Infoseek, Webcrawler чи AltaVista. ╥╖ призначення -
забезпечити потреби в засобах пошуку для компан╕╖, кампусу чи нав╕ть
п╕дрозд╕лу одного веб-сайту.

На противагу деяким пошуковим системам, що базуються на WAIS чи
засобах веб-серверу, ht://Dig може обслуговувати дек╕лька веб-сервер╕в
в одному пошуковому сайт╕. Типи цих р╕зних веб-сервер╕в значення не
мають, необх╕дна всього лише п╕дтримка протоколу HTTP 1.0.

%package devel
Summary:	Include files and libraries for htdig
Summary(pl):	Pliki nagЁСwkowe dla htdig
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains devlopment files for htdig.

%description devel -l pl
Ten pakiet zawiera pliki nagЁСwkowe htdig.

%package static
Summary:	htdig static libraries
Summary(pl):	Biblioteki statyczne htdig
Group:		Development/Libraries
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
