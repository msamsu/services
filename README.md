Linux web services .deb package sources
=======================================


Includes
--------

Nginx
http://wiki.nginx.org/Main

uWsig
http://projects.unbit.it/uwsgi/


Does
----

* downloads source
* compiles it
* creates .deb package
* and eventually installs it


Requirements
------------

```bash
apt-get install dpkg-dev debhelper libpcre3-dev libcurl4-openssl-dev
```


Usage
-----

To only create the package run:

```bash
git clone https://github.com/lemr/services.git
cd services
cd nginx
make pkgbuild && make pgkclean
```


Eventually to create and install the package run:

```bash
git clone https://github.com/lemr/services.git
cd services
cd nginx
make pkginst && make pgkclean
```


Notes
-----

* Installs all to /var/www/(nginx|uwsgi)-compiled
* Only creates init scripts to /etc/init.d/ but does NOT add them to rc.d by default
* Configuration can be found in /var/www/(nginx|uwsgi)-compiled/conf


Please send me any missing dependencies.
