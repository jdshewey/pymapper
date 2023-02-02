Hello!

  Pymapper is written using the python computer language.  As such, it is easily ported to 
multiple operating systems.  To run pymapper on Linux or Mac, you will need to download a 
couple of additional bits of software.  You will need the following:

The python interpreter.  This is available for free at http://www.python.org.  You will need
to get version 2.6.4 for use with pymapper.

Second, you will need the wxWidgets package, which controls the windows and dialog boxes.  This
is available from http://www.wxpython.org and you will need version 2.8.10 or above.  

In some cases, you may already have one or both of these installed.   Once you have them installed, 
download the pymapper code file, and unzip to a folder of your choice.  Once unpacked, run the 
pymapper.py file to start pymapper.  The following folders are created automatically by pymapper
in the folder where it is installed: /tiles/ and /maps/.  From the yahoo site, download and install
the tiles into the /tiles/ folder, keeping the tileset ID as a subfolder.  For example, download
the DT1 tileset, and install at /tiles/DT1/ for use.

That's about it for installation.  If you have issues or questions, post them to the Yahoo group
or send an email to pymapper@gmail.com and I'll give what help I can.


Linux (Ubuntu) support:

From a terminal window:
1. First make sure that you have Python installed.  Type 'python' at the prompt and you should start the python interpreter.  The 
   default prompt is >>> so if you see that you are good.  You will also get a notice telling you the version.  It needs to be 2.6 or 
   higher.  Type in exit() to end the python session.
2. Install wxGTK 2.8 with the command, 'sudo apt-get install python-wxgtk2.8'
3. Run the command, 'apt-get source -d wxwidgets2.8'
4  Now run, 'dpkg-source -x wxwidgets2.8_2.8.12.1-6ubuntu2.dsc'   You may need to install dpkg using 'sudo apt-get install dpkg-dev' if
   you don't have that already available.
5. cd wxwidgets2.8-2.8.12.1
6. cd wxPython
7. Now run the command, 'sudo python setup.py install'
wxPython and wxWidgets are now successfully installed!

From here you can run the python code by going to a terminal window, changing to the folder where pymapper is stored, and
type in "python PyMapper8.4.2.py" at the prompt.  You may need to change the name of the PyMapper file since the version changes, and I 
may forget to update this file.







