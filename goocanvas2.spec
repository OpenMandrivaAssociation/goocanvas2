%define url_ver %(echo %version | cut -d. -f1,2)

%define oname	goocanvas
%define major	9
%define api	2.0
%define libname	%mklibname %{oname} %{api} %{major}
%define girname	%mklibname %{oname}-gir %{api}
%define devname	%mklibname -d %{oname} %{api}

Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Name:		%{oname}2
Version:	2.0.4
Release:	2
Group:		Development/GNOME and GTK+
License:	LGPL+
URL:		http://sourceforge.net/projects/goocanvas
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{url_ver}/%{oname}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk-doc)

%description
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for 
drawing. It has a model/view split, and uses interfaces for canvas items and 
views, so you can easily turn any application object into canvas items.

%package -n %{libname}
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		System/Libraries
Suggests:	%{name}-i18n >= %{version}
Provides:	lib%{name} = %{version}-%{release}
Obsoletes:	%{_lib}goocanvas-2.0_9 < 2.0.1

%description -n %{libname}
This package contains the shared library for goocanvas.

%package i18n
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		System/Internationalization

%description i18n
This package contains the translations for goocanvas.

%package -n %{devname}
Summary:	New canvas widget for GTK+ that uses the cairo 2D library
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}goocanvas-2.0-devel < 2.0.1

%description -n %{devname}
This package contains the development libraries, include files 
and documentation.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x \
	--enable-introspection=yes \
	--disable-static

%make LIBS=-lm

%install
%make_install

%find_lang %{name}

%files -n %{libname}
%doc README COPYING AUTHORS
%{_libdir}/lib%{oname}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GooCanvas-%{api}.typelib

%files i18n -f %{name}.lang

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{oname}-%{api}
%{_libdir}/lib%{oname}-%{api}.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/GooCanvas-%{api}.gir

