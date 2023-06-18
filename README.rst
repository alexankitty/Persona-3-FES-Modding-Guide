How to Mod Persona 3 FES
========================
.. image:: https://readthedocs.org/projects/persona-3-fes-modding-guide/badge/?version=latest
    :target: https://persona-3-fes-modding-guide.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

This GitHub repo holds all of the content for building the readthedocs version of this guide.

The guide can be accessed below.

https://persona-3-fes-modding-guide.readthedocs.io/en/latest/

Building
--------

Linux
-----

.. code-block:: sh
    git clone https://github.com/alexankitty/Persona-3-FES-Modding-Guide
    cd ./Persona-3-FES-Modding-Guide/docs
    python -m venv ./virtual
    source ./virtual/bin/activate
    pip install -U sphinx
    pip install -r ./source/requirements.txt
    make html
    deactivate

Windows
-------

cmd
.. code-block:: bat
    git clone https://github.com/alexankitty/Persona-3-FES-Modding-Guide
    cd .\Persona-3-FES-Modding-Guide\docs
    python -m venv .\virtual
    .\virtual\Scripts\activate.bat
    pip install -U sphinx
    pip install -r .\source\requirements.txt
    .\make.bat html
    deactivate

powershell
.. code-block:: ps1
    git clone https://github.com/alexankitty/Persona-3-FES-Modding-Guide
    cd .\Persona-3-FES-Modding-Guide\docs
    python -m venv .\virtual
    .\virtual\Scripts\Activate.ps1
    pip install -U sphinx
    pip install -r .\source\requirements.txt
    cmd /c .\make.bat html
    deactivate