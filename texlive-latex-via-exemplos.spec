Name:		texlive-latex-via-exemplos
Version:	63374
Release:	1
Summary:	A LaTeX course written in brazilian portuguese language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex-via-exemplos
License:	gpl2+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-via-exemplos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-via-exemplos.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX2e course written in brazilian portuguese
language.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/latex-via-exemplos

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
