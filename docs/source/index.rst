:og:description: The purpose of this guide is to help anyone be able to mod Persona 3 FES for the PS2.

#########################
How To Mod Persona 3 FES!
#########################

.. image:: images/how_to_mod.png

The purpose of this guide is to help anyone be able to mod Persona 3 FES for the PS2.
If you would prefer to view this guide all in one page, there is the :doc:`/singlepage` for your convenience.

Requirements
------------
- `PCSX2 Nightly v1.7.5397 <https://github.com/PCSX2/pcsx2/releases/tag/v1.7.5397>`_
- `Persona 3 FES: HD Overhaul (Recommended) <https://gamebanana.com/wips/63624>`_
- `Recommended list of mods (Dub/English Audio) <https://gamebanana.com/collections/376>`_
- `Recommended list of mods (Undub/Japanese Audio) <https://gamebanana.com/collections/380>`_
- `Latest Aemulus Release <https://github.com/TekkaGB/AemulusModManager/releases>`_
- `7-Zip <https://www.7-zip.org/download.html>`_
- Approximately 6GB of free space. 1GB if you're not using P3HD.
- Once Aemulus is installed:
   - `Unpatched/Clean Persona 3 FES ISO with CRC 94A82AAA <https://p3f.cep.one/install/dump-p3f-iso>`_
   - `USA/NTSC-U PS2 BIOS <https://p3f.cep.one/install/dump-ps2-bios>`_

.. note::

   This doc is in the process of being migrated from https://gamebanana.com/tuts/15959

   If you run into any problems, be sure to check :doc:`troubleshooting`. I'm also available in the `P3HD Discord Server <https://discord.gg/dvrn8xFBF6>`_ along with a few other good people that will be happy to help, just ask for help in `#p3hd-help <https://discord.com/channels/923959061467258890/923969627019681812>`_.

   CEP Is not compatible with P3HD, thus it is recommended to start from scratch if you want P3HD support. If you want to use CEP, the guide to do so is `here <https://p3f.cep.one/install/getting-started>`_.

   This guide will assume you're using windows, as Aemulus only runs under windows. For setting up mods under MacOS or for Linux/Steam Deck there will be an Extras section at the end of this guide. Do note that a Windows computer or VM is still required to setup your mods at the time of this writing.

   You also must have a clean Persona 3 FES USA ISO with CRC 94A82AAA, any other ISOs are not supported, and directions for making it work will not be provided as it can cause other issues.

   If you're playing on hardware, the contents of this guide will not be usable as Aemulus does not support running under hardware. For information on setting up mods to work on real hardware, please see `Nobodyinparticular's (Tutorial) Playing a Modded ISO on PS2 <https://gamebanana.com/tuts/14578>`_.

   At the time of this writing, launching the game is not supported through Aemulus due to a number of issues it has with mods and texture replacements. This guide will not cover launching the game through Aemulus, and instead will show you how to launch it through Steam and PCSX2.

   Some images may be difficult to see due to limited width, if you right click, then select "**Open Image in a New Tab**" you can view the full size image.

   Lastly, any links in this guide it's recommended you open them up in a new tab so you can keep the guide open. You can either middle click, or right click and click "**Open Link in a New Tab**."

   PCSX2 v1.7.5397 is the last mod supported build at the moment. Please do not use the latest until this is resolved.

Table of Contents
-----------------

.. toctree::
   :numbered:

   downloading
   installingprogs
   installingp3hd
   setupaemulus
   installingmods
   pcsx2setup
   addtosteam
   linuxaemulussetup
   otherplatforms
   emudeck
   otherpersonagames
   troubleshooting
   afterword


:doc:`/changelog` for your convenience.