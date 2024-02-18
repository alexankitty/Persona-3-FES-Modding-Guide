Setting up Aemulus for Mods
===========================

.. note::
   If on Linux, replace instances of C:\\Emulation with ~/Documents/P3FMods where ~ refers to your home folder.
   If for some reason you haven't installed aemulus, go to :doc:`linuxaemulussetup`.
   Replace instances of opening the Aemulus exe with opening up Aemulus from your launcher.


-  1.    Navigate back to your C:\\Emulation (Or whatever you named it)
   folder you made earlier using then double click your Aemulus folder.

| 
| |image43|

-  2.    Double click **"AemulusPackageManager.exe"** to open it.

| 
| |image44|

-  3.    When you first open it, it will default to **"Persona 4
   Golden."** Click the game icon and change it to **"Persona 3 FES."**

| 
| |image45|
| |image46|
| |image47|

-  4.    Click the gear icon to open the settings screen.

| 
| |image48|
| |image49|

-  5.    To ensure your paths are completely accurate, this guide
   recommends using the **"Browse"** button for each line, the paths
   this guide will use will be included at the end of this section, but
   do note if you changed the name of your Emulation, MOD, ROM, or PCSX2
   folders, or set this up on a different drive, your paths will differ
   slightly.

| 
| |image50|

-  6.    Setting up your **"Output"** folder. Click **"Browse"**, in the
   window that pops up
-  a.    click “This PC”, then double click your C drive
-  b.    then double click Emulation, then double click MOD
-  c.    then you’ll have an empty folder, which you’ll click **"Select
   Folder"** at the bottom right.

| 
| |image51|
| |image52|
| |image53|
| |image54|
| |image55|
| |image56|
| If done right, your output folder will now be populated with
  C:\\Emulation\\MOD (or whichever folder you picked.)
| |image57|

.. note::
   If on Linux, PCSX2 stores Cheats and Textures in **"~/.config/PCSX2"**. Replace instances of Cheats and Textures path with
   **"Z:\home\<username>\.config\PCSX2\Cheats"** and  **"Z:\home\<username>\.config\PCSX2\Textures\SLUS-21621\replacements"**.


-  7.    Setting up the **"Cheats"** and **"Cheats WS"** folder, you’ll
   click **"Browse"** next to cheats. Since your C:\\Emulation\\MOD
   folder is the last one selected, it will automatically open to that
   path. Note: **Cheats_WS** no longer exists in new pcsx2 installs.
-  a.    Click emulation at the top,
-  b.    Then double click PCSX2.
-  c.    Double click cheats.
-  d.    Then click Select Folder.
-  e.    Repeat these steps for Cheats WS by clicking browse.
-  f.    Then click the PCSX2 Button up top.
-  g.    Then click the cheats_ws folder.
-  h.    Then click **"Select folder."**

| 
| |image58|
| |image59|
| |image60|
| |image61|
| |image62|

-  8.    Next we’ll set the textures folder path. If you’re not using
   P3HD for whatever reason, this step may be skipped.
-  a.    Click **"Browse"** next to the **"Textures"** line.
-  b.    Click PCSX2 at the top.
-  c.    Double click the textures folder.
-  d.    Double click SLUS-21621 (if it doesn’t exist, right click > new
   > folder and give it that name, then double click it – if you had to
   do this step, you should probably go back and follow the Persona 3 HD
   Overhaul steps as the folder was made during that process).
-  e.    Then double click replacements.
-  f.    Then click **"Select Folder."**

| 
| |image67|
| |image68|
| |image69|
| |image70|\ |image71|
| |image72|

-  9.    Next we’re going to select the **"PCSX2.exe path"** (this is
   technically optional but included for completeness sake). This step
   is done out of order to make it easier to follow the directory
   structures.
-  a.    Click **"Browse"** on the **"PCSX2.exe"** line.
-  b.    Then click the PCSX2 button in the address bar at the top.
-  c.    Then double click your pcsx2-qt.exe (In some cases it may be
   named pcsx2-qt-av2.exe instead). Please be aware that Aemulus
   launching is busted at the time of this writing. Do not use the
   launch option via Aemulus. Instead either launch the game through
   steam, create your own shortcut to launch the game, or start the game
   via PCSX2.

| 
| |image73|
| |image74|
| |image75|

-  10.    Next we will be selecting your **"P3F ISO path."**
-  a.    Click **"Browse"** on the **"P3F ISO"** path line.
-  b.    Then click Emulation in the address bar at the top.
-  c.    Then double click ROM.
-  d.    Then double click your Persona 3 FES.iso file.

| 
| |image76|
| |image77|
| |image78|
| |image79|

-  11.    Next, we’ll set the ELF path.
-  a.    Click **"Browse"** on the **"P3F ELF path"** line.
-  b.    Click emulation in the address bar at the top.
-  c.    Then double click the MOD folder.
-  d.    Then double click your Persona 3 FES.ELF file.

