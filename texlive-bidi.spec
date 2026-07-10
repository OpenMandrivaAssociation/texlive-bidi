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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A convenient interface for typesetting bidirectional texts with plain
TeX and LaTeX, using XeTeX or LuaTeX. The package includes adaptations
for use with many other commonly-used packages.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bidi
%dir %{_datadir}/texmf-dist/source/latex/bidi
%dir %{_datadir}/texmf-dist/tex/latex/bidi
%doc %{_datadir}/texmf-dist/doc/latex/bidi/README
%doc %{_datadir}/texmf-dist/doc/latex/bidi/bidi-doc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bidi/bidi-logo.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/bidi.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bidi/bidisample2e.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/bidismall2e.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/gull.jpg
%doc %{_datadir}/texmf-dist/doc/latex/bidi/picture.jpg
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test-arydshln.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test-bidi.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test-brochure.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test-casualcv.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test-classiccv.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test-color.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test-supertabular.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test-tabular.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test-tabularx.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test-tabulary.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test1-colortbl.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test1-wrapfig.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test2-colortbl.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test2-wrapfig.tex
%doc %{_datadir}/texmf-dist/doc/latex/bidi/test3-wrapfig.tex
%doc %{_datadir}/texmf-dist/source/latex/bidi/bidi-doc-intro.ltx
%doc %{_datadir}/texmf-dist/source/latex/bidi/bidi-doc-latex-basics.ltx
%doc %{_datadir}/texmf-dist/source/latex/bidi/bidi-doc-latex-pkgs.ltx
%doc %{_datadir}/texmf-dist/source/latex/bidi/bidi-doc-latex-pkgsupport.ltx
%doc %{_datadir}/texmf-dist/source/latex/bidi/bidi-doc-latex-programming.ltx
%doc %{_datadir}/texmf-dist/source/latex/bidi/bidi-doc-plain-basics.ltx
%doc %{_datadir}/texmf-dist/source/latex/bidi/bidi-doc-plain-programming.ltx
%doc %{_datadir}/texmf-dist/source/latex/bidi/bidi-doc-preamble.ltx
%doc %{_datadir}/texmf-dist/source/latex/bidi/bidi-doc-title.ltx
%doc %{_datadir}/texmf-dist/source/latex/bidi/bidi-doc.ltx
%doc %{_datadir}/texmf-dist/source/latex/bidi/bidi.dtx
%doc %{_datadir}/texmf-dist/source/latex/bidi/bidi.ins
%{_datadir}/texmf-dist/tex/latex/bidi/adjmulticol-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/algorithm2e-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/amsart-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/amsbook-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/amsmath-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/amstext-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/amsthm-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/array-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/article-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/artikel1-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/artikel2-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/artikel3-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/arydshln-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamer-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerbaseauxtemplates-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerbaseboxes-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerbasecolor-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerbasecompatibility-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerbaseframecomponents-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerbaseframesize-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerbaselocalstructure-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerbasemisc-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerbasenavigation-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerbaseoverlay-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerinnerthemecircles-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerinnerthemedefault-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerinnerthemefocus-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerinnerthemeinmargin-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerinnerthememetropolis-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerinnerthemerectangles-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerinnerthemerounded-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerouterthemedefault-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerouterthemefocus-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerouterthemeinfolines-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerouterthememetropolis-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerouterthememiniframes-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerouterthemeshadow-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerouterthemesidebar-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerouterthemesmoothbars-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerouterthemesmoothtree-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerouterthemesplit-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerouterthemetree-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerthemeHannover-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/beamerthemeSingapore-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/bidi-bibitem.pdf
%{_datadir}/texmf-dist/tex/latex/bidi/bidi-logo.pdf
%{_datadir}/texmf-dist/tex/latex/bidi/bidi-media9.sty
%{_datadir}/texmf-dist/tex/latex/bidi/bidi-perpage.sty
%{_datadir}/texmf-dist/tex/latex/bidi/bidi.sty
%{_datadir}/texmf-dist/tex/latex/bidi/bidi.tex
%{_datadir}/texmf-dist/tex/latex/bidi/bidi2in1.sty
%{_datadir}/texmf-dist/tex/latex/bidi/bidicode.sty
%{_datadir}/texmf-dist/tex/latex/bidi/bidiftnxtra.sty
%{_datadir}/texmf-dist/tex/latex/bidi/bidimoderncv.cls
%{_datadir}/texmf-dist/tex/latex/bidi/bidipoem.sty
%{_datadir}/texmf-dist/tex/latex/bidi/biditools.sty
%{_datadir}/texmf-dist/tex/latex/bidi/biditufte-book.cls
%{_datadir}/texmf-dist/tex/latex/bidi/biditufte-handout.cls
%{_datadir}/texmf-dist/tex/latex/bidi/bidituftefloat.sty
%{_datadir}/texmf-dist/tex/latex/bidi/bidituftegeneralstructure.sty
%{_datadir}/texmf-dist/tex/latex/bidi/bidituftehyperref.sty
%{_datadir}/texmf-dist/tex/latex/bidi/bidituftesidenote.sty
%{_datadir}/texmf-dist/tex/latex/bidi/bidituftetitle.sty
%{_datadir}/texmf-dist/tex/latex/bidi/bidituftetoc.sty
%{_datadir}/texmf-dist/tex/latex/bidi/boek-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/boek3-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/book-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/bookest-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/breqn-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/cals-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/caption-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/caption3-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/color-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/colortbl-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/combine-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/crop-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/cuted-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/cutwin-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/cvthemebidicasual.sty
%{_datadir}/texmf-dist/tex/latex/bidi/cvthemebidiclassic.sty
%{_datadir}/texmf-dist/tex/latex/bidi/dblfnote-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/diagbox-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/draftwatermark-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/empheq-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/eso-pic-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/extarticle-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/extbook-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/extletter-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/extrafootnotefeatures-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/extreport-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/fancybox-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/fancyhdr-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/fix2col-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/fleqn-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/float-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/floatrow-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/flowfram-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/fnpct-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/footnote-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/footnotebackref-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/framed-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/ftnright-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/geometry-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/graphicx-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/hgeneric-testphase-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/hvfloat-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/hyperref-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/imsproc-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/latex-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/leqno-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/letter-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/lettrine-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/lineno-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/listings-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/longtable-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/lscape-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/mathtools-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/mdframed-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/media9-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/memoir-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/midfloat-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/minitoc-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/multicol-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/multienum-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/natbib-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/newfloat-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/nicematrix-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/ntheorem-hyper-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/ntheorem-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/overpic-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/pdfbase-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/pdflscape-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/pgfcorescopes.code-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/pgfsys-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/picinpar-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/plain-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/pstricks-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/quotchap-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/ragged2e-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/rapport1-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/rapport3-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/refrep-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/report-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/rotating-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/scrartcl-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/scrbook-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/scrreprt-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/sidecap-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/soul-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/stabular-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/subfigure-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/tabls-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/tabularx-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/tabulary-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/tc-xetex-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/tcolorbox-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/thmbox-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/titlesec-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/titletoc-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/tocbasic-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/tocbibind-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/tocloft-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/tocstyle-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/todonotes-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/wrapfig-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/xcolor-xetex-bidi.def
%{_datadir}/texmf-dist/tex/latex/bidi/xltxtra-xetex-bidi.def
