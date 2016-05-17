Name:           fdk-aac
Version:        0.1.4
Release:        2%{?dist}
Summary:        Fraunhofer FDK AAC Codec Library

License:        FDK-AAC
URL:            http://sourceforge.net/projects/opencore-amr
Source0:        http://downloads.sourceforge.net/opencore-amr/%{name}-%{version}.tar.gz


%description
The Fraunhofer FDK AAC Codec Library ("FDK AAC Codec") is software that
implements the MPEG Advanced Audio Coding ("AAC") encoding and decoding
scheme for digital audio.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%prep
%setup -q


%build
%configure \
  --disable-silent-rules \
  --disable-static

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc ChangeLog NOTICE
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc documentation/*.pdf
%dir %{_includedir}/fdk-aac
%{_includedir}/fdk-aac/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sat May 14 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1.4-2
- Rebuilt for DeskOS

* Tue Mar 22 2016 Nux <rpm@li.nux.ro> - 0.1.4-1
- update to 0.1.4

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1.2-1
- Update to 0.1.2

* Thu Mar 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1.1-1
- Initial spec
