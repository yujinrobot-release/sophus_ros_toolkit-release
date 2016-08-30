Name:           ros-indigo-sophus-ros-conversions
Version:        0.1.2
Release:        0%{?dist}
Summary:        ROS sophus_ros_conversions package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-ecl-build
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-sophus
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-ecl-build
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-sophus

%description
Conversions between ros and sophus.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Aug 30 2016 Daniel Stonier <d.stonier@gmail.com> - 0.1.2-0
- Autogenerated by Bloom

* Thu Feb 11 2016 Daniel Stonier <d.stonier@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

* Thu Feb 11 2016 Daniel Stonier <d.stonier@gmail.com> - 0.1.0-2
- Autogenerated by Bloom

* Wed Feb 10 2016 Daniel Stonier <d.stonier@gmail.com> - 0.1.0-1
- Autogenerated by Bloom

* Wed Feb 10 2016 Daniel Stonier <d.stonier@gmail.com> - 0.1.0-0
- Autogenerated by Bloom

