PyMapper mapping program.
(c) 2009-2017 Michael Seely

http://www.pymapper.com
Support: pymapper@gmail.com
Bugs:  bugs@pymapper.com

Code count:  41622 lines.  Includes program and resource code totals.

Version 9.6
  A couple of new features make it into this update.  While in 'Icon' mode, right-clicking on an existing icon provides an option to make a copy.  Now, even easier to create a horde of Orcs for your players!  The popup information for icons also now shows the monster type (or NPC class) in the dialog title.

Version 9.5
  So, a bit longer between updates this time.  Several improvements to the xml room editors functionality.  Trying to make bold, italic, or underline text could cause a crash before, and now this has been fixed.  A couple of errors were also found in the 5th edition SRD info.  Turns out the dragons had been seriously underpowered.  The legendary actions have been restored, as well as a few more corrections in the data files.  A few more corrections and some other fixes as detailed in the changes file.  Hopefully you are enjoying the program!

Version 9.4.  Nearly 40000 lines of code!  I was very tempted to write just a few more lines to get over 40k, but I like the symmetry of this number too.  
  This version release of pymapper brings some exciting new features (to me, at least) for those who are playing online.  Pymapper can now update map images online to an ftp server.  This can also be combined with the fog-of-war option to hide sections of the map as the PC's go exploring.  Check out the tutorial available on pymapper.com for more details.
  Placing map icons has been a feature available to pymapper for some time, but the icon shown on the map has been a generic dragons head for monsters, and a generic fighter for NPC's.  Custom images can now be selected (either in the monster/npc dialog, or in the hover dialog) to show more detail on who is fighting, and what is being fought.  These custom images should be placed in the /tokens/ folder in the location where you installed pymapper.  Ideally, these should be 100x100 pixels in size.  Map icons also now have a size attribute, so that a huge creature actually occupies a 3x3 space on the map.  Sizes are split to Small & Medium (1x1), Large (2x2), Huge (3x3), and Gargantuan (4x4).
  The last major improvement deals with tileset creation.  I'll admit, making new tilesets is clunky.  It was part of the very first release of pymapper, and is not very intuitive.  So, now you can add your own images for pymapper to automatically read, creating the tileset definition file for you.  To do this, you will need to create a folder in the /tiles/ folder based on the resolution of the images you wish to use.  Say you have an image that is 50 pixels to the square.  Create a folder named "50__px" in the /tiles/ folder.  Note that there must be two underscore "_" characters separating the resolution value (50 in this example), and the "px" tag.  Drop your images into this new folder, and pymapper will treat it as any other tileset folder, with the assumption that all images share the same resolution.  Incidentally, if you place that same image in a folder named "100__px", then the size of the image in pymapper will reduce.
  

Version 9.3.  A few more lines of code, some new features, and more bugs quashed.  Relevant to this release are some corrections to the image export feature.  Tiles were not being correctly sized when pymapper saved the image file, and this has now been corrected.  This should help in printing as well.  Room and monster/npc icons now have an option to show the name next to the icon, and in the hover dialog, there is a new button to allow for renaming the monster/npc on the fly.  Now you can have Orc1, Orc2, Orc3, and so on.  Or name them if you wish...my orcs never seem to live long enough to get much benefit from having a name, but your mileage may vary.  Also on the hover dialog, there are a series of buttons that assign conditions to the monster (blinded, prone, etc.), which has been there for awhile now.  Now when you change the condition, a color bar will appear under the monster name label. Also new for icons:  the size of the icon shown on the screen is tied to the size of the monster it represents.  And one more thing for icons:  Now, when creating an icon by right-clicking on the map window, a submenu appears to enable selecting room descriptions, monsters, traps, and treasures.  No more having to go through the icon editor just to add a monster.

Version 9.2 is mostly a maintenance update, with several bugs fixed up.  These were mainly from the 5th Edition NPC editor not correctly saving information, or losing information during the save process (which corrupted the file!) and made for a less than stellar experience.  Perhaps one of the biggest improvements deals with changing the map size after you start.  The program can now add rows/columns in any direction, instead of just down and to the right.

Version 9.1 includes some new features for Dungeon Masters.  Creatures and spells from the D&D fifth edition basic rules are now available for use in icons, and as a reference.  Be sure to load dungeon resources, if this is not the default for your setup.  Additional information on the hover dialog for traps and icons are also available.  NPC information such as bonds, flaws, and ideals can now be saved along with your NPC characters.

Version 9.0 adds two major features to the pymapper experience.  Support has been added for the D&D Fifth Edition ruleset.  That is to say, while pymapper includes support 5th edition (and I play it in our home campaign), until Wizards publishes an Open Game Licesnse, there won't be much by the way of actual content included with the program.  You can add your own though, and hopefully the new features will make it worth your while.  The second major feature added to pymapper is the on-screen monster and NPC info that can be displayed on the map.  Yes, there is a tutorial for it, I suggest that you take a look.  Monsters in the d20/Pathfinder ruleset have been added, so those of you playing those systems can jump right in.  If there is a system you would like to see support for, let me know and we can see what can be set up.

