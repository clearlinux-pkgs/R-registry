#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-registry
Version  : 0.5
Release  : 1
URL      : https://cran.r-project.org/src/contrib/registry_0.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/registry_0.5.tar.gz
Summary  : Infrastructure for R Package Registries
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n registry

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521193366

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521193366
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library registry
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library registry
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library registry
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library registry|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/registry/DESCRIPTION
/usr/lib64/R/library/registry/INDEX
/usr/lib64/R/library/registry/Meta/Rd.rds
/usr/lib64/R/library/registry/Meta/demo.rds
/usr/lib64/R/library/registry/Meta/features.rds
/usr/lib64/R/library/registry/Meta/hsearch.rds
/usr/lib64/R/library/registry/Meta/links.rds
/usr/lib64/R/library/registry/Meta/nsInfo.rds
/usr/lib64/R/library/registry/Meta/package.rds
/usr/lib64/R/library/registry/Meta/vignette.rds
/usr/lib64/R/library/registry/NAMESPACE
/usr/lib64/R/library/registry/R/registry
/usr/lib64/R/library/registry/R/registry.rdb
/usr/lib64/R/library/registry/R/registry.rdx
/usr/lib64/R/library/registry/demo/registry.R
/usr/lib64/R/library/registry/doc/index.html
/usr/lib64/R/library/registry/doc/registry.R
/usr/lib64/R/library/registry/doc/registry.Rnw
/usr/lib64/R/library/registry/doc/registry.pdf
/usr/lib64/R/library/registry/help/AnIndex
/usr/lib64/R/library/registry/help/aliases.rds
/usr/lib64/R/library/registry/help/paths.rds
/usr/lib64/R/library/registry/help/registry.rdb
/usr/lib64/R/library/registry/help/registry.rdx
/usr/lib64/R/library/registry/html/00Index.html
/usr/lib64/R/library/registry/html/R.css
