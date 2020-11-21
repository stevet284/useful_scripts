Summary: Utility scripts for testing RPM creation
Name: test-utils
Version: 1.0.0
Release: 1
License: GPL
URL: https://github.com/stevet284/useful_scripts
Group: System
Packager: SteveT
Requires: bash
BuildRoot: ~/rpmbuild/

%description
A collection of utility scripts for testing RPM creation.

%prep
################################################################################
# Create the build tree and copy the files from the development directories    #
# into the build tree.                                                         #
################################################################################
echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/

cp /root/useful_scripts/bash/* $RPM_BUILD_ROOT/usr/local/bin

exit

%files
%attr(0755, root, root) /usr/local/bin/*

%pre

%post

