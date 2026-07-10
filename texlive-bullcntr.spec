%global tl_name bullcntr
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.04
Release:	%{tl_revision}.1
Summary:	Display list item counter as regular pattern of bullets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bullcntr
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bullcntr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bullcntr.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bullcntr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bullcntr package defines the command bullcntr, which may be thought
of as an analogue of the \fnsymbol command: like the latter, it displays
the value of a counter lying between 1 and 9, but uses, for the purpose,
a regular pattern of bullets.

