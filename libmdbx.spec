# Globals description:
# Target Package Version (target_pkgver): Indicates the current library version.
# Target SO Version (target_sover): Indicates the current shared-object ABI version, should correspond to major version of the library.
# Target Minor Version (target_minor_pkgver): Indicates a minor fix or patch to the library.
# Target Supplemental Version (target_suppl_ver): Indicates which version of the supplemental patches to use.
%define pkgver       %{?target_pkgver}%{!?target_pkgver:0.12.0}
%define sover        %{?target_sover}%{!?target_sover:0}
%define minor_pkgver %{?target_minor_pkgver}%{!?target_minor_pkgver:0}
%define suppl_ver    %{?target_suppl_ver}%{!?target_suppl_ver:0.1.2}
Name:       libmdbx
Vendor:     Erthink
Version:    %{pkgver}.%{minor_pkgver}
Release:    0%{?dist}
Summary:    An amazingly fast key-value database library

License:    OpenLDAP
URL:        https://gitflic.ru/project/erthink/libmdbx
Source0:    https://raw.githubusercontent.com/kaiwetlesen/%{name}-release/main/amalgamated-sources/%{name}-v%{pkgver}.tar.gz
Patch0:     https://raw.githubusercontent.com/kaiwetlesen/%{name}-release/v%{suppl_ver}/CMakeLists.txt.patch

BuildRequires:  cmake, gcc, gcc-c++, binutils

%description
MDBX is an extremely fast, compact, powerful, embedded, transactional key-value
store database, with permissive license. MDBX has a specific set of properties
and capabilities, focused on creating unique lightweight solutions with
extraordinary performance.


%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package    utils
Summary:    Utilities for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description    utils
The %{name}-utils package contains utilities for maintaining %{name} data files.


%prep
%autosetup -c


%build
%cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DMDBX_BUILD_TIMESTAMP:STRING=unknown .
%cmake_build --config Release


%install
%cmake_install --config Release
%__mkdir -p %{buildroot}%{_datadir}/licenses/%{name}/ %{buildroot}%{_datadir}/doc/%{name}/
%__cp LICENSE %{buildroot}%{_datadir}/licenses/%{name}/
%__cp README.md %{buildroot}%{_datadir}/doc/%{name}/
%__cp ChangeLog.md %{buildroot}%{_datadir}/doc/%{name}/
%__gzip %{buildroot}%{_mandir}/man1/mdbx_*


%{?ldconfig_scriptlets}


%files
%license LICENSE
%doc README.md ChangeLog.md
%{_libdir}/%{name}.so.%{sover}
%{_libdir}/%{name}.so.%{pkgver}

%files devel
%license LICENSE
%doc README.md ChangeLog.md
%{_includedir}/*
%{_libdir}/%{name}.so

%files utils
%license LICENSE
%doc README.md ChangeLog.md
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Fri Jun 29 2022 Kai Wetlesen <kaiw@semiotic.ai> - 0.12.0.0-0%{?dist}
- Bumped libmdbx version to latest

* Fri Jun 29 2022 Kai Wetlesen <kaiw@semiotic.ai> - 0.11.8.0-0%{?dist}
- Bumped libmdbx version to latest

* Fri Jun 29 2022 Kai Wetlesen <kaiw@semiotic.ai> - 0.11.7.0-0%{?dist}
- Bumped libmdbx version to latest

* Wed Apr 20 2022 Kai Wetlesen <kaiw@semiotic.ai> - 0.11.6.0.1%{?dist}
- Built new release based off GitFlic after Github's callous blanket shutdown of Russian developer accounts

* Thu Mar 24 2022 Kai Wetlesen <kaiw@semiotic.ai> - 0.11.6.0-0%{?dist}
- Bumped libmdbx version to latest
- Version bump addresses Linux kernel bug with kernel <= 4.19

* Thu Feb 24 2022 Kai Wetlesen <kaiw@semiotic.ai> - 0.11.5.0-0%{?dist}
- Bumped libmdbx version to latest

* Thu Feb 24 2022 Kai Wetlesen <kaiw@semiotic.ai> - 0.11.4.0-3%{?dist}
- Implemented library versioning

* Thu Feb 24 2022 Kai Wetlesen <kaiw@semiotic.ai> - 0.11.4.0-2%{?dist}
- Resolved rpmlint issues, improved building

* Wed Feb 16 2022 Kai Wetlesen <kaiw@semiotic.ai> - 0.11.4.0-1%{?dist}
- Revised spec to utilise cmake macros

* Tue Feb 08 2022 Kai Wetlesen <kaiw@semiotic.ai> - 0.11.4.0-0%{?dist}
- Initial specification file
