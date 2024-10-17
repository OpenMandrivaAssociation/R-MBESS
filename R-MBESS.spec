%global packname  MBESS
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          3.3.3
Release:          1
Summary:          MBESS
Group:            Sciences/Mathematics
License:          GPLv2+
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core



Requires:         R-MASS R-sem R-boot R-nlme R-gsl R-lavaan R-parallel R-snow R-OpenMx 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 

BuildRequires:   R-MASS R-sem R-boot R-nlme R-gsl R-lavaan R-parallel R-snow R-OpenMx 
%description
MBESS implements methods that are especially useful to researchers working
within the behavioral, educational, and social sciences (both substantive
researchers and methodologists), Many of the methods contained within
MBESS are applicable to quantitative research in general,

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
