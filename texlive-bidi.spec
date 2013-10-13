# revision 31877
# category Package
# catalog-ctan /macros/xetex/latex/bidi
# catalog-date 2013-10-10 15:42:29 +0200
# catalog-license lppl1.3
# catalog-version 14.1
Name:		texlive-bidi
Version:	14.1
Release:	1
Summary:	Bidirectional typesetting in plain TeX and LaTeX, using XeTeX engine
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/bidi
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
%{_texmfdistdir}/tex/xelatex/bidi/amsart-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/amsbook-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/amsmath-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/amstext-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/amsthm-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/array-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/article-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/artikel1-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/artikel2-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/artikel3-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/arydshln-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/bibitem.pdf
%{_texmfdistdir}/tex/xelatex/bidi/bidi-longtable.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidi.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidi.tex
%{_texmfdistdir}/tex/xelatex/bidi/bidi2in1.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidicode.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidiftnxtra.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidimoderncv.cls
%{_texmfdistdir}/tex/xelatex/bidi/bidipoem.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidipresentation.cls
%{_texmfdistdir}/tex/xelatex/bidi/biditools.sty
%{_texmfdistdir}/tex/xelatex/bidi/biditufte-book.cls
%{_texmfdistdir}/tex/xelatex/bidi/biditufte-handout.cls
%{_texmfdistdir}/tex/xelatex/bidi/bidituftefloat.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidituftegeneralstructure.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidituftehyperref.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidituftesidenote.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidituftetitle.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidituftetoc.sty
%{_texmfdistdir}/tex/xelatex/bidi/boek-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/boek3-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/book-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/bookest-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/breqn-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/cals-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/caption-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/caption3-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/color-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/colortbl-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/combine-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/crop-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/cuted-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/cutwin-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/cvthemebidicasual.sty
%{_texmfdistdir}/tex/xelatex/bidi/cvthemebidiclassic.sty
%{_texmfdistdir}/tex/xelatex/bidi/dblfnote-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/draftwatermark-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/empheq-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/eso-pic-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/extarticle-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/extbook-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/extletter-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/extrafootnotefeatures-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/extreport-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/fancybox-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/fancyhdr-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/fix2col-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/fleqn-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/float-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/floatrow-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/flowfram-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/footnote-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/framed-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/ftnright-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/geometry-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/graphicx-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/hvfloat-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/hyperref-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/latex-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/leqno-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/letter-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/lettrine-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/listings-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/loadingorder-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/longtable-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/mdframed-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/memoir-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/midfloat-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/minitoc-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/multicol-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/multienum-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/natbib-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/newfloat-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/ntheorem-hyper-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/ntheorem-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/pdfpages-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/pgf-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/picinpar-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/plain-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/pstricks-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/quotchap-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/ragged2e-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/rapport1-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/rapport3-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/refrep-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/report-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/rotating-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/scrartcl-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/scrbook-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/scrlettr-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/scrreprt-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/sidecap-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/stabular-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/subfigure-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tabls-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tabulary-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/titlesec-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/titletoc-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tocbibind-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tocloft-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tocstyle-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/wrapfig-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/xcolor-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/xltxtra-xetex-bidi.def
%doc %{_texmfdistdir}/doc/xelatex/bidi/README
%doc %{_texmfdistdir}/doc/xelatex/bidi/bidi-logo.pdf
%doc %{_texmfdistdir}/doc/xelatex/bidi/bidi-logo.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/bidi.pdf
%doc %{_texmfdistdir}/doc/xelatex/bidi/bidisample2e.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/bidismall2e.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/gull.jpg
%doc %{_texmfdistdir}/doc/xelatex/bidi/picture.jpg
%doc %{_texmfdistdir}/doc/xelatex/bidi/presentation-sample.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test-arydshln.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test-bidi.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test-brochure.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test-casualcv.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test-classiccv.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test-color.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test-supertabular.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test-tabular.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test-tabularx.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test-tabulary.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test1-colortbl.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test1-wrapfig.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test2-colortbl.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test2-wrapfig.tex
%doc %{_texmfdistdir}/doc/xelatex/bidi/test3-wrapfig.tex
#- source
%doc %{_texmfdistdir}/source/xelatex/bidi/bidi.dtx
%doc %{_texmfdistdir}/source/xelatex/bidi/bidi.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
