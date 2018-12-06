%global goipath         github.com/git-lfs/wildmatch
Version:                1.0.0

%gometa

# Hack to match name that will exist when Go macros are updated.
%global goname golang-github-git-lfs-wildmatch

Name:           %{goname}
Release:        1%{?dist}
Summary:        Pattern matching language for filepaths compatible with Git
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for building other packages
which use import path with %{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE.md
%doc README.md


%changelog
* Wed Oct 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to first tagged version

* Wed Aug 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.3.20180816gitb31c344
- Re-template against More Go Packaging guidelines
- Update to latest commit

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20180219git8a05186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 03 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20180219git8a05186
- Initial package
