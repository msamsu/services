BUILDDIR=./build
COPY=rsync -a --exclude .svn
PKGNAME=`head -n 1 debian/changelog |cut -d\  -f1`
PKGVER=`head -n 1 debian/changelog |grep -oE "[0-9.]+"`

INSTALL_DIR='/var/www/uwsgi-compiled'

UWSGI_VERSION='0.9.6.5'


all:
	mkdir -p ${BUILDDIR}/bin ${BUILDDIR}/conf ${BUILDDIR}/etc ${BUILDDIR}/default
	rm -rf src && mkdir src
	cd src && wget 'http://projects.unbit.it/downloads/uwsgi-$(UWSGI_VERSION).tar.gz'
	cd src && tar xf uwsgi-$(UWSGI_VERSION).tar.gz
	cd src/uwsgi-$(UWSGI_VERSION) && make
	${COPY} src/uwsgi-$(UWSGI_VERSION)/uwsgi ${BUILDDIR}/bin/
	${COPY} src/uwsgi-$(UWSGI_VERSION)/nginx/uwsgi_params ${BUILDDIR}/conf/
	${COPY} conf/* ${BUILDDIR}/conf/
	${COPY} etc/* ${BUILDDIR}/etc/
	${COPY} default/* ${BUILDDIR}/default/

install:
	true

clean:
	rm -rf ${BUILDDIR}

pkgbuild:
	dpkg-buildpackage -b -uc
	mkdir -p pkg
	mv ../${PKGNAME}_${PKGVER}*deb pkg/
	rm -f ../${PKGNAME}_${PKGVER}*changes
	echo "Package build OK"

pkginst: pkgbuild
	dpkg -i pkg/${PKGNAME}_${PKGVER}*deb
	echo "Package install OK"

pkgclean:
	./debian/rules clean

