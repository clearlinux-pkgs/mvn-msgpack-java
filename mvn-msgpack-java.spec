#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-msgpack-java
Version  : 0.8.16
Release  : 1
URL      : https://github.com/msgpack/msgpack-java/archive/0.8.16.tar.gz
Source0  : https://github.com/msgpack/msgpack-java/archive/0.8.16.tar.gz
Source1  : https://repo1.maven.org/maven2/org/msgpack/msgpack-core/0.8.16/msgpack-core-0.8.16.jar
Source2  : https://repo1.maven.org/maven2/org/msgpack/msgpack-core/0.8.16/msgpack-core-0.8.16.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: mvn-msgpack-java-data = %{version}-%{release}
Requires: mvn-msgpack-java-license = %{version}-%{release}

%description
MessagePack for Java
===
[MessagePack](http://msgpack.org) is a binary serialization format. If you need a fast and compact alternative of JSON, MessagePack is your friend. For example, a small integer can be encoded in a single byte, and short strings only need a single byte prefix + the original byte array. MessagePack implementation is already available in various lanaguages (See also the list in http://msgpack.org) and works as a universal data format.

%package data
Summary: data components for the mvn-msgpack-java package.
Group: Data

%description data
data components for the mvn-msgpack-java package.


%package license
Summary: license components for the mvn-msgpack-java package.
Group: Default

%description license
license components for the mvn-msgpack-java package.


%prep
%setup -q -n msgpack-java-0.8.16

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-msgpack-java
cp LICENCE.sbt-extras.txt %{buildroot}/usr/share/package-licenses/mvn-msgpack-java/LICENCE.sbt-extras.txt
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-msgpack-java/LICENSE.txt
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-msgpack-java/NOTICE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/msgpack/msgpack-core/0.8.16
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/msgpack/msgpack-core/0.8.16/msgpack-core-0.8.16.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/msgpack/msgpack-core/0.8.16
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/msgpack/msgpack-core/0.8.16/msgpack-core-0.8.16.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/msgpack/msgpack-core/0.8.16/msgpack-core-0.8.16.jar
/usr/share/java/.m2/repository/org/msgpack/msgpack-core/0.8.16/msgpack-core-0.8.16.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-msgpack-java/LICENCE.sbt-extras.txt
/usr/share/package-licenses/mvn-msgpack-java/LICENSE.txt
/usr/share/package-licenses/mvn-msgpack-java/NOTICE
