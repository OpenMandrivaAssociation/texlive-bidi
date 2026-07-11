%global tl_name bidi
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	26.01.08
Release:	%{tl_revision}.1
Summary:	Bidirectional typesetting in plain TeX and LaTeX, using XeTeX or LuaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/generic/bidi
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidi.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidi.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A convenient interface for typesetting bidirectional texts with plain
TeX and LaTeX, using XeTeX or LuaTeX. The package includes adaptations
for use with many other commonly-used packages.

