%define	snap	20030413
Summary:	A web indexing and searching system for a small domain or intranet
Summary(es):	Indexador y m�quina de b�squeda para web
Summary(pl):	System indeksowania i przeszukiwania www dla ma�ych domen i intranetu
Summary(pt_BR):	Indexador e m�quina de procura para web
Summary(ru):	������������� ������� web-������ ��� ��������� ������� ��� intranet
Summary(uk):	���������� ������� web-������ ��� ��������� ����Φ� �� intranet
Name:		htdig
Version:	3.2.0b4
Release:	0.%{snap}.1
License:	GPL
Group:		Networking/Utilities
# 3.2.0b3 has security bugs, so for now we are using snapshot
Source0:	http://www.htdig.org/files/snapshots/%{name}-%{version}-%{snap}.tar.gz
Patch0:		%{name}-pl-dont-mix-up.patch
URL:		http://www.htdig.org/
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
Requires(post):	awk
Requires(post):	fileutils
Requires(post):	grep
Requires(post):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/htdig
%define		cgidir		/home/services/httpd/cgi-bin
%define		htmldir		/home/services/httpd/html
%define		htdigdir	%{htmldir}/%{name}

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
This version of ht://Dig has been patched for handling pl chars encoded 
in iso-8859-2.

%description -l es
El ht://Dig es un sistema completo para indexaci�n y b�squeda en un
dominio peque�o o intranet. El sistema no fue proyectado para
substituir sistemas m�s potentes en Internet como el Lycos, Infoseek,
Webcrawler o Altavista. Su prop�sito es cubrir las necesidades de una
compa��a, campus o mismo una secci�n particular de un sitio Web.
Diferentemente de sistemas de b�squeda basados en WAIS o servidores
web el ht://Dig puede cubrir varios servidores web en una
localizaci�n. El tipo de estos diferentes servidores web no interesa
desde que entiendan el protocolo HTTP 1.0.
This version of ht://Dig has been patched for handling pl chars encoded
in iso-8859-2.

%description -l pl
ht://Dig jest kompletnym systemem indeksuj�cym i przeszukuj�cym www
dla ma�ych domen oraz intranetu. System nie zosta� opracowany jako
wielki system typu Lycos, Infoseek WebCrawler i AltaVista. Natomiast
nadeje si� do zastosowania w pojedy�czej firmie, kampusie lub
jakiejkolwiek stronie www.

W odr�nieniu do innych bazuj�cych na WAIS-sie lub serwerch www
systemach, ht://Dig mo�e ��czy� kilka serwer�w www w jednym miejscu.
Typ serwera nie ma znaczenia, dop�ki pracuje on zgodnie z protoko�em
HTTP 1.0
Ta wersja ht://Dig zosta�a za�atana aby obs�ugiwa� polskie znaki 
zakodowane zgodnie z ISO-8859-2.

%description -l pt_BR
O ht://Dig � um sistema completo para indexa��o e busca em um dom�nio
pequeno ou intranet. O sistema n�o foi projetado para substituir
sistemas mais poderosos para a Internet como o Lycos, Infoseek,
Webcrawler ou Altavista. Seu prop�sito � cobrir as necessidades para
uma companhia, campus ou mesmo uma se��o particular de um site Web.

Diferentemente de sistemas de busca baseados em WAIS ou servidores web
o ht://Dig pode cobrir v�rios servidores web em uma localiza��o. O
tipo destes diferentes servidores web n�o interessa desde que eles
entendam o protocolo HTTP 1.0.
This version of ht://Dig has been patched for handling pl chars encoded
in iso-8859-2.

%description -l ru
������� ht://Dig �������� ����������� �������� �������������� � ������
� ���-��������� ��� ��������� ������� ��� intranet. ��� ������� ��
������������� ��� ������ ������ ������������������ ��������� ������
���� Lycos, Infoseek, Webcrawler ��� AltaVista. �� ���������� -
���������� ����������� � ��������� ������ ��� ��������, ������� ���
���� ���������� ������ ���-�����.

� ����������������� ��������� ��������� �������, ���������� �� WAIS
��� ��������� ���-�������, ht://Dig ����� ����������� ���������
���-�������� � ����� ��������� �����. ���� ���� ��������� ���-��������
�������� �� �����, ���������� ����� ���� ��������� ��������� HTTP 1.0.
This version of ht://Dig has been patched for handling pl chars encoded
in iso-8859-2.

