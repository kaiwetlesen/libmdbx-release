#!/bin/bash

set -e

GIT_TAG='v0.11.6'
PKG_NAME='libmdbx'
REPO_URL='https://gitflic.ru/project/erthink/libmdbx.git'

rm -rf ${PKG_NAME}-src
git clone $REPO_URL ${PKG_NAME}-src
cd ${PKG_NAME}-src
git checkout -b ${PKG_NAME}-${GIT_TAG} tags/${GIT_TAG}

# Build specific stuff:
make release-assets
tarfile=$(ls ${PKG_NAME}*.tar.gz)
zipfile=$(ls ${PKG_NAME}*.zip)

mv "${tarfile}" "../amalgamated-sources/${PKG_NAME}-${GIT_TAG}.tar.gz"
mv "${zipfile}" "../amalgamated-sources/${PKG_NAME}-${GIT_TAG}.zip"

cd ..
rm -rf ${PKG_NAME}-src
