%{!?target_ver:         %global target_ver          0.11.4}
%{!?target_minor_ver:   %global target_minor_ver    0}
Name:       libmdbx
Version:    %{target_ver}.%{target_minor_ver}
Release:    1%{?dist}
Summary:    LibMDBX: An amazingly fast key-value database library

License:    OpenLDAP Public License Version 2.8
URL:        https://github.com/erthink/libmdbx
Source0:    https://github.com/erthink/libmdbx/releases/download/v%{target_ver}/libmdbx-amalgamated-%{target_ver}.tar.gz

Requires: libomp
BuildRequires:  cmake, gcc, gcc-c++, binutils, libomp-devel

%description
libmdbx is an extremely fast, compact, powerful, embedded, transactional
key-value store database, with permissive license. MDBX has a specific set of
properties and capabilities, focused on creating unique lightweight solutions
with extraordinary performance.


%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package    utils
Summary:    %{name} utilities
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
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%{?ldconfig_scriptlets}


%files
%license LICENSE
%doc README.md ChangeLog.md
%{_libdir}/*

%files devel
%license LICENSE
%doc README.md ChangeLog.md
%{_includedir}/*

%files utils
%license LICENSE
%doc README.md ChangeLog.md
%{_bindir}/*
%{_mandir}/*


%changelog
* Wed Feb 16 2022 Kai Wetlesen <kaiw@semiotic.ai>
- Revised spec
* Tue Feb 08 2022 Kai Wetlesen <kaiw@semiotic.ai>
- Initial specification file
