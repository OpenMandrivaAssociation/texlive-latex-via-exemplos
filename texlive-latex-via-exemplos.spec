%global tl_name latex-via-exemplos
%global tl_revision 78322

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A LaTeX course written in Brazilian Portuguese language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex-via-exemplos
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-via-exemplos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-via-exemplos.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX2e course written in Brazilian Portuguese language.

