#!/usr/bin/env python3

from __future__ import print_function
from pkg_resources import parse_version
import sys

libraries = {
    "python":     "3.6",
    "numpy":      "1.13.3",
    "pandas":     "0.23.0",
    "matplotlib": "2.1.1",
    "sklearn":    "0.19.1",
    "scipy":      "0.19.1",
    "seaborn":    "0.8.0",
    "statsmodels":    "0.9.0",
    "lxml":       "4.2.1"
}

installed = {}


missing=[]
old=[]

def helper(name, required_version):
    try:
        x = __import__(name)
    except Exception:        # ModuleNotFoundError: # does not work in Python 2
        x = None
    if x:
        if name == "lxml":
            from lxml import etree
            version = etree.__version__
        else:
            version = x.__version__
        
        if parse_version(version) < parse_version(required_version):
            old.append(name)
        installed[name] = (version, x.__file__)
    else:
        installed[name] = ("-", "-")
        missing.append(name)

def max_length(L):
    return max(len(x) for x in L)

python_version = ".".join(map(str, sys.version_info[:3]))
#print(python_version)
print("Python version:", sys.version.split('\n')[0])
for library, required_version in libraries.items():
    if library == "python":
        location = sys.executable
        installed[library] = (python_version, location)
        if parse_version(python_version) < parse_version(libraries[library]):
            old.append(library)
    else:
        helper(library, required_version)

library_length = max_length(["Library"] + list(installed.keys()))
required_length = max_length(["Required"] + list(libraries.values()))
installed_version_length = max_length(["Installed"] + [ version for version, location in installed.values() ])
#library_length = max([ len(library) for library in installed ])
#installed_version_length = max([ len(version) for version, location in installed.values() ])
#required_length = max([ len(required_version) for required_version in libraries.values() ])
#library_length = max(library_length, len("Library"))
#installed_version_length = max(installed_version_length, len("Installed"))
#required_length = max(required_length, len("Required"))

print("%-*s %*s %*s %s" % (library_length, "Library", installed_version_length, "Installed",
                           required_length, "Required", "Location"))
for library in installed:
    installed_version, location = installed[library]
    required = libraries[library]
    print("%-*s %*s %*s %s" % (library_length, library,
                               installed_version_length, installed_version,
                               required_length, required,
                               location))
print()


if missing:
    print("The following libraries are missing:")
    for library in missing:
        print(library)

print()

if old:
    print("The following libraries are too old:")
    for library in old:
        print(library)
#print(installed)

print()

if missing or old:
    print("Installation is not complete!")
else:
    print("Installation is complete!")
    
