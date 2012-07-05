%define oname goocanvas

%define major		9
%define api		2.0
%define gmajor		2.0
%define libname		%mklibname %{oname} %{api} %{major}
%define develname	%mklibname -d %{oname} %{api}
%define girname		%mklibname %{oname}-gir %{gmajor}

%define url_ver %(echo %version | cut -d. -f1,2)

Name:		goocanvas2
Version:	2.0.1
Release:	1
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		Development/GNOME and GTK+
License:	LGPL+
URL:		http://sourceforge.net/projects/goocanvas
Source0:	http://download.gnome.org/sources/%{oname}/%{url_ver}/%{oname}-%{version}.tar.bz2
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for 
drawing. It has a model/view split, and uses interfaces for canvas items and 
views, so you can easily turn any application object into canvas items.

%package -n %{libname}
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		System/Libraries
Requires:	%{name}-i18n >= %{version}
Provides:	lib%{name} = %{version}-%{release}
Obsoletes:	%{_lib}goocanvas-2.0_9 < 2.0.1

%description -n %{libname}
This package contains the shared library for goocanvas.

%package i18n
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		System/Internationalization

%description i18n
This package contains the translations for goocanvas.

%package -n %{develname}
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}goocanvas-2.0-devel < 2.0.1

%description -n %{develname}
This package contains the development libraries, include files 
and documentation.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x \
	--enable-introspection=yes \
	--disable-static
%make LIBS=-lm

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%find_lang %{name}

%files -n %{libname}
%doc README COPYING AUTHORS
%{_libdir}/lib%{oname}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GooCanvas-%{gmajor}.typelib

%files i18n -f %{name}.lang

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{oname}-%{api}
%{_libdir}/lib%{oname}-%{api}.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/GooCanvas-%{gmajor}.gir
