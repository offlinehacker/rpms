%global extuuid    space-bar@luchrioh
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-space-bar
Version:        5
Release:        0
Summary:        GNOME Shell workspace switcher extension

License:        GPLv2+
URL:            https://github.com/christopher-l/space-bar
Source0:        https://extensions.gnome.org/extension-data/space-barluchrioh.v5.shell-extension.zip#/%{name}-%{version}.zip

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 4.42.0


%description
GNOME Shell extension that shows workspaces buttons in top panel 


%prep
%autosetup -c -n %{name}-%{version} -p 1


%build


%install
mkdir -p %{buildroot}%{extdir}
cp -pr * %{buildroot}%{extdir}

# Install schema.
mkdir -p %{buildroot}%{gschemadir}
cp -pr schemas/*gschema.xml %{buildroot}%{gschemadir}

# Cleanup unused files.
rm -fr %{buildroot}%{extdir}/{README*,schemas}


%files
%doc README.md
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
