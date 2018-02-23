Name:           i3lock-multimonitor
Version:        abbdf6e857f329aa9ccf670d3787eaff41b48e08
Release:        1%{?dist}
Summary:        This is a script which uses a background image, resizes it to show correctly on any multimonitor setup.

License:        MIT
Source0:        https://github.com/tarnjotsingh/i3lock-multimonitor/archive/abbdf6e857f329aa9ccf670d3787eaff41b48e08.tar.gz

Requires:       i3lock
Requires:       ImageMagick

%global debug_package %{nil}

%description
The idea for this project was shamelessly copied from guimeira's i3lock-fancy-multimonitor.

It uses ImageMagick to resize the background image. You can replace this image to change background.

By using information from xrandr and basic math, this script supports multiple monitor setups, displaying the background image on all screens.

It caches the generated image for different screen sizes and xrandr output. So even though first lock command will take a second to finish, subsequent lock will be lighting fast.

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 i3lock-mm %{buildroot}/%{_bindir}/i3lock-mm

%files
%license LICENSE
%doc README.md
%{_bindir}/i3lock-mm

%changelog
* Wed Feb 21 2018 Sascha Marcel Schmidt <mail@saschaschmidt.net>
- Initial version of the package.