Version 8.3 mainly corrects an issue on some versions of Linux that crashed during startup.  Print previewing of tile manifests also has some changes to hopefully make them faster to create.  A preview of the manifest is shown prior to printing as well.

Version 8.2 is a maintenance update.  A bunch of dead code was removed, and some settings changed on dialogs to make them resizable by dragging the corner.  This should help the visibility on some computer configurations.  When importing a new tileset, the tileset name will appear in the page name prompt as a default now.


Version 8.0 adds the fog-of-war to maps.  This makes it possible for a DM/GM to create a map, and then place an overlay on top to hide features from players.  The fog can be selectively removed as players move through the map.  A secondary display box ("Secondary Map Viewport") is available to display on a projector, or just to save snapshots of the map state.  
For those of you using the room icon editor, the DEL key now works properly, instead of having to use SHIFT+DEL to remove characters.

-----------------------------------------
Version 7.0 marks the first significant change in how tilesets are loaded.  Previously, a user had to manually navigate to a folder to find a tileset and open them one at a time.  Pymapper now looks for all .set format files located under the /tiles/ folder where pymapper is installed.  Tilesets should still be installed in their own subfolders, but now a tileset manager takes the place of being able to find what tilesets are available.

Two new types of tiles debut in this version, markers and symbols.  Both can act as normal tiles, but with some additional features.  Markers are user-defined, from the Symbols and Markers manager.  They are available in six different shapes, with customizable colors and short text labels.  These would typically be the monster placement markers found in an adventure.  Markers can act as tiles (they show up on their own tile page) or they can be assigned to a room icon.  If used as an icon, they can have an xml file associated with them to store images, text, etc.  

Symbols are user defined images (either jpg or png format) that facilitate a quick way to create tiles without having to go through the tileset creation process.  Symbols are located in the artwork/symbols folder and are automatically loaded into the Symbols page when pymapper starts.  These symbols must have a size in multiples of 100 pixels (say 100x300, but not 142x227) to load properly.  Pymapper will set the size of the symbol at 100 pixels per square.  Other custom symbols can be added through the Symbol and Marker manager.


-----------------------------------------

Version 6.4 adds a number of bugfixes, and pushes us past the 30k mark for lines of code.  Woohoo!  The biggest addition in this version is the addition of a new operation mode.  Simple tools for drawing lines, circles, etc. is available while in "Draw" mode.  The mode button is at the bottom left of the window.  Select it and the tools will come up.  You can also press F12 to change modes.  Check the changes.txt file for other minor improvements to the program.

Version 6.0 of pymapper introduces pages to the map window display.  Multiple pages can be created and maps loaded to better handle dungeons with multiple levels.  Page information for maps is stored in the map file;  information for tile pages is stored in the pymapper.ini file.  Time to create the ultimate delve!

Version 5.2 adds the long awaited random dungeon generation functionality.  After much development (and much frustration and finally inspiration) a workable randomizer methodology was developed for the program.  Random dungeons are based around the concept of a geomorph, which is a fancy way of saying "a collection of tiles that fit together."  Each geomorph is 12 squares wide and 14 squares high.  Each geomorph has a series of 'connection points' defined to tell pymapper how they align next to other geomorphs.  The dungeon randomizer takes a group of geomorphs and fits them together according to these connection points.  A sample set of geomorphs is included in this release.  Users are highly encouraged to submit new geomorphs so that we can get a wide assortment of options.  The randomizer can be found in the Maps menu.  A tutorial file is also included in the /geomorphs/ folder where you installed pymapper.

Version 5.1 adds a splash screen, extra options for the room icons, and a new way to display tiles on the tile window.  The default now is to show both sides of the tile.  You can drag either image from the tile window and it will pull the matching image onto the map window.  If you prefer the other style (showing one side, with a hover image for the reverse) you can change back to this option in the Options|Program menu.  See the changes.txt file for other new features and bugfixes in this release.

The major change to version 5.0 is the support for the d20/D&D 3.5 SRD.  The d20 information is stored in a folder named /srd/d20 where pymapper is installed.

Menu items that are dimmed out will be activated in later releases.

Pymapper is also now available on SourceForge.  Just so you know.

Note:  Tilesets need to be saved in the \tiles\ subfolder where you installed PyMapper.  The program will be looking for folders named the same as the set ID.  For example, DT2, DU1, etc.

Use the center button on your mouse to drag the map around the screen.  Hold down the center button and drag.

Use the left and right arrow keys to rotate tiles, as well as right-clicking on the map window.

The first step to making maps is to import a tileset.  This can be done by selecting Import Tileset from the File menu.  Then click and drag the tile from the tile display to the map display.

The import tiles function can be used to create new tilesets.  Open the sample.set file in notepad (it's plain text) to see definitions of the tags used in the program.  This file is located in the /tiles/ directory.

Many thanks to everyone for finding bugs and providing suggestions!