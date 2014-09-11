Name:           ros-indigo-ecl-exceptions
Version:        0.61.0
Release:        0%{?dist}
Summary:        ROS ecl_exceptions package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ecl_exceptions
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-ecl-config
Requires:       ros-indigo-ecl-errors
Requires:       ros-indigo-ecl-license
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ecl-config
BuildRequires:  ros-indigo-ecl-errors
BuildRequires:  ros-indigo-ecl-license

%description
Template based exceptions - these are simple and practical and avoid the
proliferation of exception types. Although not syntatactically ideal, it is
convenient and eminently practical.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Sep 12 2014 Daniel Stonier <d.stonier@gmail.com> - 0.61.0-0
- Autogenerated by Bloom

