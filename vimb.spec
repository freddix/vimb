Summary:	Vim-like browser
Name:		vimb
Version:	2.8
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	https://github.com/fanglingsu/vimb/archive/%{version}.tar.gz
# Source0-md5:	32cdc9caa2031e4ad4f28dc4cd3b1fbc
BuildRequires:	gtk+3-webkit-devel
BuildRequires:	libsoup-devel
BuildRequires:	pkg-config
Requires:	glib-networking
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vimb is a fast and lightweight vim like web browser based on the
webkit web browser engine and the GTK toolkit. Vimb is modal like
the great Vim editor and also easily configurable during runtime.
Vimb is mostly keyboard driven and does not detract you from your
daily work.

%prep
%setup -q

%build
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make} clean
%{__make} GTK=3

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vimb
%{_mandir}/man1/vimb.1*

