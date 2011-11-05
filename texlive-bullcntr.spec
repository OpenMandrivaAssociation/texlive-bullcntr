# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/bullcntr
# catalog-date 2008-08-17 01:00:50 +0200
# catalog-license lppl
# catalog-version 0.04
Name:		texlive-bullcntr
Version:	0.04
Release:	1
Summary:	Display list item counter as regular pattern of bullets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bullcntr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bullcntr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bullcntr.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bullcntr.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The bullcntr package defines the command bullcntr, which can be
thought of as an analogue of the \fnsymbol command: like the
latter, it displays the value of a counter lying between 1 and
9, but uses, for the purpose, a regular pattern of bullets.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bullcntr/bullcntr.sty
%{_texmfdistdir}/tex/latex/bullcntr/bullenum.sty
%doc %{_texmfdistdir}/doc/latex/bullcntr/00readme.txt
%doc %{_texmfdistdir}/doc/latex/bullcntr/README
%doc %{_texmfdistdir}/doc/latex/bullcntr/bullcntr-man.pdf
%doc %{_texmfdistdir}/doc/latex/bullcntr/bullcntr-man.tex
%doc %{_texmfdistdir}/doc/latex/bullcntr/bullcntr-sam.tex
%doc %{_texmfdistdir}/doc/latex/bullcntr/bullenum-sam.tex
%doc %{_texmfdistdir}/doc/latex/bullcntr/manifest.txt
#- source
%doc %{_texmfdistdir}/source/latex/bullcntr/bullcntr.dtx
%doc %{_texmfdistdir}/source/latex/bullcntr/bullcntr.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