| 
| |image80|
| |image81|
| |image82|
| |image83|

-  12.   Next, in Aemulus settings, click the **"Delete Old Versions"**
   checkbox so that it is checked. Any time a mod is updated, the old
   package is removed. (Explanation: Aemulus caches old versions of
   packages but hides them in the interface, this will reduce the amount
   of space required for your install. Anytime there is a mod update, it
   is worth checking the mod page prior to updating in the event of any
   breaking issues.)

| 
| |image84|

-  13.    Next, we’re going to unpack the base files. The reason for
   doing this is to enable an Aemulus feature called BIN merging. This
   effectively increases mod cross compatibility when utilized. Click
   the **"Unpack Base Files"** button in the settings screen.

| 
| |image85|

-  14.    The application will seemingly lock up, but in the log you’ll
   see some output from it showing that its extracting files. Just hang
   tight and wait for it to finish.

| 
| |image86|

-  15.    Once done Aemulus will give you a window saying **“Finished
   Unpacking”** click **"OK"** on that and now we can move to installing
   mods.

| 
| |image87|

Oh no I got a prequisites error when unpacking base files
---------------------------------------------------------

| 
| This specific error actually can be thrown for reasons other than not
  having the prerequisites installed. The utilities used for Persona 3
  FES do not require anything else to be installed. More likely the case
  is that you do not have enough storage space to unpack the files.
  Please check the amount of space available for the drive you have
  Aemulus on, and free up space if needs be. Persona 3 FES's base files
  require approximately 1GB worth of free space.

.. |image43| image:: https://i.imgur.com/2dlFGLy.png
.. |image44| image:: https://i.imgur.com/ugVWT46.png
.. |image45| image:: https://i.imgur.com/gyI74kV.png
.. |image46| image:: https://i.imgur.com/KwML3aL.png
.. |image47| image:: https://i.imgur.com/2iIPPvh.png
.. |image48| image:: https://i.imgur.com/U259AES.png
.. |image49| image:: https://i.imgur.com/NPtYNNY.png
.. |image50| image:: https://i.imgur.com/04eScoq.png
.. |image51| image:: https://i.imgur.com/GAp2HvK.png
.. |image52| image:: https://i.imgur.com/Gq0dx4J.png
.. |image53| image:: https://i.imgur.com/1XNTZEQ.png
.. |image54| image:: https://i.imgur.com/JOXOpHg.png
.. |image55| image:: https://i.imgur.com/44awjh8.png
.. |image56| image:: https://i.imgur.com/MWFQAL3.png
.. |image57| image:: https://i.imgur.com/4lQqz7O.png
.. |image58| image:: https://i.imgur.com/pI9SuYm.png
.. |image59| image:: https://i.imgur.com/32EKjee.png
.. |image60| image:: https://i.imgur.com/HXczZU6.png
.. |image61| image:: https://i.imgur.com/yjLJIQt.png
.. |image62| image:: https://i.imgur.com/verle50.png
.. |image63| image:: https://i.imgur.com/TY41cYF.png
.. |image64| image:: https://i.imgur.com/AGodGUL.png
.. |image65| image:: https://i.imgur.com/JtntmwB.png
.. |image66| image:: https://i.imgur.com/kfnlv9i.png
.. |image67| image:: https://i.imgur.com/pgLD2Yb.png
.. |image68| image:: https://i.imgur.com/SXBens1.png
.. |image69| image:: https://i.imgur.com/0GfgCeW.png
.. |image70| image:: https://i.imgur.com/gcZQvnQ.png
.. |image71| image:: https://i.imgur.com/wZ1fT1s.png
.. |image72| image:: https://i.imgur.com/5rfCw48.png
.. |image73| image:: https://i.imgur.com/Y9CH8Uf.png
.. |image74| image:: https://i.imgur.com/ZtCSLhC.png
.. |image75| image:: https://i.imgur.com/14mASfQ.png
.. |image76| image:: https://i.imgur.com/mmlEVwP.png
.. |image77| image:: https://i.imgur.com/5J7Os6W.png
.. |image78| image:: https://i.imgur.com/4BypGvy.png
.. |image79| image:: https://i.imgur.com/CYpBbjs.png
.. |image80| image:: https://i.imgur.com/Wc5pPl6.png
.. |image81| image:: https://i.imgur.com/XesXf5O.png
.. |image82| image:: https://i.imgur.com/eETBSx9.png
.. |image83| image:: https://i.imgur.com/w7ecY5X.png
.. |image84| image:: https://i.imgur.com/SNGTfHD.png
.. |image85| image:: https://i.imgur.com/q1sLpwW.png
.. |image86| image:: https://i.imgur.com/IPxI11k.png
.. |image87| image:: https://i.imgur.com/k5318OE.png