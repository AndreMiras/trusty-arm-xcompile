#!/usr/bin/env python2
import glob
import shutil
import argparse
import subprocess


DOWNLOAD_DIRECTORY = "/root/downloads"
SHARED_DIRECTORY = "/shared"
ARCH = 'armel'


def prepare_download():
    """
    Creates local download directories.
    """
    subprocess.call(['mkdir', '-p', DOWNLOAD_DIRECTORY])

def copy_deb_files_to_host():
    deb_files = glob.glob("%s/*.deb" % (DOWNLOAD_DIRECTORY))
    for deb_file in deb_files:
        shutil.copy(deb_file, SHARED_DIRECTORY)

def cross_compile(package):
    """
    apt-get -y build-dep cppunit
    apt-get source cppunit
    ARCH=armel
    dpkg-buildpackage -a$ARCH -rfakeroot -uc
    """
    prepare_download()
    # moves to DOWNLOAD_DIRECTORY before downloading sources
    # subprocess.call(['cd', DOWNLOAD_DIRECTORY])
    # prepares package dependencies
    subprocess.call(['apt-get', '-y', 'build-dep', package])
    # downloads package sources
    subprocess.call(['apt-get', 'source', package], cwd=DOWNLOAD_DIRECTORY)
    # retrieves the source directory name usually package-*
    source_directory = glob.glob("%s/%s-*" % (DOWNLOAD_DIRECTORY, package))[0]
    # builds the package
    subprocess.call(['dpkg-buildpackage', '-j4', '-a%s' % (ARCH), '-rfakeroot', '-uc'], cwd=source_directory)


def main():
    parser = argparse.ArgumentParser(description='Automates Ubuntu package cross compilation.')
    parser.add_argument(
            '--xcompile',
            help='cross compile a package, e.g. --xcompile cppunit')
    args = parser.parse_args()
    if args.xcompile:
        package = args.xcompile
        cross_compile(package)
        copy_deb_files_to_host()

if __name__ == "__main__":
    main()
