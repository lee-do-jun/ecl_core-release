Name:           ros-jade-ecl-concepts
Version:        0.61.4
Release:        0%{?dist}
Summary:        ROS ecl_concepts package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ecl_concepts
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-ecl-config
Requires:       ros-jade-ecl-license
Requires:       ros-jade-ecl-type-traits
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-ecl-config
BuildRequires:  ros-jade-ecl-license
BuildRequires:  ros-jade-ecl-type-traits

%description
Introduces a compile time concept checking mechanism that can be used most
commonly to check for required functionality when passing template arguments.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Oct 20 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.4-0
- Autogenerated by Bloom

