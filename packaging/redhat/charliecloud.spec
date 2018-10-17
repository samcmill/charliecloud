Name:       charliecloud
Version:    @VERSION@
Release:    1%{?dist}
Summary:    Lightweight user-defined software stacks for high-performance computing

Group:      System Environment/Base
License:    Apache-2.0
URL:        https://hpc.github.io/charliecloud
Source0:    %{name}-%{version}.tar.gz

ExclusiveOS:    linux
BuildRequires:  make >= 3.82
Requires:       rysnc >= 3.1.3, wget >= 1.14

BuildRoot:      %{?_tmppath}%{!?_tmppath:/var/tmp}/%{name}-%{version}-%{release}-root

%description
Charliecloud provides user-defined software stacks (UDSS) for high-performance computing
(HPC) centers. This “bring your own software stack” functionality addresses needs such as:

* software dependencies that are numerous, complex, unusual, differently configured, or
simply newer/older than what the center provides;

* build-time requirements unavailable within the center, such as relatively unfettered
internet access;

* validated software stacks and configuration to meet the standards of a particular
field of inquiry;

* portability of environments between resources, including workstations and other test
and development system not managed by the center;

* consistent environments, even archivally so, that can be easily, reliabily, and
verifiably reproduced in the future;

* and/or usability and comprehensibility.

For more information visit: https://hpc.github.io/charliecloud/

# Uncomment to prevent python compilation error on CentOS (#2235)
#%global __os_install_post    \
#    /usr/lib/rpm/redhat/brp-compress \
#    %{!?__debug_package:\
#    /usr/lib/rpm/redhat/brp-strip %{__strip} \
#    /usr/lib/rpm/redhat/brp-strip-comment-note %{__strip} %{__objdump} \
#    } \
#    /usr/lib/rpm/redhat/brp-strip-static-archive %{__strip} \
#    %{!?__jar_repack:/usr/lib/rpm/redhat/brp-java-repack-jars} \
#%{nil}

%prep
%setup -q

%build
%{__make} %{?mflags}

%install
%{__make} %{?mflags_install} install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT

%clean
rm -Rf $RPM_BUILD_ROOT
rm -Rf $LIBEXEC_DIR/charliecloud

%files
%doc LICENSE README.rst

# Helper scripts
%{_libexecdir}/%{name}/base.sh
%{_libexecdir}/%{name}/version.sh
%{_bindir}/ch-build
%{_bindir}/ch-build2dir
%{_bindir}/ch-docker2tar
%{_bindir}/ch-fromhost
%{_bindir}/ch-pull2dir
%{_bindir}/ch-pull2tar
%{_bindir}/ch-tar2dir

# Binaries
%{_bindir}/ch-run
%{_bindir}/ch-ssh

%changelog
