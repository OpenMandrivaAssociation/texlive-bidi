# revision 24680
# category Package
# catalog-ctan /macros/latex/contrib/bidi
# catalog-date 2011-11-28 11:55:23 +0100
# catalog-license lppl1.3
# catalog-version 11.150
Name:		texlive-bidi
Version:	11.150
Release:	2
Summary:	Support for bidirectional typesetting in plain TeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bidi
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidi.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidi.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A convenient interface for typesetting bidirectional texts with
plain TeX and LaTeX. The package includes adaptations for use
with many other commonly-used packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bidi/amsart-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/amsbook-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/amsmath-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/amsthm-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/array-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/article-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/artikel1-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/artikel2-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/artikel3-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/arydshln-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/bibitem.pdf
%{_texmfdistdir}/tex/latex/bidi/bidi.sty
%{_texmfdistdir}/tex/latex/bidi/bidi.tex
%{_texmfdistdir}/tex/latex/bidi/bidi2in1.sty
%{_texmfdistdir}/tex/latex/bidi/bidicode.sty
%{_texmfdistdir}/tex/latex/bidi/bidiftnxtra.sty
%{_texmfdistdir}/tex/latex/bidi/bidimoderncv.cls
%{_texmfdistdir}/tex/latex/bidi/bidipoem.sty
%{_texmfdistdir}/tex/latex/bidi/bidipresentation.cls
%{_texmfdistdir}/tex/latex/bidi/biditools.sty
%{_texmfdistdir}/tex/latex/bidi/biditufte-book.cls
%{_texmfdistdir}/tex/latex/bidi/biditufte-handout.cls
%{_texmfdistdir}/tex/latex/bidi/bidituftefloat.sty
%{_texmfdistdir}/tex/latex/bidi/bidituftegeneralstructure.sty
%{_texmfdistdir}/tex/latex/bidi/bidituftehyperref.sty
%{_texmfdistdir}/tex/latex/bidi/bidituftesidenote.sty
%{_texmfdistdir}/tex/latex/bidi/bidituftetitle.sty
%{_texmfdistdir}/tex/latex/bidi/bidituftetoc.sty
%{_texmfdistdir}/tex/latex/bidi/boek-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/boek3-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/book-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/bookest-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/breqn-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/caption-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/color-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/colortbl-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/combine-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/crop-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/cutwin-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/cvthemebidicasual.sty
%{_texmfdistdir}/tex/latex/bidi/cvthemebidiclassic.sty
%{_texmfdistdir}/tex/latex/bidi/dblfnote-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/draftwatermark-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/empheq-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/extarticle-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/extbook-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/extletter-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/extrafootnotefeatures.def
%{_texmfdistdir}/tex/latex/bidi/extreport-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/fancyhdr-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/fleqn-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/float-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/flowfram-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/footnote-luatex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/footnote-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/framed-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/graphicx-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/hvfloat-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/hyperref-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/leqno-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/letter-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/lettrine-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/listings-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/loadingorder-bidi.def
%{_texmfdistdir}/tex/latex/bidi/longtable-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/luatex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/memoir-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/minitoc-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/multicol-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/multienum-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/natbib-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/pdfpages-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/pgf-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/picinpar-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/plain-luatex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/plain-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/pstricks-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/quotchap-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/ragged2e-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/rapport1-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/rapport3-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/refrep-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/report-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/scrartcl-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/scrbook-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/scrlettr-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/scrreprt-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/sidecap-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/stabular-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/subfigure-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/tabls-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/tabulary-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/tikz-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/titlesec-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/titletoc-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/tocbibind-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/tocloft-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/tocstyle-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/wrapfig-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/xcolor-xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/xetex-bidi.def
%{_texmfdistdir}/tex/latex/bidi/xltxtra-xetex-bidi.def
%doc %{_texmfdistdir}/doc/latex/bidi/README
%doc %{_texmfdistdir}/doc/latex/bidi/bidi-logo.pdf
%doc %{_texmfdistdir}/doc/latex/bidi/bidi-logo.tex
%doc %{_texmfdistdir}/doc/latex/bidi/bidi.pdf
%doc %{_texmfdistdir}/doc/latex/bidi/bidisample2e.tex
%doc %{_texmfdistdir}/doc/latex/bidi/bidismall2e.tex
%doc %{_texmfdistdir}/doc/latex/bidi/gull.jpg
%doc %{_texmfdistdir}/doc/latex/bidi/picture.jpg
%doc %{_texmfdistdir}/doc/latex/bidi/presentation-sample.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test-arydshln.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test-bidi.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test-brochure.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test-casualcv.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test-classiccv.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test-color.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test-supertabular.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test-tabular.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test-tabularx.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test-tabulary.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test1-colortbl.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test1-wrapfig.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test2-colortbl.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test2-wrapfig.tex
%doc %{_texmfdistdir}/doc/latex/bidi/test3-wrapfig.tex
#- source
%doc %{_texmfdistdir}/source/latex/bidi/bidi.dtx
%doc %{_texmfdistdir}/source/latex/bidi/bidi.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
