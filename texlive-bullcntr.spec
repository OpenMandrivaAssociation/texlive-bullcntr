Name:		texlive-bullcntr
Version:	15878
Release:	2
Summary:	Display list item counter as regular pattern of bullets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bullcntr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bullcntr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bullcntr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bullcntr.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bullcntr package defines the command bullcntr, which can be
thought of as an analogue of the \fnsymbol command: like the
latter, it displays the value of a counter lying between 1 and
9, but uses, for the purpose, a regular pattern of bullets.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
