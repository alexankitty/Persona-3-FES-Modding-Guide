Installing Aemulus on Linux
===========================

Dependencies
------------
.. note::
    The installer script requires some dependencies to be installed in order for it to run right.
    Wine depends on lib32, make sure you have your multilib repos enabled, the below are some commands that should get everything working correctly, but you may or may not need more.
      
Arch Linux
----------
.. code-block:: sh

    sudo sed -i "/\[multilib\]/,/Include/"'s/^#//' /etc/pacman.conf
    sudo pacman -Sy
    sudo pacman -S curl wine winetricks p7zip unzip desktop-file-utils lib32-gnutls lib32-gst-plugins-base git

Debian/Ubuntu
-------------
.. code-block:: sh

    dpkg --add-architecture i386
    sudo apt install curl wine winetricks p7zip unzip desktop-file-utils gnutls git

Fedora
------
.. code-block:: sh

    sudo dnf install curl wine winetricks p7zip unzip desktop-file-utils gnutls gnutls.i686 git

Steam Deck and Other Immutable Distros Install
----------------------------------------------
1. Clone or click code, then download zip from https://github.com/alexankitty/aemulus-installer-linux.
2. If you downloaded the source zip, extract it.
3. Open your terminal and cd to the aemulus-installer-linux folder.
4. If you downloaded the source zip, run `chmod +x AemulusSetupProton.sh`.
5. Run the script with `./AemulusSetupProton.sh`.

Install
-------
1.  Run the above command that matches your distro, making any adjustments as needed.
2.  Run the following codeblock to download the installer repo and run the installer. 

    .. code-block:: sh

        git clone https://github.com/alexankitty/aemulus-installer-linux
        cd aemulus-installer-linux
        chmod +x ./AemulusSetup.sh
        ./AemulusSetup.sh

    |image160|

3.  Once the script has finished running, Aemulus can be opened by navigating to `Games > Aemulus Package Manager` in your launcher. An example of how this looks in KDE is provided. 
    |image161|

.. |image160| image:: https://imgur.com/Po17FKf.png
.. |image161| image:: https://imgur.com/2V5l7Eh.png