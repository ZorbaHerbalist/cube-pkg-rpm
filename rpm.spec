Summary: TheRPM package management system
Name: rpm
Version: 4.17.1.1
Release: 1
License: GPL 2
Source0: http://ftp.osuosl.org/pub/rpm/releases/rpm-4.17.x/rpm-4.17.1.1.tar.bz2
Patch0: freebsd.patch
Patch1: freebsd-posix_spawnp.patch
Patch2: freebsd-libgcrypt-hack.patch

%description
The RPM Package Manager (RPM).

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CPPFLAGS="-I/usr/local/include" \
LDFLAGS="-L/usr/local/lib" \
LIBS="-lgetline -lz -lm" \
./configure --without-archive
gmake

%install

%files

%changelog
