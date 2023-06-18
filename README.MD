# How to Mod Persona 3 FES

[![Documentation Status](https://readthedocs.org/projects/persona-3-fes-modding-guide/badge/?version=latest)](https://persona-3-fes-modding-guide.readthedocs.io/en/latest/?badge=latest)

This GitHub repo holds all of the content for building the readthedocs
version of this guide.

The guide can be accessed below.

<https://persona-3-fes-modding-guide.readthedocs.io/en/latest/>

## Building

## Linux

``` sh
git clone https://github.com/alexankitty/Persona-3-FES-Modding-Guide
cd ./Persona-3-FES-Modding-Guide/docs
python -m venv ./virtual
source ./virtual/bin/activate
pip install -U sphinx
pip install -r ./source/requirements.txt
make html
deactivate
```

## Windows

cmd 
``` bat 
git clone
<https://github.com/alexankitty/Persona-3-FES-Modding-Guide> cd
.Persona-3-FES-Modding-Guidedocs python -m venv .virtual
.virtualScriptsactivate.bat pip install -U sphinx pip install -r
.sourcerequirements.txt .make.bat html deactivate
```

powershell
``` ps1
 git clone
<https://github.com/alexankitty/Persona-3-FES-Modding-Guide> cd
.Persona-3-FES-Modding-Guidedocs python -m venv .virtual
.virtualScriptsActivate.ps1 pip install -U sphinx pip install -r
.sourcerequirements.txt cmd /c .make.bat html deactivate
```