PCSX2 Setup
===========

-  1.    Re-use an open File Explorer window or open a new one, and
   navigate to C:\\Emulation\\PCSX2 or whatever you named those two
   folders earlier.

| 
| |image104|
| |image105|
| |image106|

-  2.    Download the HostFS cheat, and optionally if you’re playing
   16:9 the Wide cheat from
   `here <https://drive.google.com/drive/folders/1QsxslhJpkPKNOz7bgveneFKZ_nf9VzFG?usp=sharing>`__.
-  3.    Open another file explorer window and navigate to your
   downloads folder by clicking downloads under the Quick Access area.

| 
| |image107|

-  4.    In the PCSX2 folder, open the cheats folder

| 
| |image108|

-  5.    Drag and drop the HostFS and Wide (if you downloaded wide!)
   cheats into the PCSX2 cheats directory we just opened.

| 
| |image109|

-  6.    Don’t be alarmed if you see there are already cheats in the
   folder, as Aemulus put these in for you when you built your mods
   earlier. When finished your cheats folder should look similar to
   this, you may have more cheats depending on the mods you have
   installed.

| 
| |image110|

-  7.    Navigate back to your PCSX2 folder by clicking PCSX2 in the
   address bar.

| 
| |image111|

-  8.    Open the pcsx2-qt.exe (or pcsx2-qt-av2.exe) file.

| 
| |image112|

-  9.    Once PCSX2 is open click **“Add Game Directory…”**, if you’re
   using a previously used install of PCSX2, and you have a populated
   list, right click and click **“Add Search Directory...”**

| 
| |image113|
| If you don’t have the above option, then right click and click **“Add
  Search Directory…”**
| |image114|

-  10.    Click the emulation button at the top of the address bar, then
   click MOD, then click **"Select Folder."**

| 
| |image115|
| |image116|
| |image117|

-  11.    You’ll get a popup asking if you want to search recursively.
   Just click **"No"** for this one.

| 
| |image118|

-  12.    If completed correctly you should now have an entry that says
   something like **“PERSONA 3 FES”**, right click it, and click
   **"Properties."**

| 
| |image119|

-  13.    Click **"Browse..."** next to where it says **"Disc Path:"**

| 
| |image120|

-  14.    Click Emulation in the address bar at the top, then double
   click ROM, then double click your Persona 3 FES.iso file

| 
| |image121|
| |image122|
| |image123|

-  15.    Once that’s done, your game properties should look similar to
   this. Go ahead and click **"Close"** now.

| |image124|

-  16.    Next click **"Settings"**, then click **"Emulation."**

| 
| |image125|

-  17.    In the window that pops up, click the checkbox next to
   **“Enable Cheats”** along with **“Enable Host Filesystem”** so that
   they’re both checked like in the screenshot provided below.

| 
| |image126|

-  18.    Next, click on **"Graphics."**

| 
| |image127|

-  19.    Set **"Renderer"** to **"Vulkan"** if it’s available, or to
   **"Direct3D12"**, or 11 if it’s not.
-  a.    Set your adapter to match with your GPU name.
-  b.    Set your Aspect ratio to 4:3 if you want to play in the
   original aspect ratio, or 16:9 if you want to play in widescreen.
-  c.    FMV Aspect ratio should be set to 4:3, or if you’re using the
   true widescreen opening from Simply Better FMVs then this should be
   set to **"Widescreen (16:9)."**
-  d.    Make sure you keep **“Enable Widescreen Patches”** unchecked.

| 
| |image128|

-  20.    Next click the **"Rendering"** tab.
-  a.    Set "Internal Resolution" to either the same approximate size
   as your display, or to +1x more than it. In this example we’ll assume
   you’re using a 1920x1080 display, and will recommend you set 4x for
   Native. If you’re experiencing slowdowns, be sure to decrease this
   value. If you set it below 2x, you will no longer see an improvement
   from P3HD.
-  b.    If you’re on an AMD GPU, you also must set **"Texture
   Filtering"** to **“Bilinear (Forced)”** for anyone else it should be
   set to **“Bilinear (PS2)”**. The rest of the settings will  be up to
   your preference.

