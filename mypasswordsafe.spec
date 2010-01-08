
%define name	mypasswordsafe
%define Name	MyPasswordSafe
%define version	20091018
%define rel	1

Summary:	Straight-forward, easy-to-use password manager
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	GPLv2+
Group:		Databases
URL:		http://www.semanticgap.com/myps/
# http://github.com/sneakin/mypasswordsafe/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		mypasswordsafe-debian-fixes.patch
Patch1:		mypasswordsafe-const-char.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel imagemagick libxscrnsaver-devel

%description
MyPasswordSafe is a straight-forward, easy-to-use password manager
that maintains compatibility with Password Safe files. MyPasswordSafe
has the following features:
- Safes are encrypted when they are stored to disk.
- Passwords never have to be seen, because they are copied to the
  clipboard
- Random passwords can be generated.
- Window size, position, and column widths are remembered.
- Passwords remain encrypted until they need to be decrypted at the
  dialog and file levels.
- A safe can be made active so it will always be opened when
  MyPasswordSafe starts.
- Supports Unicode in the safes
- Languages supported: English and French

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
%make PREFIX=%{_prefix}

%install
rm -rf %{buildroot}

%makeinstall PREFIX=%{buildroot}%{_prefix}
rm -rf %{buildroot}%{_prefix}/share/doc


install -d -m755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{Name}
Comment=Password Manager
Exec=%{_bindir}/%{Name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-Archiving-Other;Qt;Office;Database;Archiving;
EOF

install -m755 -d %{buildroot}%{_iconsdir} %{buildroot}%{_miconsdir}
install -m644 -D images/keys.png %{buildroot}%{_liconsdir}/%{name}.png
convert images/keys.png -resize 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert images/keys.png -resize 16x16 %{buildroot}%{_miconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc CHANGES README* doc/sshots doc/manual*.html
%{_bindir}/%{Name}
%{_datadir}/%{Name}
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