%description -l uk
������� ht://Dig � ���������� �������� ������������ �� ������ �
���-���Ҧ���� ��� ��������� ����Φ� �� intranet. �� ������� ��
���������� ��� ��ͦ�� �������� �������Ϧ������Ԧ������ ���������
������ ���� Lycos, Infoseek, Webcrawler �� AltaVista. �� ����������� -
����������� ������� � ������� ������ ��� �����Φ�, ������� �� ��צ��
Ц����Ħ�� ������ ���-�����.

�� ��������� ������ ��������� ��������, �� ��������� �� WAIS ��
������� ���-�������, ht://Dig ���� ������������� ��˦���� ���-�����Ҧ�
� ������ ���������� ���Ԧ. ���� ��� Ҧ���� ���-�����Ҧ� �������� ��
�����, ����Ȧ��� ������ ���� Ц������� ��������� HTTP 1.0.
This version of ht://Dig has been patched for handling pl chars encoded
in iso-8859-2.

%package devel
Summary:	Include files and libraries for htdig
Summary(pl):	Pliki nag��wkowe dla htdig
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains devlopment files for htdig.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe htdig.

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
%setup -q -n %{name}-%{version}-%{snap}
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
cd db
%{__libtoolize}
%{__aclocal}
%{__autoconf}
cd ..
%configure \
	--libexec=%{_libdir} \
	--sysconfdir=%{_sysconfdir} \
	--with-image-dir=%{htdigdir} \
	--with-cgi-bin-dir=%{cgidir} \
	--with-search-dir=%{htmldir} \
	--with-config-dir=%{_sysconfdir} \
	--localstatedir=%{_var}/lib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/cron.daily,/var/lib/%{name},%{htdigdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_bindir}/rundig $RPM_BUILD_ROOT/etc/cron.daily/htdig-dbgen
ln -sf %{_defaultdocdir}/%{name}-%{version} $RPM_BUILD_ROOT%{htdigdir}/htdoc

for file in $RPM_BUILD_ROOT%{cgidir}/*; do
  file=$(basename "$file")
  cp -f $RPM_BUILD_ROOT%{cgidir}/${file} $RPM_BUILD_ROOT%{_bindir}/${file}
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Only run this if installing for the first time
if [ "$1" = 1 ]; then
  if [ -f /etc/httpd/httpd.conf ]; then
	umask 027
	for i in `grep '^ServerName' /etc/httpd/httpd.conf | sort -u | awk '{print $2}'`; do
		echo -n "http://$i/ "
	done > /etc/httpd/httpd.conf.htdig.tmp
	SERVERNAMES="`cat /etc/httpd/httpd.conf.htdig.tmp`"
	rm -f /etc/httpd/httpd.conf.htdig.tmp
	[ -z "$SERVERNAMES" ] && SERVERNAMES="`hostname -f`"
	[ -z "$SERVERNAMES" ] && SERVERNAMES="localhost"
	SERVERNAME=`grep '^ServerName' /etc/httpd/httpd.conf | uniq -d | awk '{print $2}'`
	grep -v -e local_urls -e local_user_urls -e start_url %{_sysconfdir}/htdig.conf > %{_syscofndir}/htdig.conf.tmp
	mv -f %{_sysconfdir}/htdig.conf.tmp %{_sysconfdir}/htdig.conf
	echo "start_url:$SERVERNAMES
local_urls:		$SERVERNAMES
local_user_urls:	http://$SERVERNAME/=/home/,/public_html/" >> %{_sysconfdir}/htdig.conf
  fi
fi

%files
%defattr(644,root,root,755)
%doc README htdoc
%dir /var/lib/%{name}
%attr(755,root,root) %{cgidir}/ht*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/mifluz
%attr(755,root,root) %{_libdir}/*/*.so
%{_libdir}/*/*.la
%dir %{htdigdir}
%{htdigdir}/*
%{_datadir}/%{name}/*
%attr(750,root,http) %dir %{_sysconfdir}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%config(missingok,noreplace) %verify(not size mtime md5) %{htmldir}/search.html
%config(missingok) /etc/cron.daily/htdig-dbgen

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/*
%{_includedir}/*/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*/*.a
