Name:		texlive-halloweenmath
Version:	52602
Release:	2
Summary:	Scary and creepy math symbols with AMS-LaTeX integration
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/halloweenmath
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/halloweenmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/halloweenmath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/halloweenmath.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a handful of commands for typesetting
mathematical symbols of various kinds, ranging from 'large'
operators to extensible arrow-like relations and growing
arrow-like math accents that all draw from the classic
Halloween-related iconography (pumpkins, witches, ghosts, cats,
and so on) while being, at the same time, seamlessly integrated
within the rest of the mathematics produced by (AmS-)LaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/halloweenmath
%{_texmfdistdir}/tex/latex/halloweenmath
%doc %{_texmfdistdir}/doc/latex/halloweenmath

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
