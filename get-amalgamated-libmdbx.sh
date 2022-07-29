#!/bin/bash

# Configurables:
GIT_TAG='v0.11.7'
PKG_NAME='libmdbx'
REPO_URL='https://gitflic.ru/project/erthink/libmdbx.git'
WARNINGS_ARE_NOT_ERRORS='true'

# Bail on error:
set -e

# Grab the source:
rm -rf ${PKG_NAME}-src
git clone $REPO_URL ${PKG_NAME}-src
cd ${PKG_NAME}-src
git checkout -b ${PKG_NAME}-${GIT_TAG} tags/${GIT_TAG}

# Temporarily turn off treatment of warnings as errors (set only if needed):
if ! [ "$WARNINGS_ARE_NOT_ERRORS" = 'true' ]; then
	sed -e 's/-Werror//g' GNUmakefile > GNUmakefile.tmp && mv GNUmakefile.tmp GNUmakefile
	git commit -a -m 'Turned off warnings as errors'
fi

# Build specific stuff:
make release-assets
tarfile=$(ls ${PKG_NAME}*.tar.gz)
zipfile=$(ls ${PKG_NAME}*.zip)

mv "${tarfile}" "../amalgamated-sources/${PKG_NAME}-${GIT_TAG}.tar.gz"
mv "${zipfile}" "../amalgamated-sources/${PKG_NAME}-${GIT_TAG}.zip"

cd ..
rm -rf ${PKG_NAME}-src
