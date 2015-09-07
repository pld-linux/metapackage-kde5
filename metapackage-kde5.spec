Summary:	K Desktop Environment 5 with additional packages
Summary(pl.UTF-8):	Środowisko graficzne KDE5 z dodatkowymi pakietami
Name:		metapackage-kde5
Version:	5
Release:	0.1
License:	GPL/LGPL
Group:		X11/Applications
Requires:	ka5-konsole
Requires:	kf5-kded
Requires:	kf5-kinit
Requires:	kf5-krunner
Requires:	kf5-plasma-framework
Requires:	kf5-solid
Requires:	kp5-breeze
Requires:	kp5-kmenuedit
Requires:	kp5-milou
Requires:	kp5-plasma-desktop
Requires:	kp5-plasma-workspace
Requires:	kp5-polkit-kde-agent
Requires:	kp5-systemsettings
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Desktop Environment 5 with additional packages (metapackage).

%description -l pl.UTF-8
Środowisko graficzne KDE5 z dodatkowymi pakietami (metapakiet).

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
