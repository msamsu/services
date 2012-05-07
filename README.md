Linux web services .deb package sources
=======================================

 * Nginx
http://wiki.nginx.org/Main

 * uWsig
http://projects.unbit.it/uwsgi/


.deb packages sources do:

 * downloads source
 * compiles it
 * creates .deb package
 * and eventually installs it


Installs all to /var/www/(nginx|uwsgi)-compiled
Only creates init scripts to /etc/init.d/ but does NOT add them to rc.d by default
Configuration can be found in /var/www/(nginx|uwsgi)-compiled/conf


To only create the package run:

```bash
git clone git@github.com:lemr/services.git
cd services
cd nginx
make pkgbuild && make pgkclean
```


Eventually to create and install the package run:

```bash
git clone git@github.com:lemr/services.git
cd services
cd nginx
make pkginst && make pgkclean
```


Please send me any missing dependencies.