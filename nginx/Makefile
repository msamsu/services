BUILDDIR=./build
COPY=rsync -a --exclude .svn
PKGNAME=`head -n 1 debian/changelog |cut -d\  -f1`
PKGVER=`head -n 1 debian/changelog |grep -oE "[0-9.]+"`

INSTALL_DIR='/var/www/nginx-compiled'

NGINX_VERSION='1.2.0'


all:
	mkdir -p ${BUILDDIR}/bin ${BUILDDIR}/conf ${BUILDDIR}/etc
	rm -rf src && mkdir -p src/compiled
	cd src && wget 'http://nginx.org/download/nginx-$(NGINX_VERSION).tar.gz'
	cd src && tar xf nginx-$(NGINX_VERSION).tar.gz
	cd src/nginx-$(NGINX_VERSION) && ./configure --prefix=../compiled \
                  --with-cc-opt="-DNGX_HAVE_ACCEPT4=0" \
		  --error-log-path=$(INSTALL_DIR)/log/error.log \
		  --pid-path=/var/run/nginx-compiled.pid \
		  --lock-path=/var/lock/nginx-compiled \
		  --http-log-path=$(INSTALL_DIR)/log/access.log \
		  --http-client-body-temp-path=$(INSTALL_DIR)/temp/body \
		  --http-proxy-temp-path=$(INSTALL_DIR)/temp/proxy \
		  --http-fastcgi-temp-path=$(INSTALL_DIR)/temp/fastcgi \
		  --http-uwsgi-temp-path=$(INSTALL_DIR)/temp/uwsgi \
		  --http-scgi-temp-path=$(INSTALL_DIR)/temp/scgi
	cd src/nginx-$(NGINX_VERSION) && make && make install
	${COPY} src/compiled/sbin/nginx ${BUILDDIR}/bin/
	${COPY} src/compiled/conf/* ${BUILDDIR}/conf/
	${COPY} etc/* ${BUILDDIR}/etc/

install:
	true

clean:
	rm -rf ${BUILDDIR}


pkgbuild:
	dpkg-buildpackage -b
	mkdir -p pkg
	mv ../${PKGNAME}_${PKGVER}*deb pkg/
	rm -f ../${PKGNAME}_${PKGVER}*changes
	echo "Package build OK"

pkginst: pkgbuild
	dpkg -i pkg/${PKGNAME}_${PKGVER}*deb
	echo "Package install OK"

pkgclean:
	./debian/rules clean