| 
| |image129|

-  21.    Click the **"Texture Replacement"** tab, the **"Search
   Directory"** should be auto populated to
   “C:\\Emulation\\PCSX2\\Textures” if you followed this guide to a tee,
   otherwise it will be the textures folder of wherever you placed
   PCSX2. You should never need to change this option as storing your
   textures elsewhere is not covered by this guide. Click the **"Load
   Textures"** checkbox so that it is checked. **"Async Texture
   Loading"** is checked by default.

| 
| |image130|

-  22.    Lastly, click **"BIOS"** and double check that you have a BIOS
   properly installed, else it’ll fail to boot. If you have a USA bios
   showing in your BIOS Selection, you should be all set.

| |image131|

-  23.    Click **"Close"** in PCSX2 settings.

| 
| |image132|

-  24.    Double click Persona 3 FES in your game list to launch the
   game.

| 
| |image133|

-  25.    To fix the window size you can either double click the screen
   to switch to full screen mode, or click **"View"**, then **"Window
   Size"**, then set it to one less than the **"Internal Resolution"**
   you picked.

| 
| |image134|

-  26.    Finally, click **"Settings"**, then **"Controllers"**, then
   click **"Controller Port 1 DualShock 2."**

| 
| |image135|
| |image136|

-  27.    If you’re using a controller, you can select **"Automatic
   Mapping"**, and then find your controller in the list, if you’re
   using a keyboard there are some defaults already set, but you can
   click each button in the window to remap them to how you see fit.

| 
| |image137|
| |image138|

.. |image104| image:: https://i.imgur.com/6y8riOF.png
.. |image105| image:: https://i.imgur.com/WQeu7IC.png
.. |image106| image:: https://i.imgur.com/O9Cx7jo.png
.. |image107| image:: https://i.imgur.com/Mht2OzV.png
.. |image108| image:: https://i.imgur.com/wt8GhJY.png
.. |image109| image:: https://i.imgur.com/S4zyO1b.png
.. |image110| image:: https://i.imgur.com/w6MY3tC.png
.. |image111| image:: https://i.imgur.com/OTBj9uA.png
.. |image112| image:: https://i.imgur.com/ZU4sYcp.png
.. |image113| image:: https://i.imgur.com/dJmpBzi.png
.. |image114| image:: https://i.imgur.com/bE2PNHL.png
.. |image115| image:: https://i.imgur.com/gK4JUyl.png
.. |image116| image:: https://i.imgur.com/YW0CyOc.png
.. |image117| image:: https://i.imgur.com/gqk3Nf9.png
.. |image118| image:: https://i.imgur.com/xhZu6J7.png
.. |image119| image:: https://i.imgur.com/nlTsxAp.png
.. |image120| image:: https://i.imgur.com/Q6NKNPB.png
.. |image121| image:: https://i.imgur.com/nD2BBRV.png
.. |image122| image:: https://i.imgur.com/N801lXQ.png
.. |image123| image:: https://i.imgur.com/WvcW30n.png
.. |image124| image:: https://i.imgur.com/GAAUbuA.png
.. |image125| image:: https://i.imgur.com/imaFd64.png
.. |image126| image:: https://i.imgur.com/OXrUyk3.png
.. |image127| image:: https://i.imgur.com/cQbBdEX.png
.. |image128| image:: https://i.imgur.com/2VghlmF.png
.. |image129| image:: https://i.imgur.com/2jUUMIF.png
.. |image130| image:: https://i.imgur.com/Q70fMKv.png
.. |image131| image:: https://i.imgur.com/NCFnnr3.png
.. |image132| image:: https://i.imgur.com/yWDZuqp.png
.. |image133| image:: https://i.imgur.com/SxHSpxW.png
.. |image134| image:: https://i.imgur.com/KP550Hw.png
.. |image135| image:: https://i.imgur.com/8jXrW6M.png
.. |image136| image:: https://i.imgur.com/LMGGPyF.png
.. |image137| image:: https://i.imgur.com/pd1rgJ3.png
.. |image138| image:: https://i.imgur.com/bVfhAlf.png