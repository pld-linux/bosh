Summary:	Browsable output shell
Name:		bosh
Version:	0.6
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://dl.sourceforge.net/bosh/%{name}-%{version}.tar.gz
# Source0-md5:	975ef183ed4d2314186b1f2705d57c65
Patch0:		%{name}-ncurses.patch
URL:		http://bosh.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bosh stands for browsable output shell. This is a bit of a misnomer
because it isn't really a shell. What is does is store the output of a
specified program in a buffer, and provides a simple curses interface
to browse this buffer. Actions can be configured which can make use of
the contents of the currently selected line.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/bosh
%{_mandir}/man1/bosh.1*
