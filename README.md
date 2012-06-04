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

For creating .deb packages you'll need:

```bash
apt-get install dpkg-dev debhelper
```

For nginx compilation you'll need:

```bash
apt-get install libpcre3-dev libcurl4-openssl-dev
```

For uwsgi compilation you'll need:

```bash
apt-get install libxml2-dev python-dev
```


Usage
-----

To only create the package run:

```bash
git clone https://github.com/lemr/services.git
cd services
cd nginx
make pkgbuild && make pkgclean
```


Eventually to create and install the package run:

```bash
git clone https://github.com/lemr/services.git
cd services
cd nginx
make pkginst && make pkgclean
```


Notes
-----

* Installs all to /var/www/(nginx|uwsgi)-compiled
* Only creates init scripts to /etc/init.d/ but does NOT add them to rc.d and does not start them by default
* Configuration can be found in /var/www/(nginx|uwsgi)-compiled/conf


Please send me any missing dependencies.
