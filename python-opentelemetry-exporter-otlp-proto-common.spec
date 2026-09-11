Name:           python-opentelemetry-exporter-otlp-proto-common
# Pinned to 1.39.1 to match the OpenTelemetry stack (base opentelemetry-api is
# 1.39.1). This package pins opentelemetry-proto to its exact version, and the
# proto-grpc/proto-http exporters pin it to theirs, so the cluster moves together.
Version:        1.39.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        OpenTelemetry Protobuf encoding

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp-proto-common
Source:         %{pypi_source opentelemetry_exporter_otlp_proto_common}

BuildArch:      noarch
BuildRequires:  python3-devel
# The encoder modules (trace_encoder/metrics_encoder and _internal) import
# opentelemetry.sdk unconditionally at module load, but upstream's metadata only
# declares opentelemetry-proto, so the automatic dependency generator never emits
# a Requires for the SDK. Add it manually (see the Requires below); it is needed
# here so the import check can load those modules.
BuildRequires:  python3dist(opentelemetry-sdk)


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opentelemetry-exporter-otlp-proto-common' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-opentelemetry-exporter-otlp-proto-common
Summary:        %{summary}
# opentelemetry-sdk is a hard runtime dependency (the encoders import it at load)
# that upstream fails to declare, so the automatic generator does not pick it up.
Requires:       python3dist(opentelemetry-sdk)

%description -n python3-opentelemetry-exporter-otlp-proto-common %_description


%prep
%autosetup -p1 -n opentelemetry_exporter_otlp_proto_common-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files -l opentelemetry


%check
%pyproject_check_import


%files -n python3-opentelemetry-exporter-otlp-proto-common -f %{pyproject_files}


%changelog
%autochangelog
